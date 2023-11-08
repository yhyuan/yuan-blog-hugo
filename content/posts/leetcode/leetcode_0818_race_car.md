---
title: 818. race car
date: '2022-05-22'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0818 race car
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={818}/>
 

  Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions. Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):

  

  	When you get an instruction 'A', your car does the following:

  	

  		position +<TeX>=</TeX> speed

  		speed <TeX>=</TeX> 2

  	

  	

  	When you get an instruction 'R', your car does the following:

  	

  		If your speed is positive then speed <TeX>=</TeX> -1

  		otherwise speed <TeX>=</TeX> 1

  	

  	Your position stays the same.

  

  For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3, and your speed goes to 1 --> 2 --> 4 --> -1.

  Given a target position target, return the length of the shortest sequence of instructions to get there.

   

 >   Example 1:

  

 >   Input: target <TeX>=</TeX> 3

 >   Output: 2

 >   Explanation: 

 >   The shortest instruction sequence is "AA".

 >   Your position goes from 0 --> 1 --> 3.

  

 >   Example 2:

  

 >   Input: target <TeX>=</TeX> 6

 >   Output: 5

 >   Explanation: 

 >   The shortest instruction sequence is "AAARA".

 >   Your position goes from 0 --> 1 --> 3 --> 7 --> 7 --> 6.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> target <TeX>\leq</TeX> 10^4


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

use std::collections::VecDeque;
use std::collections::HashSet;
impl Solution {
    pub fn racecar(target: i32) -> i32 {
        let mut queue: VecDeque<(i32, i32)> = VecDeque::new();
        let mut visited: HashSet<(i32, i32)> = HashSet::new();
        queue.push_back((0, 1));
        visited.insert((0, 1));
        let mut step = 0;
        while queue.len() > 0 {
            let n = queue.len();
            let mut is_found = false;
            for i in 0..n {
                let (pos, speed) = queue.pop_front().unwrap();
                if pos + speed == target {
                    is_found = true;
                    break;
                }
                let state_after_a = (pos + speed, speed * 2);
                if !visited.contains(&state_after_a) {
                    visited.insert(state_after_a);
                    queue.push_back(state_after_a);                    
                }
                let state_after_r = (pos, if speed > 0 {-1} else {1});
                if !visited.contains(&state_after_r) {
                    visited.insert(state_after_r);
                    queue.push_back(state_after_r);                    
                }
            }
            if is_found {
                break;
            }
            step += 1;
        }
        step + 1
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_818() {
        assert_eq!(Solution::racecar(3), 2);
        assert_eq!(Solution::racecar(6), 5);
    }
}

```

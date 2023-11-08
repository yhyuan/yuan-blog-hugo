---
title: 1654. minimum jumps to reach home
date: '2022-08-22'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 1654 minimum jumps to reach home
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1654}/>
 

  A certain bug's home is on the x-axis at position x. Help them get there from position 0.

  The bug jumps according to the following rules:

  

  	It can jump exactly a positions forward (to the right).

  	It can jump exactly b positions backward (to the left).

  	It cannot jump backward twice in a row.

  	It cannot jump to any forbidden positions.

  

  The bug may jump forward beyond its home, but it cannot jump to positions numbered with negative integers.

  Given an array of integers forbidden, where forbidden[i] means that the bug cannot jump to the position forbidden[i], and integers a, b, and x, return the minimum number of jumps needed for the bug to reach its home. If there is no possible sequence of jumps that lands the bug on position x, return -1.

   

 >   Example 1:

  

 >   Input: forbidden <TeX>=</TeX> [14,4,18,1,15], a <TeX>=</TeX> 3, b <TeX>=</TeX> 15, x <TeX>=</TeX> 9

 >   Output: 3

 >   Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.

  

 >   Example 2:

  

 >   Input: forbidden <TeX>=</TeX> [8,3,16,6,12,20], a <TeX>=</TeX> 15, b <TeX>=</TeX> 13, x <TeX>=</TeX> 11

 >   Output: -1

  

 >   Example 3:

  

 >   Input: forbidden <TeX>=</TeX> [1,6,2,14,5,17,4], a <TeX>=</TeX> 16, b <TeX>=</TeX> 9, x <TeX>=</TeX> 7

 >   Output: 2

 >   Explanation: One jump forward (0 -> 16) then one jump backward (16 -> 7) will get the bug home.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> forbidden.length <TeX>\leq</TeX> 1000

 >   	1 <TeX>\leq</TeX> a, b, forbidden[i] <TeX>\leq</TeX> 2000

 >   	0 <TeX>\leq</TeX> x <TeX>\leq</TeX> 2000

 >   	All the elements in forbidden are distinct.

 >   	Position x is not forbidden.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::VecDeque;
impl Solution {
    pub fn minimum_jumps(forbidden: Vec<i32>, a: i32, b: i32, x: i32) -> i32 {
        if x == 0 {
            return 0i32;
        } 
        let a = a as usize;
        let b = b as usize;
        let x = x as usize;
        let len_max = 2000 + 2 * usize::max(a, b) + 1;
        let mut queue: VecDeque<(usize, bool)> = VecDeque::new();
        queue.push_back((0, true));

        let mut lands: Vec<Vec<bool>> = vec![vec![true; 2]; len_max]; // 0: jump left, 1: jump right
        let mut steps = 1;
        //let mut result = -1;

        for &i in forbidden.iter() {
            lands[i as usize][0] = false;
            lands[i as usize][1] = false;
        }

        while !queue.is_empty() {
            let mut next_queue: VecDeque<(usize, bool)> = VecDeque::new();
            while !queue.is_empty() {
                let (i, can_back) = queue.pop_front().unwrap();
                // println!("i: {}, can_back: {}, steps: {}", i, can_back, steps);
                let step_up = i + a;
                //let step_back = i - b;
                if step_up == x || (can_back && i == b + x) {
                    // result = steps as i32;
                    return steps as i32;
                }
                if step_up < len_max && lands[step_up][0] {
                    lands[step_up][0] = false;
                    next_queue.push_back((step_up, true));
                }
                if can_back && i > b && lands[i - b][1] {
                    let step_back = i - b;
                    lands[step_back][1] = false;
                    next_queue.push_back((step_back, false));
                }
            }
            queue = next_queue;
            steps += 1;
        }
        -1
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1654() {
        /*
        assert_eq!(Solution::minimum_jumps(vec![14,4,18,1,15], 3, 15, 9), 3);
        assert_eq!(Solution::minimum_jumps(vec![8,3,16,6,12,20], 15, 13, 11), -1);
        assert_eq!(Solution::minimum_jumps(vec![1,6,2,14,5,17,4], 16, 9, 7), 2);
        assert_eq!(Solution::minimum_jumps(vec![162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98], 29, 98, 80), 121);
        */
        //assert_eq!(Solution::minimum_jumps(vec![61,104,19,60,68,157,183,148,116,93,190,13,177,47,15,133,111], 75, 165, 150), 2);
        assert_eq!(Solution::minimum_jumps(vec![61,104,19,60,68,157,183,148,116,93,190,13,177,47,15,133,111], 75, 165, 150), 2);
    }
}


```

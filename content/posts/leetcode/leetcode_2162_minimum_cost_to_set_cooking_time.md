---
title: 2162. minimum cost to set cooking time
date: '2022-09-15'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 2162 minimum cost to set cooking time
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={2162}/>

A generic microwave supports cooking times for:



at least 1 second.

at most 99 minutes and 99 seconds.

To set the cooking time, you push at most four digits. The microwave normalizes what you push as four digits by prepending zeroes. It interprets the first two digits as the minutes and the last two digits as the seconds. It then adds them up as the cooking time. For example,



You push 9 5 4 (three digits). It is normalized as 0954 and interpreted as 9 minutes and 54 seconds.

You push 0 0 0 8 (four digits). It is interpreted as 0 minutes and 8 seconds.

You push 8 0 9 0. It is interpreted as 80 minutes and 90 seconds.

You push 8 1 3 0. It is interpreted as 81 minutes and 30 seconds.

You are given integers startAt, moveCost, pushCost, and targetSeconds. Initially, your finger is on the digit startAt. Moving the finger above any specific digit costs moveCost units of fatigue. Pushing the digit below the finger once costs pushCost units of fatigue.



There can be multiple ways to set the microwave to cook for targetSeconds seconds but you are interested in the way with the minimum cost.



Return the minimum cost to set targetSeconds seconds of cooking time.



Remember that one minute consists of 60 seconds.



 



 > Example 1:





 > Input: startAt <TeX>=</TeX> 1, moveCost <TeX>=</TeX> 2, pushCost <TeX>=</TeX> 1, targetSeconds <TeX>=</TeX> 600

 > Output: 6

 > Explanation: The following are the possible ways to set the cooking time.

 > - 1 0 0 0, interpreted as 10 minutes and 0 seconds.

 >   The finger is already on digit 1, pushes 1 (with cost 1), moves to 0 (with cost 2), pushes 0 (with cost 1), pushes 0 (with cost 1), and pushes 0 (with cost 1).

 >   The cost is: 1 + 2 + 1 + 1 + 1 <TeX>=</TeX> 6. This is the minimum cost.

 > - 0 9 6 0, interpreted as 9 minutes and 60 seconds. That is also 600 seconds.

 >   The finger moves to 0 (with cost 2), pushes 0 (with cost 1), moves to 9 (with cost 2), pushes 9 (with cost 1), moves to 6 (with cost 2), pushes 6 (with cost 1), moves to 0 (with cost 2), and pushes 0 (with cost 1).

 >   The cost is: 2 + 1 + 2 + 1 + 2 + 1 + 2 + 1 <TeX>=</TeX> 12.

 > - 9 6 0, normalized as 0960 and interpreted as 9 minutes and 60 seconds.

 >   The finger moves to 9 (with cost 2), pushes 9 (with cost 1), moves to 6 (with cost 2), pushes 6 (with cost 1), moves to 0 (with cost 2), and pushes 0 (with cost 1).

 >   The cost is: 2 + 1 + 2 + 1 + 2 + 1 <TeX>=</TeX> 9.

 > Example 2:





 > Input: startAt <TeX>=</TeX> 0, moveCost <TeX>=</TeX> 1, pushCost <TeX>=</TeX> 2, targetSeconds <TeX>=</TeX> 76

 > Output: 6

 > Explanation: The optimal way is to push two digits: 7 6, interpreted as 76 seconds.

 > The finger moves to 7 (with cost 1), pushes 7 (with cost 2), moves to 6 (with cost 1), and pushes 6 (with cost 2). The total cost is: 1 + 2 + 1 + 2 <TeX>=</TeX> 6

 > Note other possible ways are 0076, 076, 0116, and 116, but none of them produces the minimum cost.

 



**Constraints:**



 > 0 <TeX>\leq</TeX> startAt <TeX>\leq</TeX> 9

 > 1 <TeX>\leq</TeX> moveCost, pushCost <TeX>\leq</TeX> 105

 > 1 <TeX>\leq</TeX> targetSeconds <TeX>\leq</TeX> 6039

 > Accepted


## Solution
### Rust
```rust
 pub struct Solution {}
 /*
 use std::collections::HashSet;
 use std::collections::BinaryHeap;
 impl Solution {
    pub fn calculate_seconds(state: i32) -> i32 {
        let seconds = (state / 1000) * 60 + (state % 1000) / 10;
        seconds
    }
    pub fn min_cost_set_time(start_at: i32, move_cost: i32, push_cost: i32, target_seconds: i32) -> i32 {
        // use a 5 digits number to mark the state. The first 4 will be displayed and the last one will be 
        // current finger position.
        // initial state (00000 + start_at)
        // move: change the last digit to 0, 1, 2, 3, ...9 (but not the state's current last digit)
        // push: abcde => bcdee
        // target state: (state / 1000) * 60 + (state % 1000) / 10
        let mut visited: HashSet<i32> = HashSet::new();
        let mut heap: BinaryHeap<(i32, i32)> = BinaryHeap::new();
        let initial_state = 00000 + start_at;
        visited.insert(initial_state);
        heap.push((0, initial_state));
        while heap.len() > 0 {
            let (cost, state) = heap.pop().unwrap();
            /*
            let seconds = (state / 1000) * 60 + (state % 1000) / 10;
            if seconds == target_seconds {
                return cost;
            }
            */
            // bcde state % 10000   e: state % 10
            let push_state = (state % 10000) * 10 + (state % 10);
            if !visited.contains(&push_state) {
                if Self::calculate_seconds(push_state) == target_seconds {
                    return -(cost - push_cost)
                }
                heap.push((cost - push_cost, push_state));    
                visited.insert(initial_state);
            }
            let current_finger = state % 10;
            for i in 0..10i32 {
                if i != current_finger {
                    let move_state = state - current_finger + i;
                    if !visited.contains(&move_state) {
                        if Self::calculate_seconds(move_state) == target_seconds {
                            return -(cost - move_cost)
                        }        
                        heap.push((cost - move_cost, move_state));
                        visited.insert(move_state);
                    }
        
                }
            }
        }
        -1
    }
}
*/
impl Solution {
    pub fn calculate_cost(time: &String, start_at: i32, move_cost: i32, push_cost: i32) -> i32 {
        let chars: Vec<char> = time.chars().collect::<Vec<char>>();
        let mut finger_pos = start_at;
        let mut ans = 0;
        for i in 0..chars.len() {
            let digit = chars[i] as i32 - '0' as i32;
            if finger_pos != digit {
                ans += move_cost;
                finger_pos = digit;
            }
            ans += push_cost;
        }
        ans
    }
    pub fn min_cost_set_time(start_at: i32, move_cost: i32, push_cost: i32, target_seconds: i32) -> i32 {
        let minutes = target_seconds / 60;
        let seconds = target_seconds % 60;
        let mut candidates = vec![];
        if target_seconds < 100 {
            candidates.push(format!("{}", target_seconds));
            if target_seconds >= 60 {
                let time = if seconds >= 10 {format!("{}{}", minutes, seconds)} else {format!("{}0{}", minutes, seconds)};
                candidates.push(time);
            }
        } else {
            candidates.push(if seconds >= 10 {format!("{}{}", minutes, seconds)} else {format!("{}0{}", minutes, seconds)});
            if seconds < 40 {
                let time = format!("{}{}", minutes - 1, seconds + 60);
                candidates.push(time);
            }    
        }
        let mut min_cost = i32::MAX;
        for i in 0..candidates.len() {
            if candidates[i].len() > 4 {
                continue;
            }
            let cost = Self::calculate_cost(&candidates[i], start_at, move_cost, push_cost);
            min_cost = i32::min(min_cost, cost);
        }
        min_cost 
    }
}

// submission codes end
 
 #[cfg(test)]
 mod tests {
     use super::*;
 
     #[test]
     fn test_2162() {
        assert_eq!(Solution::min_cost_set_time(1, 9403, 9402, 6008), 65817);
        
        assert_eq!(Solution::min_cost_set_time(1, 1219, 1218, 73), 4873);
        assert_eq!(Solution::min_cost_set_time(1, 2, 1, 600), 6);
        assert_eq!(Solution::min_cost_set_time(0, 1, 2, 76), 6);
        
    }
 }
 
```

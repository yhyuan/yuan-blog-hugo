---
title: 134. gas station
date: '2021-09-09'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0134 gas station
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={134}/>
 

  There are n gas stations along a circular route, where the amount of gas at the i^th station is gas[i].

  You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the i^th station to its next (i + 1)^th station. You begin the journey with an empty tank at one of the gas stations.

  Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

   

 >   Example 1:

  

 >   Input: gas <TeX>=</TeX> [1,2,3,4,5], cost <TeX>=</TeX> [3,4,5,1,2]

 >   Output: 3

 >   Explanation:

 >   Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank <TeX>=</TeX> 0 + 4 <TeX>=</TeX> 4

 >   Travel to station 4. Your tank <TeX>=</TeX> 4 - 1 + 5 <TeX>=</TeX> 8

 >   Travel to station 0. Your tank <TeX>=</TeX> 8 - 2 + 1 <TeX>=</TeX> 7

 >   Travel to station 1. Your tank <TeX>=</TeX> 7 - 3 + 2 <TeX>=</TeX> 6

 >   Travel to station 2. Your tank <TeX>=</TeX> 6 - 4 + 3 <TeX>=</TeX> 5

 >   Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.

 >   Therefore, return 3 as the starting index.

  

 >   Example 2:

  

 >   Input: gas <TeX>=</TeX> [2,3,4], cost <TeX>=</TeX> [3,4,3]

 >   Output: -1

 >   Explanation:

 >   You can't start at station 0 or 1, as there is not enough gas to travel to the next station.

 >   Let's start at station 2 and fill up with 4 unit of gas. Your tank <TeX>=</TeX> 0 + 4 <TeX>=</TeX> 4

 >   Travel to station 0. Your tank <TeX>=</TeX> 4 - 3 + 2 <TeX>=</TeX> 3

 >   Travel to station 1. Your tank <TeX>=</TeX> 3 - 3 + 3 <TeX>=</TeX> 3

 >   You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.

 >   Therefore, you can't travel around the circuit once no matter where you start.

  

   

  **Constraints:**

  

 >   	gas.length <TeX>=</TeX><TeX>=</TeX> n

 >   	cost.length <TeX>=</TeX><TeX>=</TeX> n

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 10^4

 >   	0 <TeX>\leq</TeX> gas[i], cost[i] <TeX>\leq</TeX> 10^4


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
        let n = gas.len();
        if n < 2 {
            return if gas[0] > cost[0] {0} else {-1};
        }
        for i in 0..n {
            let mut gas_balance = 0;
            let mut is_success = true;
            for j in 0..n {
                gas_balance += gas[(i + j) % n];
                gas_balance -= cost[(i + j) % n];
                //println!("j: {}, gas_balance: {}", j, gas_balance);
                if gas_balance < 0 {
                    is_success = false;
                    //println!("break i: {}", i);
                    break;
                }
            }
            if is_success {
                return i as i32;
            }
        }
        -1
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_134() {
        assert_eq!(Solution::can_complete_circuit(vec![1,2,3,4,5], vec![3,4,5,1,2]), 3);
        assert_eq!(Solution::can_complete_circuit(vec![2,3,4], vec![3,4,3]), -1);
        assert_eq!(Solution::can_complete_circuit(vec![4,5,2,6,5,3], vec![3,2,7,3,2,9]), -1);
        assert_eq!(Solution::can_complete_circuit(vec![4,5,3,1,4], vec![5,4,3,4,2]), -1);
    }
}



```

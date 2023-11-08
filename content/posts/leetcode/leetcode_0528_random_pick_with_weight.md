---
title: 528. random pick with weight
date: '2022-03-26'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0528 random pick with weight
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={528}/>
 

  You are given an array of positive integers w where w[i] describes the weight of i^th index (0-indexed).

  We need to call the function pickIndex() which randomly returns an integer in the range [0, w.length - 1]. pickIndex() should return the integer proportional to its weight in the w array. For example, for w <TeX>=</TeX> [1, 3], the probability of picking the index 0 is 1 / (1 + 3) <TeX>=</TeX> 0.25 (i.e 25%) while the probability of picking the index 1 is 3 / (1 + 3) <TeX>=</TeX> 0.75 (i.e 75%).

  More formally, the probability of picking index i is w[i] / sum(w).

   

 >   Example 1:

  

 >   Input

 >   ["Solution","pickIndex"]

 >   [[[1]],[]]

 >   Output

 >   [null,0]

 >   Explanation

 >   Solution solution <TeX>=</TeX> new Solution([1]);

 >   solution.pickIndex(); // return 0. Since there is only one single element on the array the only option is to return the first element.

  

 >   Example 2:

  

 >   Input

 >   ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]

 >   [[[1,3]],[],[],[],[],[]]

 >   Output

 >   [null,1,1,1,1,0]

 >   Explanation

 >   Solution solution <TeX>=</TeX> new Solution([1, 3]);

 >   solution.pickIndex(); // return 1. It's returning the second element (index <TeX>=</TeX> 1) that has probability of 3/4.

 >   solution.pickIndex(); // return 1

 >   solution.pickIndex(); // return 1

 >   solution.pickIndex(); // return 1

 >   solution.pickIndex(); // return 0. It's returning the first element (index <TeX>=</TeX> 0) that has probability of 1/4.

 >   Since this is a randomization problem, multiple answers are allowed so the following outputs can be considered correct :

 >   [null,1,1,1,1,0]

 >   [null,1,1,1,1,1]

 >   [null,1,1,1,0,0]

 >   [null,1,1,1,0,1]

 >   [null,1,0,1,0,0]

 >   ......

 >   and so on.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> w.length <TeX>\leq</TeX> 10000

 >   	1 <TeX>\leq</TeX> w[i] <TeX>\leq</TeX> 10^5

 >   	pickIndex will be called at most 10000 times.


## Solution
### Rust
```rust
// pub struct Solution {}


// submission codes start here
use rand::Rng;
pub struct Solution {
    pub pre_sum: Vec<i32>,
    pub total: i32,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Solution {

    fn new(w: Vec<i32>) -> Self {
        let total: i32 = w.iter().sum();
        let n = w.len();
        let mut pre_sum: Vec<i32> = vec![0; n];
        pre_sum[0] = w[0];
        for i in 1..n {
            pre_sum[i] = pre_sum[i - 1] + w[i];
        }
        Self {
            pre_sum: pre_sum,
            total: total,
        }
    }
    
    fn pick_index(&self) -> i32 {
        let mut rng = rand::thread_rng();
        let val = rng.gen_range(0, self.total);
        if val < self.pre_sum[0] {
            return 0i32
        }
        println!("random number: {}", val);
        /*if val == 0 {
            return 0i32
        }
        0<= [pre_sum[i], pre_sum[i + 1]) return i + 1
        */
        let mut low = 0; // pre_sum[low] =< val
        let mut high = self.pre_sum.len() - 1; // pre_sum[high] > val
        while low + 1 < high {
            let mid = low + (high - low) / 2;
            if self.pre_sum[mid] > val {
                high = mid;
            } else if self.pre_sum[mid] <= val {
                low = mid;
            }
        }
        if val >= self.pre_sum[low + 1] {
            return low as i32 + 1 + 1;
        }
        low as i32 + 1
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution::new(w);
 * let ret_1: i32 = obj.pick_index();
 */

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_528() {
        let obj = Solution::new(vec![3,14,1,7]);
        println!("pre_sum: {:?}", obj.pre_sum);
        for i in 0..10 {
            println!("pick_index: {}", obj.pick_index());
        }
    }
}

```

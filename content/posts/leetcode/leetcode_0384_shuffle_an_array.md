---
title: 384. shuffle an array
date: '2022-02-08'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0384 shuffle an array
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={384}/>
 

  Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

  Implement the Solution class:

  

  	Solution(int[] nums) Initializes the object with the integer array nums.

  	int[] reset() Resets the array to its original configuration and returns it.

  	int[] shuffle() Returns a random shuffling of the array.

  

   

 >   Example 1:

  

 >   Input

 >   ["Solution", "shuffle", "reset", "shuffle"]

 >   [[[1, 2, 3]], [], [], []]

 >   Output

 >   [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

 >   Explanation

 >   Solution solution <TeX>=</TeX> new Solution([1, 2, 3]);

 >   solution.shuffle();    // Shuffle the array [1,2,3] and return its result.

 >                          // Any permutation of [1,2,3] must be equally likely to be returned.

 >                          // Example: return [3, 1, 2]

 >   solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]

 >   solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 200

 >   	-10^6 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^6

 >   	All the elements of nums are unique.

 >   	At most 5  10^4 calls in total will be made to reset and shuffle.


## Solution
### Rust
```rust
//pub struct Solution {}


// submission codes start here
//Fisher–Yates shuffle
use rand::Rng;
struct Solution {
    nums: Vec<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Solution {

    fn new(nums: Vec<i32>) -> Self {
        let nums = nums;
        Self {nums}
    }
    
    /** Resets the array to its original configuration and return it. */
    fn reset(&self) -> Vec<i32> {
        self.nums.clone()
    }
    
    /** Returns a random shuffling of the array. */
    fn shuffle(&self) -> Vec<i32> {
        let mut nums = self.nums.clone();
        let n = nums.len();
        for i in (0..n).rev() {
            //let j = random.randint(0,i+1)
            // Generate random number in the range [0, 99]
            let j = rand::thread_rng().gen_range(0, i + 1);
            nums.swap(i, j);
        }
        nums
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution::new(nums);
 * let ret_1: Vec<i32> = obj.reset();
 * let ret_2: Vec<i32> = obj.shuffle();
 */

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_384() {
    }
}

```

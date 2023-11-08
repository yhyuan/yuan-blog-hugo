---
title: 398. random pick index
date: '2022-02-22'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0398 random pick index
---



Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Implement the Solution class:



Solution(int[] nums) Initializes the object with the array nums.

int pick(int target) Picks a random index i from nums where nums[i] <TeX>=</TeX><TeX>=</TeX> target. If there are multiple valid i's, then each index should have an equal probability of returning.





>   Example 1:
>   Input
>   ["Solution", "pick", "pick", "pick"]
>   [[[1, 2, 3, 3, 3]], [3], [1], [3]]
>   Output
>   [null, 4, 0, 2]
>   Explanation
>   Solution solution <TeX>=</TeX> new Solution([1, 2, 3, 3, 3]);
>   solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
>   solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
>   solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
**Constraints:**
>   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 2  10^4
>   	-2^31 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 2^31 - 1
>   	target is an integer from nums.
>   	At most 10^4 calls will be made to pick.


## Solution


### Rust
```rust
//pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
use rand::Rng;
pub struct Solution {
hashmap: HashMap<i32, Vec<usize>>,
}


/**
* `&self` means the method takes an immutable reference.
* If you need a mutable reference, change it to `&mut self` instead.
*/
impl Solution {

fn new(nums: Vec<i32>) -> Self {
let mut hashmap: HashMap<i32, Vec<usize>> = HashMap::new();
for (i, num) in nums.iter().enumerate() {
if hashmap.contains_key(num) {
let mut indices = hashmap[num].clone();
indices.push(i);
hashmap.insert(*num, indices);
} else {
hashmap.insert(*num, vec![i]);
}
}
Self {hashmap}
}

fn pick(&self, target: i32) -> i32 {
let indices = &self.hashmap[&target];
let n = indices.len();
let mut rng = rand::thread_rng();
let i = rng.gen_range::<i32, i32, i32>(0, n as i32);
indices[i as usize] as i32
}
}

/**
* Your Solution object will be instantiated and called as such:
* let obj = Solution::new(nums);
* let ret_1: i32 = obj.pick(target);
*/

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_398() {
}
}

```

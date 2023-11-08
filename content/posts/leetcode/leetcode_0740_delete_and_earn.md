---
title: 740. delete and earn
date: '2022-05-06'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0740 delete and earn
---

 

  You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

  

  	Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.

  

  Return the maximum number of points you can earn by applying the above operation some number of times.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [3,4,2]

 >   Output: 6

 >   Explanation: You can perform the following operations:

 >   - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums <TeX>=</TeX> [2].

 >   - Delete 2 to earn 2 points. nums <TeX>=</TeX> [].

 >   You earn a total of 6 points.

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [2,2,3,3,3,4]

 >   Output: 9

 >   Explanation: You can perform the following operations:

 >   - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums <TeX>=</TeX> [3,3].

 >   - Delete a 3 again to earn 3 points. nums <TeX>=</TeX> [3].

 >   - Delete a 3 once more to earn 3 points. nums <TeX>=</TeX> [].

 >   You earn a total of 9 points.

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 2  10^4

 >   	1 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^4


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
impl Solution {
    pub fn delete_and_earn(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 1 {
            return nums[0];
        }
        let mut hashmap: HashMap<i32, usize> = HashMap::new();
        for i in 0..n {
            if hashmap.contains_key(&nums[i]) {
                *hashmap.get_mut(&nums[i]).unwrap() += 1;
            } else {
                hashmap.insert(nums[i], 1);
            }
        }
        let mut indices = hashmap.keys().cloned().collect::<Vec<_>>();
        let max_num = *indices.iter().max().unwrap();
        //We want maxPoints(num) to return the maximum points that we can gain if we only consider all the elements in nums with values between 0 and num.
        //maxPoints(x) = max(maxPoints(x - 1), maxPoints(x - 2) + gain),
        //First, maxPoints(0) will always be equal to 0. Second, when considering maxPoints(1)
        if max_num == 0 {
            return 0;
        }
        let mut dp = (0, 0);
        // let mut dp = vec![0; max_num as usize + 1];
        if hashmap.contains_key(&1) {
            // dp[1] = *hashmap.get(&1).unwrap() as i32;
            dp.1 = *hashmap.get(&1).unwrap() as i32;
        }
        for i in 2..=max_num as usize {
            let k = i as i32;
            let gain = if hashmap.contains_key(&k) {
                *hashmap.get(&k).unwrap() as i32 * k
            } else {0};
            //dp[i] = i32::max(dp[i - 1], dp[i - 2] + gain);
            dp = (dp.1, i32::max(dp.1, dp.0 + gain));
        }
        //println!("{:?}", dp);
       //dp[max_num as usize]
       dp.1
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_740() {
        assert_eq!(Solution::delete_and_earn(vec![3,4,2]), 6);
        assert_eq!(Solution::delete_and_earn(vec![2,2,3,3,3,4]), 9);
        assert_eq!(Solution::delete_and_earn(vec![8,3,4,7,6,6,9,2,5,8,2,4,9,5,9,1,5,7,1,4]), 61);
    }
}


```

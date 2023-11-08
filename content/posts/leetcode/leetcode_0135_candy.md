---
title: 135. candy
date: '2021-09-10'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0135 candy
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={135}/>
 

  There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

  You are giving candies to these children subjected to the following requirements:

  

  	Each child must have at least one candy.

  	Children with a higher rating get more candies than their neighbors.

  

  Return the minimum number of candies you need to have to distribute the candies to the children.

   

 >   Example 1:

  

 >   Input: ratings <TeX>=</TeX> [1,0,2]

 >   Output: 5

 >   Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

  

 >   Example 2:

  

 >   Input: ratings <TeX>=</TeX> [1,2,2]

 >   Output: 4

 >   Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.

 >   The third child gets 1 candy because it satisfies the above two conditions.

  

   

  **Constraints:**

  

 >   	n <TeX>=</TeX><TeX>=</TeX> ratings.length

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 2  10^4

 >   	0 <TeX>\leq</TeX> ratings[i] <TeX>\leq</TeX> 2  10^4


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn candy(ratings: Vec<i32>) -> i32 {
        let n = ratings.len();
        let mut candies = vec![1; n];
        for i in 0..n - 1 {
            if ratings[i + 1] > ratings[i] {
                candies[i + 1] = candies[i] + 1;
            }
        }
        for i in (0..n - 1).rev() {
            if ratings[i] > ratings[i + 1] && candies[i] <= candies[i + 1] {
                candies[i] = candies[i + 1] + 1;
            }
        }
        let result = candies.into_iter().fold(0, |sum, val| sum  + val);
        result
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_135() {
        assert_eq!(Solution::candy(vec![1,0,2]), 5);
        assert_eq!(Solution::candy(vec![1,2,2]), 4);
        assert_eq!(Solution::candy(vec![1,3,4,5,2]), 11);
    }
}

```

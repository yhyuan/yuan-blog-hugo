---
title: 278. first bad version
date: '2021-12-14'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0278 first bad version
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={278}/>
 

  You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

  Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

  You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

   

 >   Example 1:

  

 >   Input: n <TeX>=</TeX> 5, bad <TeX>=</TeX> 4

 >   Output: 4

 >   Explanation:

 >   call isBadVersion(3) -> false

 >   call isBadVersion(5) -> true

 >   call isBadVersion(4) -> true

 >   Then 4 is the first bad version.

  

 >   Example 2:

  

 >   Input: n <TeX>=</TeX> 1, bad <TeX>=</TeX> 1

 >   Output: 1

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> bad <TeX>\leq</TeX> n <TeX>\leq</TeX> 2^31 - 1


## Solution
### Rust
```rust
pub struct Solution {
  pub bad_version: i32,
}


// submission codes start here

// The API isBadVersion is defined for you.
// isBadVersion(versions:i32)-> bool;
// to call it use self.isBadVersion(versions)

impl Solution {
    pub fn new(bad_version: i32) -> Self {
      Solution {bad_version: bad_version}
    }
    pub fn isBadVersion(&self, n: i32) -> bool {
      self.bad_version <= n
    }
    pub fn first_bad_version(&self, n: i32) -> i32 {
      if self.isBadVersion(0) {
        return 0;
      }
      let mut low = 0;
      let mut high = n;
      while low + 1 < high {
        let mid = low + (high - low) / 2;
        if self.isBadVersion(mid) {
          high = mid;
        } else {
          low = mid
        }
      }
      if self.isBadVersion(low) {
        return low;
      }
      high
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use crate::solution;

    use super::*;

    #[test]
    fn test_278() {
      assert_eq!( Solution::new(4).first_bad_version(5), 4);
    }
}

```

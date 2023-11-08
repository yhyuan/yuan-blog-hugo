---
title: 552. student attendance record ii
date: '2022-04-01'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0552 student attendance record ii
---

 

  An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

  

  	'A': Absent.

  	'L': Late.

  	'P': Present.

  

  Any student is eligible for an attendance award if they meet both of the following criteria:

  

  	The student was absent ('A') for strictly fewer than 2 days total.

  	The student was never late ('L') for 3 or more consecutive days.

  

  Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 10^9 + 7.

   

 >   Example 1:

  

 >   Input: n <TeX>=</TeX> 2

 >   Output: 8

 >   Explanation: There are 8 records with length 2 that are eligible for an award:

 >   "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"

 >   Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).

  

 >   Example 2:

  

 >   Input: n <TeX>=</TeX> 1

 >   Output: 3

  

 >   Example 3:

  

 >   Input: n <TeX>=</TeX> 10101

 >   Output: 183236316

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 10^5


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/**
 * A is allowed only once or A is not allowed. 
 * If A is not allowed, we can only have L and P. The total number of possibility is 2^n. L is allow one or 
 * twice continuously. Let's name the count is f(n). n is the length of array.
 * if A is allowed once, A can be in 0, 1, 2.... n - 1. A's position will divide the list to
 * two smaller array. The first part's length is k, the second part's length is n - 1 - k. 
 * In the first part and second part, L is only allowed once or twince continuously. So the result is 
 * Sum(f(k) * f(n - 1 - k)) k = 0, 1, 2, 3, .... n - 1
 *
 * Now the problem is simplified. Let's have a array with length n. The total number of possible array is 2^n. We need
 * to figrue out how many of them did not contain more than 2 consecutive L. Let's mark the result at n - 1 with four numbers
 * 1. The results end with LL. v1
 * 2. The results end with PL  v2
 * 3. The results end with PP  v3
 * 4. The results end with LP  v4
 * 
 * Then, for n, 
 * 1. The reults ends with LL. next_v1 = v2 (It can only be possible that we add L behind PL).
 * 2. The results ends with PL next_v2 = v3 + v4 (It can only be possible that we add L behind PP and LP).
 * 3. The results ends with PP. next_v3 = v3 + v4 (It can only be possible that we add P behind PP and LP).
 * 4. The resutls ends with LP  next_v4 = v1 + v2 (It can only be possible that we add P behind LL and PL).
 * 
 * n = 1 
 * 
 */
impl Solution {
    pub fn calculate_dp(n: usize) -> Vec<i64> {
        let mut dp: Vec<i64> = vec![1, 2, 4];
        let mut current = (1, 1, 1, 1);
        if n >= 3 {
            for i in 3..=n {
                let (v1, v2, v3, v4) = current;
                current = (v2, (v3 + v4) % 1000000007, (v3 + v4) % 1000000007, (v1 + v2) % 1000000007);
                let mut res = current.0;
                res = (res + current.1) % 1000000007;
                res = (res + current.2) % 1000000007;
                res = (res + current.3) % 1000000007;
                dp.push(res);
            }    
        }
        dp
    }
    pub fn check_record(n: i32) -> i32 {
        let n = n as usize;
        let dp: Vec<i64> = Self::calculate_dp(n);
        let mut ans = dp[n];
        for k in 0..=n - 1 {
            ans += (dp[k] * dp[n - 1 - k]) % 1000000007;
            ans = ans % 1000000007;
        }
        ans as i32
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_552() {
        assert_eq!(Solution::check_record(1), 3);
        assert_eq!(Solution::check_record(2), 8);
        assert_eq!(Solution::check_record(10101), 183236316);
    }
}

```

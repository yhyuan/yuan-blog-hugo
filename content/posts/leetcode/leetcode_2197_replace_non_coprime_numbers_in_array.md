---
title: 2197. replace non coprime numbers in array
date: '2022-09-27'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 2197 replace non coprime numbers in array
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={2197}/>

You are given an array of integers nums. Perform the following steps:



Find any two adjacent numbers in nums that are non-coprime.

If no such numbers are found, stop the process.

Otherwise, delete the two numbers and replace them with their LCM (Least Common Multiple).

Repeat this process as long as you keep finding two adjacent non-coprime numbers.

Return the final modified array. It can be shown that replacing adjacent non-coprime numbers in any arbitrary order will lead to the same result.



The test cases are generated such that the values in the final array are less than or equal to 108.



Two values x and y are non-coprime if GCD(x, y) > 1 where GCD(x, y) is the Greatest Common Divisor of x and y.



 



 > Example 1:



 > Input: nums <TeX>=</TeX> [6,4,3,2,7,6,2]

 > Output: [12,7,6]

 > Explanation: 

 > - (6, 4) are non-coprime with LCM(6, 4) <TeX>=</TeX> 12. Now, nums <TeX>=</TeX> [12,3,2,7,6,2].

 > - (12, 3) are non-coprime with LCM(12, 3) <TeX>=</TeX> 12. Now, nums <TeX>=</TeX> [12,2,7,6,2].

 > - (12, 2) are non-coprime with LCM(12, 2) <TeX>=</TeX> 12. Now, nums <TeX>=</TeX> [12,7,6,2].

 > - (6, 2) are non-coprime with LCM(6, 2) <TeX>=</TeX> 6. Now, nums <TeX>=</TeX> [12,7,6].

 > There are no more adjacent non-coprime numbers in nums.

 > Thus, the final modified array is [12,7,6].

 > Note that there are other ways to obtain the same resultant array.

 > Example 2:



 > Input: nums <TeX>=</TeX> [2,2,1,1,3,3,3]

 > Output: [2,1,1,3]

 > Explanation: 

 > - (3, 3) are non-coprime with LCM(3, 3) <TeX>=</TeX> 3. Now, nums <TeX>=</TeX> [2,2,1,1,3,3].

 > - (3, 3) are non-coprime with LCM(3, 3) <TeX>=</TeX> 3. Now, nums <TeX>=</TeX> [2,2,1,1,3].

 > - (2, 2) are non-coprime with LCM(2, 2) <TeX>=</TeX> 2. Now, nums <TeX>=</TeX> [2,1,1,3].

 > There are no more adjacent non-coprime numbers in nums.

 > Thus, the final modified array is [2,1,1,3].

 > Note that there are other ways to obtain the same resultant array.

 



**Constraints:**



 > 1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 105

 > 1 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 105

 > The test cases are generated such that the values in the final array are less than or equal to 108.

 > Accepted

 > 3,826


## Solution
### Rust
```rust
pub struct Solution {}
impl Solution {
    pub fn gcd(num1: i32, num2: i32) -> i32 {
        let num3 = num2 % num1;
        if num3 == 0 {
            return num1;
        }
        return Self::gcd(num3, num1);
    }
    pub fn replace_non_coprimes(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut stack: Vec<i32> = vec![];
        for i in 0..n {
            stack.push(nums[i]);
            while stack.len() > 1 {
                let num1 = stack[stack.len() - 1];
                let num2 = stack[stack.len() - 2];
                println!("num1: {}, num2: {}", num1, num2);
                let gcd = if num1 < num2 {Self::gcd(num1, num2)} else {Self::gcd(num2, num1)};
                println!("gcd: {}", gcd);
                if gcd == 1 {
                    break;
                }
                let lcm = num1 / gcd * num2;
                stack.pop();
                stack.pop();
                stack.push(lcm);
            }
        }
        stack
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_2197() {
        assert_eq!(Solution::replace_non_coprimes(vec![6,4,3,2,7,6,2]), vec![12,7,6]);        
    }
}



```

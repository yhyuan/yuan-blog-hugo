---
title: 2167. minimum time to remove all cars containing illegal goods
date: '2022-09-19'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 2167 minimum time to remove all cars containing illegal goods
---


You are given a 0-indexed binary string s which represents a sequence of train cars. s[i] <TeX>=</TeX> '0' denotes that the ith car does not contain illegal goods and s[i] <TeX>=</TeX> '1' denotes that the ith car does contain illegal goods.



As the train conductor, you would like to get rid of all the cars containing illegal goods. You can do any of the following three operations any number of times:



Remove a train car from the left end (i.e., remove s[0]) which takes 1 unit of time.

Remove a train car from the right end (i.e., remove s[s.length - 1]) which takes 1 unit of time.

Remove a train car from anywhere in the sequence which takes 2 units of time.

Return the minimum time to remove all the cars containing illegal goods.



Note that an empty sequence of cars is considered to have no cars containing illegal goods.



 



 > Example 1:



 > Input: s <TeX>=</TeX> "1100101"

 > Output: 5

 > Explanation: 

 > One way to remove all the cars containing illegal goods from the sequence is to

 > - remove a car from the left end 2 times. Time taken is 2  1 <TeX>=</TeX> 2.

 > - remove a car from the right end. Time taken is 1.

 > - remove the car containing illegal goods found in the middle. Time taken is 2.

 > This obtains a total time of 2 + 1 + 2 <TeX>=</TeX> 5. 



 > An alternative way is to

 > - remove a car from the left end 2 times. Time taken is 2  1 <TeX>=</TeX> 2.

 > - remove a car from the right end 3 times. Time taken is 3  1 <TeX>=</TeX> 3.

 > This also obtains a total time of 2 + 3 <TeX>=</TeX> 5.



 > 5 is the minimum time taken to remove all the cars containing illegal goods. 

 > There are no other ways to remove them with less time.

 > Example 2:



 > Input: s <TeX>=</TeX> "0010"

 > Output: 2

 > Explanation:

 > One way to remove all the cars containing illegal goods from the sequence is to

 > - remove a car from the left end 3 times. Time taken is 3  1 <TeX>=</TeX> 3.

 > This obtains a total time of 3.



 > Another way to remove all the cars containing illegal goods from the sequence is to

 > - remove the car containing illegal goods found in the middle. Time taken is 2.

 > This obtains a total time of 2.



 > Another way to remove all the cars containing illegal goods from the sequence is to 

 > - remove a car from the right end 2 times. Time taken is 2  1 <TeX>=</TeX> 2. 

 > This obtains a total time of 2.



 > 2 is the minimum time taken to remove all the cars containing illegal goods. 

 > There are no other ways to remove them with less time.

 



**Constraints:**



 > 1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 2  105

 > s[i] is either '0' or '1'.

 > Accepted

 > 1,380

 > Submissions


## Solution
### Rust
```rust
use std::collections::HashMap;
pub struct Solution {}
impl Solution {
    /* 
    pub fn minimum_time_helper(s: &String, count_ones: usize, memo: &mut HashMap<String, i32>) -> i32 {
        if count_ones == 0 {
            return 0i32;
        }
        if memo.contains_key(s) {
            return *memo.get(s).unwrap();
        }
        let chars: Vec<char> = s.chars().collect();
        let n = chars.len();        
        if chars[0] == '1' {
            let remove_first = format!("{}", &s[1..]);
            let r = 1 + Self::minimum_time_helper(&remove_first, count_ones - 1, memo);
            memo.insert(format!("{}", s), r);
            return r
        }
        if chars[n - 1] == '1' {
            let remove_last = format!("{}", &s[..n - 1]);
            let r = 1 + Self::minimum_time_helper(&remove_last, count_ones - 1, memo);
            memo.insert(format!("{}", s), r);
            return r
        }
        //println!("chars: {:?}", &chars[start..=end]);
        let mut i = 0;
        while chars[i] != '1' {
            i = i + 1;
        }
        let start_step = i;
        let mut i = n - 1;
        while chars[i] != '1' {
            i = i - 1;
        }
        let end_step = i;
        let remove_index = if start_step - 0 < n - 1 - end_step {start_step} else {end_step};
        let remove_middle = format!("{}{}", &s[..remove_index], &s[remove_index + 1..]);
        let r_remove_middle = 2 + Self::minimum_time_helper(&remove_middle, count_ones - 1, memo);

        let r = if start_step - 0 < n - 1 - end_step {
            let remove_first = format!("{}", &s[1..]);
            let r_remove_first = 1 + Self::minimum_time_helper(&remove_first, count_ones, memo);
            i32::min(r_remove_first, r_remove_middle)
        } else {
            let remove_last = format!("{}", &s[..n - 1]);
            let r_remove_last = 1 + Self::minimum_time_helper(&remove_last, count_ones, memo);            
            i32::min(r_remove_last, r_remove_middle)
        };
        memo.insert(format!("{}", s), r);
        r
    }
    pub fn minimum_time(s: String) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        //let n = chars.len();
        let count_ones = chars.iter().filter(|&x| x == &'1').count();
        let mut memo: HashMap<String, i32> = HashMap::new();
        //println!("count_ones:{}", count_ones);
        Self::minimum_time_helper(&s, count_ones, &mut memo)
    }
    */
    pub fn remove_left(chars: &Vec<char>, start: usize, end: usize) -> i32 {
        let mut k = 0;
        let mut result = 0;
        for i in start..=end {
            if chars[i] == '1' {
                result = k;
            }
            k = k + 1;
        }
        result
    }
    
    pub fn remove_right(chars: &Vec<char>, start: usize, end: usize) -> i32 {
        let mut k = 0;
        let mut result = 0;
        for i in (start..=end).rev() {
            if chars[i] == '1' {
                result = k;
            }
            k = k + 1;
        }
        result
    }
    /**
     * Now, the question is how to choose left and right parts, we can have potentially O(n^2) options and we can not check them all. Let us calculate how much 
     * we paid:
     * |..left..|..middle..|..right..|
     * For left and right we paid just their lengths. For middle we pay twice number of ones se have inside, so we have: 
     * len(left) + 2* count(middle, 1) + len(right) = len(left) + len(middle) + len(right) + 2*count(middle, 1) - len(middle) = n + count(middle, 1) - count(middle, 0).
     * So, in fact what we need to found is the subarray with the smallest count(middle, 1) - count(middle, 0) value. If we now replace all 0 with -1, it is the same 
     * as found the subarray with the smallest sum! And we can use classical dp solution for problem 53. Maximum Subarray. Do not forgot about empty array case, 
     * it costs me 5min penalty on the contest.
     */
    pub fn minimum_time(s: String) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        /* 
        let sum_val: i8 = chars.iter().map(|&c| if c == '0' {0} else {1}).sum();
        if sum_val == 0i8 {
            return 0i32;
        }
        */
        let nums: Vec<i32> = chars.iter().map(|&c| if c == '0' {-1} else {1}).collect();
        let n = nums.len();
        let mut dp: Vec<i32> = vec![0; n];
        dp[0] = nums[0];
        for i in 1..n {
            dp[i] = i32::min(dp[i - 1] + nums[i], nums[i]);
        }
        let min_value = i32::min(0, *dp.iter().min().unwrap());
        n as i32 + min_value
        // 0i32
        //let count_ones = chars.iter().filter(|&x| x == &'1').count();
        //let mut memo: HashMap<String, i32> = HashMap::new();
        //println!("count_ones:{}", count_ones);
        //Self::minimum_time_helper(&s, count_ones, &mut memo)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_2167() {
        /*
        println!("{}", Solution::minimum_time("1100101".to_string()));
        println!("{}", Solution::minimum_time("0010".to_string()));
        println!("{}", Solution::minimum_time("1001010101".to_string()));
        println!("{}", Solution::minimum_time("011001111111101001010000001010011".to_string()));
        
        println!("{}", Solution::minimum_time("1010101001000111101110011011010111101000001010111110011111101011000010010111000000110000111010000101101010100100110100101001001100111000100000101011101011000101100100111001011101100011010011111000101110010101110010011010111001011000111110110001100101100011011000101110001001100111111011100000011001111111111011001111111011010101010011100010110101101100101101001000010001110010001101111010000000010110100110000111000000111011100000100011110101111100001001011111101011001100001110010101100101001100000110101000100000001001111101100101001101110111011110011110100001100011100110100001101111001010011001111111111011000101010111001100001011101001100001111001000111100111111101101100000001011010101010100010001111101001111011101010111100110011111001101011010100001101001111011111101000011011110101110011111101000111010101100101110000001100111000111111111000000100001100010001010100100000000110100111111110000110011101010100111011100010010011011101010000110101101101001100110000100011110010101101100010101100111000000001011100011000001000001100100100000000110100011011101111100100101110000000111101101101010000010111011110100000111101101011001010011110001011000010011001010000011000001001110010101011010111000110101010110101010100100001101111101010000010101010100010100000110010100110001000010000000001101000110011001111011111001110010010010001010010001000001100101111101001100001001000010111000001000100000011101110111010111110011111110101001111110001010110111111001110011100000010110001010011101110001001111000011001000111101100000011111111010100101001111001101111010101001001011100111110110111001010111101110100011010001011110101000100100110011111001011101001011000010000100111100100111101011100011101111011000000111110011110000100101111101111100100101000101101101111111110101110101111000110011111000011011010001001100111000010100111110000100011110010001110110010010000100011011001010101000110000010000111000010101101111000011001010010011000000001100011100111110001011011101110111001110101110000111001011000101111011001011011101110111111001111010000010100011011100001000110110000001000100110100001001100100101101011111100101100101100101010100100111011111010011011100111010110010011110101001011101101010111111111101111100111001110000101000011010001110000111001011010000101000101111110001000010001001111110100111111001000010001100000100101011110100011011100110110011000000110100100010110100101011010010011111110011111100111001001110111001010000010100000010101001011000000011000100010000100011000000110011101110111000011011001100001100111101000101000110110101111110100011001011100100010101000110110101011001110100100110110110110001001111011010000010011010000010001100100100010111010001100010110000100111111000010010001010001000011010010100010100001100100011010000000011101000010110011100101110111100100000110110111000100010001010111100011010110001101111100110110110110010100111001010000101011001011101011101111111010111001001100011100001000010011001110101011001001001001101101001101101010011001010011111001010100110010010000111100011001011011100000010101101110101111011110000011001000000000111000010001001001101001001111111100100101011101100010011010011101000101101101011101010101101111010110100110100000010111101100100011111011011100000100000101111010010001011100000000111110000011001100011001101101011011001011101001110111001110001011110010110100111100011001100100011010010011101100001011010111010100111111111011000101010100110011000011011110111111101111000100100110010110100001001000110111101001011101100000100000100100111101011101101110010111110111011110101000000111000010101100110010111001101001011011110100110110100111100110101110111010001011101010001100000101111110000111111101101000101101010000100001101110101110111111100110010000010100110110101100001110011100010110100111110011101001110100101010001001000100000011111100011111011000100010111110110100100010101101100011110111001110000101011111100111001001111001110010110001110101010100111111000011000110100100000010100101101110111110001110100100101111100010100001101110000011000001000010101100110011101000100100000001010100000110101001101000000100100111110111010100000101000011001101100011011111111010001100110010110010010010010111000010111100011101101000010110001010001110100100110001010111111110100000011001000000011110110011001111001110101111001111000111100010001101010110110000001011000011000100000111011101011011010011100000101011010011010111100110110110100011001101101111011011010000010001100000000111011111001001100010010001000101001011010101100010001010001010011000000011111100000111101010111000000101010111001011101100101010000001010000011111111100011011110110101100111101100010111101111001111000100001111110010111001001100111".to_string()));
        */        
        assert_eq!(Solution::minimum_time("1100101".to_string()), 5);        
        assert_eq!(Solution::minimum_time("0010".to_string()), 2);        
        assert_eq!(Solution::minimum_time("1".to_string()), 1);        

    }
}


```

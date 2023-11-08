---
title: 975. odd even jump
date: '2022-06-19'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0975 odd even jump
---

 

  You are given an integer array arr. From some starting index, you can make a series of jumps. The (1^st, 3^rd, 5^th, ...) jumps in the series are called odd-numbered jumps, and the (2^nd, 4^th, 6^th, ...) jumps in the series are called even-numbered jumps. Note that the jumps are numbered, not the indices.

  You may jump forward from index i to index j (with i < j) in the following way:

  

  	During odd-numbered jumps (i.e., jumps 1, 3, 5, ...), you jump to the index j such that arr[i] <TeX>\leq</TeX> arr[j] and arr[j] is the smallest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.

  	During even-numbered jumps (i.e., jumps 2, 4, 6, ...), you jump to the index j such that arr[i] ><TeX>=</TeX> arr[j] and arr[j] is the largest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.

  	It may be the case that for some index i, there are no legal jumps.

  

  A starting index is good if, starting from that index, you can reach the end of the array (index arr.length - 1) by jumping some number of times (possibly 0 or more than once).

  Return the number of good starting indices.

   

 >   Example 1:

  

 >   Input: arr <TeX>=</TeX> [10,13,12,14,15]

 >   Output: 2

 >   Explanation: 

 >   From starting index i <TeX>=</TeX> 0, we can make our 1st jump to i <TeX>=</TeX> 2 (since arr[2] is the smallest among arr[1], arr[2], arr[3], arr[4] that is greater or equal to arr[0]), then we cannot jump any more.

 >   From starting index i <TeX>=</TeX> 1 and i <TeX>=</TeX> 2, we can make our 1st jump to i <TeX>=</TeX> 3, then we cannot jump any more.

 >   From starting index i <TeX>=</TeX> 3, we can make our 1st jump to i <TeX>=</TeX> 4, so we have reached the end.

 >   From starting index i <TeX>=</TeX> 4, we have reached the end already.

 >   In total, there are 2 different starting indices i <TeX>=</TeX> 3 and i <TeX>=</TeX> 4, where we can reach the end with some number of

 >   jumps.

  

 >   Example 2:

  

 >   Input: arr <TeX>=</TeX> [2,3,1,1,4]

 >   Output: 3

 >   Explanation: 

 >   From starting index i <TeX>=</TeX> 0, we make jumps to i <TeX>=</TeX> 1, i <TeX>=</TeX> 2, i <TeX>=</TeX> 3:

 >   During our 1st jump (odd-numbered), we first jump to i <TeX>=</TeX> 1 because arr[1] is the smallest value in [arr[1], arr[2], arr[3], arr[4]] that is greater than or equal to arr[0].

 >   During our 2nd jump (even-numbered), we jump from i <TeX>=</TeX> 1 to i <TeX>=</TeX> 2 because arr[2] is the largest value in [arr[2], arr[3], arr[4]] that is less than or equal to arr[1]. arr[3] is also the largest value, but 2 is a smaller index, so we can only jump to i <TeX>=</TeX> 2 and not i <TeX>=</TeX> 3

 >   During our 3rd jump (odd-numbered), we jump from i <TeX>=</TeX> 2 to i <TeX>=</TeX> 3 because arr[3] is the smallest value in [arr[3], arr[4]] that is greater than or equal to arr[2].

 >   We can't jump from i <TeX>=</TeX> 3 to i <TeX>=</TeX> 4, so the starting index i <TeX>=</TeX> 0 is not good.

 >   In a similar manner, we can deduce that:

 >   From starting index i <TeX>=</TeX> 1, we jump to i <TeX>=</TeX> 4, so we reach the end.

 >   From starting index i <TeX>=</TeX> 2, we jump to i <TeX>=</TeX> 3, and then we can't jump anymore.

 >   From starting index i <TeX>=</TeX> 3, we jump to i <TeX>=</TeX> 4, so we reach the end.

 >   From starting index i <TeX>=</TeX> 4, we are already at the end.

 >   In total, there are 3 different starting indices i <TeX>=</TeX> 1, i <TeX>=</TeX> 3, and i <TeX>=</TeX> 4, where we can reach the end with some

 >   number of jumps.

  

 >   Example 3:

  

 >   Input: arr <TeX>=</TeX> [5,1,3,4,2]

 >   Output: 3

 >   Explanation: We can reach the end from starting indices 1, 2, and 4.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> arr.length <TeX>\leq</TeX> 2  10^4

 >   	0 <TeX>\leq</TeX> arr[i] < 10^5


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
impl Solution {
    pub fn odd_even_jumps_helper(arr: &Vec<i32>, odd_jump: &Vec<usize>, even_jump: &Vec<usize>, index: usize, is_odd_jump: bool, memo: &mut HashMap<(usize, bool), bool>) -> bool {
        if memo.contains_key(&(index, is_odd_jump)) {
            return memo[&(index, is_odd_jump)];
        }
        //println!("index: {}", index);
        //let n = arr.len();
        let next_index = if is_odd_jump {odd_jump[index]} else {even_jump[index]};
        if next_index == usize::MAX {
            memo.insert((index, is_odd_jump), false);
            return false;                   
        }
        let res = Self::odd_even_jumps_helper(arr, odd_jump, even_jump, next_index, !is_odd_jump, memo);
        memo.insert((index, is_odd_jump), res);
        return res;
    }

    pub fn find_jump(arr_val_index: &Vec<(i32, usize)>) -> Vec<usize> {
        let n = arr_val_index.len();
        let mut result: Vec<usize> = vec![usize::MAX; n];
        let mut stack: Vec<usize> = vec![];
        for i in 0..n {
            let index = arr_val_index[i].1;
            //println!("index: {}", index);
            while stack.len() > 0 && index > stack[stack.len() - 1] {
                let val = stack.pop().unwrap();
                result[val] = index;
            }
            stack.push(index);
            //println!("stack: {:?}", stack);
        }
        result
    }

    pub fn odd_even_jumps(arr: Vec<i32>) -> i32 {        
        let n = arr.len();
        let mut arr_val_index = (0..n).into_iter().map(|i| (arr[i], i)).collect::<Vec<_>>();
        arr_val_index.sort();
        let odd_jump = Self::find_jump(&arr_val_index);
        //println!("odd_jump:{:?}", odd_jump);
        let mut arr_val_index_rev = (0..n).into_iter().map(|i| (-arr[i], i)).collect::<Vec<_>>();
        arr_val_index_rev.sort();
        let even_jump = Self::find_jump(&arr_val_index_rev);
        //println!("even_jump:{:?}", even_jump);
        // at position i, use odd or jump whether we can reach final position
        let mut memo: HashMap<(usize, bool), bool> = HashMap::new();
        memo.insert((n - 1, true), true);
        memo.insert((n - 1, false), true);
        let mut ans = 0;
        for i in (0..n).rev() {
            let res = Self::odd_even_jumps_helper(&arr, &odd_jump, &even_jump,  i, true, &mut memo);
            // println!("i: {}, res: {:?}", i, res);
            if res {
                ans += 1;
            }
        }
        ans
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_975() {
        assert_eq!(Solution::odd_even_jumps(vec![5,1,3,4,2]), 3);
        assert_eq!(Solution::odd_even_jumps(vec![10,13,12,14,15]), 2);
        assert_eq!(Solution::odd_even_jumps(vec![2,3,1,1,4]), 3);
    }
}

```

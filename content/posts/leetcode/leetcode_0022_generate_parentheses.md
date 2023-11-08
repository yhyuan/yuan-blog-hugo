---
title: 22. generate parentheses
date: '2021-05-23'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0022 generate parentheses
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={22}/>
 

  Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

   

 >   Example 1:

 >   Input: n <TeX>=</TeX> 3

 >   Output: ["((()))","(()())","(())()","()(())","()()()"]

 >   Example 2:

 >   Input: n <TeX>=</TeX> 1

 >   Output: ["()"]

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 8


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        if n < 1 {
            return vec![];
        }
        let mut result = Vec::new();
        Solution::dfs(n, 0, 0, &mut result, String::new());
        result
    }

    fn dfs(n: i32, left: i32, right: i32, result: &mut Vec<String>, mut path: String) {
        println!("path: {}, left: {}, right: {}", path, left, right);
        if left == n && right == n {
            result.push(path);
            return;
        }
        if left < n {
            let mut new_path = path.clone();
            new_path.push('(');
            Solution::dfs(n, left + 1, right, result, new_path);
        }
        if right < left {
            // reuse path to avoid clone overhead
            path.push(')');
            Solution::dfs(n, left, right + 1, result, path);
        }
    }
    
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let n = n as usize;
        let mut results: Vec<Vec<String>> = vec![vec![]; n + 1];
        results[1] = vec!["()".to_string()];
        if n == 1 {
            //let result = vec!["()"];
            return results[1].clone();
        }
        //results[1].clone()
        
        for i in 2..=n {
            let mut result: Vec<String> = results[i - 1].iter().map(|str| format!("({})", str)).collect();
            for k in 1..i {
                let vector_1 = &results[k];
                let vector_2 = &results[i - k];
                let iter_1 = if vector_1.len() == 1 { 1 } else {vector_1.len() - 1};
                let iter_2 = if vector_2.len() == 1 { 1 } else {vector_2.len() - 1};
                for i1 in 0..iter_1 {
                    for i2 in 0..iter_2 {
                        let str = format!("{}{}", vector_1[i1], vector_2[i2]);
                        result.push(str);
                    }
                }
            }
            //let mut last_result = vec![format!("{}()", results[i - 1][results[i - 1].len() - 1])]; 
            result.push(format!("{}()", results[i - 1][results[i - 1].len() - 1]));
            results[i] = result;
        }
        results[n].clone()
        
    }
    
}
*/
use std::collections::HashSet;
impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let n = n as usize;
        let mut dp: Vec<HashSet<String>> = vec![HashSet::new(); n + 1];
        let mut hashset = HashSet::new();
        hashset.insert("()".to_string());
        dp[1] = hashset;
        for i in 2..=n {
            let mut res: HashSet<String> = HashSet::new();
            for k in 1..i {
                let pre_res = &dp[k];
                let post_res = &dp[i - k];
                for str1 in pre_res.iter() {
                    for str2 in post_res.iter() {
                        res.insert(format!("{}{}", str1, str2));
                    }
                }
            }
            let pre_res = &dp[i - 1];
            for str in pre_res.iter() {
                res.insert(format!("({})", str));
            }
            dp[i] = res;
        }
        let hashset = dp[n].clone();
        hashset.into_iter().collect::<Vec<String>>()
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_22() {
        assert_eq!(Solution::generate_parenthesis(1), vec_string!["()"]);
        
        assert_eq!(Solution::generate_parenthesis(2), vec_string!["(())", "()()"]);
        
        assert_eq!(
            Solution::generate_parenthesis(3).len(),
            vec_string!["((()))", "(()())", "(())()", "()(())", "()()()"].len()
        );

        assert_eq!(
            Solution::generate_parenthesis(4),
            vec_string!["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
        );

    }
}

```

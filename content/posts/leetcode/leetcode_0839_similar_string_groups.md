---
title: 839. similar string groups
date: '2022-05-25'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0839 similar string groups
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={839}/>
 

  Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

  For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

  Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

  We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?

   

 >   Example 1:

  

 >   Input: strs <TeX>=</TeX> ["tars","rats","arts","star"]

 >   Output: 2

  

 >   Example 2:

  

 >   Input: strs <TeX>=</TeX> ["omv","ovm"]

 >   Output: 1

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> strs.length <TeX>\leq</TeX> 300

 >   	1 <TeX>\leq</TeX> strs[i].length <TeX>\leq</TeX> 300

 >   	strs[i] consists of lowercase letters only.

 >   	All words in strs have the same length and are anagrams of each other.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::{HashMap, HashSet};
impl Solution {
    pub fn dfs(graph: &Vec<HashSet<usize>>, visited: &mut Vec<bool>, index: usize) {
        visited[index] = true;
        for &neighbor in graph[index].iter() {
            if !visited[neighbor] {
                Self::dfs(graph, visited, neighbor);
            }
        }
    }
    pub fn is_similar(s1: &String, s2: &String) -> bool {
        let chars1 = s1.chars().collect::<Vec<_>>();
        let chars2 = s2.chars().collect::<Vec<_>>();
        let n = chars2.len();
        let mut count = 0;
        for i in 0..n {
            if chars1[i] != chars2[i] {
                count += 1;
                if count >= 3 {
                    break;
                }
            }
        }
        count == 0 || count == 2        
    }
    pub fn num_similar_groups(strs: Vec<String>) -> i32 {
        let n = strs.len();
        let mut graph: Vec<HashSet<usize>> = vec![HashSet::new(); n];
        for i in 0..n {
            for j in i + 1..n {
                if Self::is_similar(&strs[i], &strs[j]) {
                    graph[i].insert(j);
                    graph[j].insert(i);
                }
            }
        }
        let mut visited: Vec<bool> = vec![false; n];
        let mut count = 0;
        for i in 0..n {
            if !visited[i] {
                Self::dfs(&graph, &mut visited, i);
                count += 1;
            }
        }
        count
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_839() {
        assert_eq!(Solution::num_similar_groups(vec_string!["tars","rats","arts","star"]), 2);
        assert_eq!(Solution::num_similar_groups(vec_string!["omv","ovm"]), 1);
        assert_eq!(Solution::num_similar_groups(vec_string!["abc","abc"]), 1);
    }
}

```

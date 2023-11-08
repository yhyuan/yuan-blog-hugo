---
title: 1202. smallest string with swaps
date: '2022-07-19'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 1202 smallest string with swaps
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1202}/>
 

  You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] <TeX>=</TeX> [a, b] indicates 2 indices(0-indexed) of the string.

  You can swap the characters at any pair of indices in the given pairs any number of times.

  Return the lexicographically smallest string that s can be changed to after using the swaps.

   

 >   Example 1:

  

 >   Input: s <TeX>=</TeX> "dcab", pairs <TeX>=</TeX> [[0,3],[1,2]]

 >   Output: "bacd"

 >   Explaination: 

 >   Swap s[0] and s[3], s <TeX>=</TeX> "bcad"

 >   Swap s[1] and s[2], s <TeX>=</TeX> "bacd"

  

 >   Example 2:

  

 >   Input: s <TeX>=</TeX> "dcab", pairs <TeX>=</TeX> [[0,3],[1,2],[0,2]]

 >   Output: "abcd"

 >   Explaination: 

 >   Swap s[0] and s[3], s <TeX>=</TeX> "bcad"

 >   Swap s[0] and s[2], s <TeX>=</TeX> "acbd"

 >   Swap s[1] and s[2], s <TeX>=</TeX> "abcd"

 >   Example 3:

  

 >   Input: s <TeX>=</TeX> "cba", pairs <TeX>=</TeX> [[0,1],[1,2]]

 >   Output: "abc"

 >   Explaination: 

 >   Swap s[0] and s[1], s <TeX>=</TeX> "bca"

 >   Swap s[1] and s[2], s <TeX>=</TeX> "bac"

 >   Swap s[0] and s[1], s <TeX>=</TeX> "abc"

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 10^5

 >   	0 <TeX>\leq</TeX> pairs.length <TeX>\leq</TeX> 10^5

 >   	0 <TeX>\leq</TeX> pairs[i][0], pairs[i][1] < s.length

 >   	s only contains lower case English letters.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
pub struct DisjointSet {
    parents: Vec<usize>,
    ranks: Vec<usize>
}
impl DisjointSet {
    pub fn new(n: usize) -> Self {
        let parents = (0..n).into_iter().collect::<Vec<_>>();
        let ranks = vec![1usize; n];
        DisjointSet {
            parents,
            ranks
        }
    }

    pub fn find(&self, i: usize) -> usize {
        let mut p = self.parents[i];
        while p != self.parents[p] {
            p = self.parents[p];
        }
        p
    }

    pub fn union(&mut self, i: usize, j: usize) -> bool {
        let ip = self.find(i);
        let jp = self.find(j);
        if ip == jp {
            return false;
        }
        if self.ranks[ip] < self.ranks[jp] {
            self.parents[ip] = self.parents[jp];
        } else if self.ranks[ip] > self.ranks[jp] {
            self.parents[jp] = self.parents[ip];
        } else {
            self.parents[jp] = self.parents[ip];
            self.ranks[ip] += 1;
        }
        true
    }
}
use std::collections::HashMap;
impl Solution {
    pub fn smallest_string_with_swaps(s: String, pairs: Vec<Vec<i32>>) -> String {
        let chars: Vec<char> = s.chars().collect();
        let mut disjoint_set = DisjointSet::new(s.len());
        for i in 0..pairs.len() {
            let start = pairs[i][0] as usize;
            let end = pairs[i][1] as usize;
            disjoint_set.union(start, end);
        }
        let mut hashmap: HashMap<usize, Vec<usize>> = HashMap::new();
        for i in 0..chars.len() {
            let p = disjoint_set.find(i);
            if hashmap.contains_key(&p) {
                let chars_vec = hashmap.get_mut(&p).unwrap();
                chars_vec.push(i);
            } else {
                hashmap.insert(p, vec![i]);
            }
        }
        let mut new_chars = vec![' '; chars.len()];
        for (key, val) in hashmap.iter() {
            let mut ches: Vec<char> = val.iter().map(|&i| chars[i]).collect();
            ches.sort();
            for (index, value) in val.iter().enumerate() {
                let ch = ches[index];
                new_chars[*value] = ch;
            }
        }
        let s = new_chars.iter().collect::<String>();
        // println!("{}", s);
        s
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1202() {
        assert_eq!(Solution::smallest_string_with_swaps("dcab".to_owned(), vec![vec![0,3],vec![1,2]]), "bacd".to_string());
        assert_eq!(Solution::smallest_string_with_swaps("dcab".to_owned(), vec![vec![0,3],vec![1,2],vec![0,2]]), "abcd".to_string());
    }
}

```

---
title: 990. satisfiability of equality equations
date: '2022-06-23'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0990 satisfiability of equality equations
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={990}/>
 

  You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi<TeX>=</TeX><TeX>=</TeX>yi" or "xi!<TeX>=</TeX>yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

  Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.

   

 >   Example 1:

  

 >   Input: equations <TeX>=</TeX> ["a<TeX>=</TeX><TeX>=</TeX>b","b!<TeX>=</TeX>a"]

 >   Output: false

 >   Explanation: If we assign say, a <TeX>=</TeX> 1 and b <TeX>=</TeX> 1, then the first equation is satisfied, but not the second.

 >   There is no way to assign the variables to satisfy both equations.

  

 >   Example 2:

  

 >   Input: equations <TeX>=</TeX> ["b<TeX>=</TeX><TeX>=</TeX>a","a<TeX>=</TeX><TeX>=</TeX>b"]

 >   Output: true

 >   Explanation: We could assign a <TeX>=</TeX> 1 and b <TeX>=</TeX> 1 to satisfy both equations.

  

 >   Example 3:

  

 >   Input: equations <TeX>=</TeX> ["a<TeX>=</TeX><TeX>=</TeX>b","b<TeX>=</TeX><TeX>=</TeX>c","a<TeX>=</TeX><TeX>=</TeX>c"]

 >   Output: true

  

 >   Example 4:

  

 >   Input: equations <TeX>=</TeX> ["a<TeX>=</TeX><TeX>=</TeX>b","b!<TeX>=</TeX>c","c<TeX>=</TeX><TeX>=</TeX>a"]

 >   Output: false

  

 >   Example 5:

  

 >   Input: equations <TeX>=</TeX> ["c<TeX>=</TeX><TeX>=</TeX>c","b<TeX>=</TeX><TeX>=</TeX>d","x!<TeX>=</TeX>z"]

 >   Output: true

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> equations.length <TeX>\leq</TeX> 500

 >   	equations[i].length <TeX>=</TeX><TeX>=</TeX> 4

 >   	equations[i][0] is a lowercase letter.

 >   	equations[i][1] is either '<TeX>=</TeX>' or '!'.

 >   	equations[i][2] is '<TeX>=</TeX>'.

 >   	equations[i][3] is a lowercase letter.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
pub struct DisjointSet {
    parents: Vec<usize>,
    ranks: Vec<usize>,
}

impl DisjointSet {
    pub fn new(n: usize) -> Self {
        let ranks = vec![1; n];
        let parents = (0..n).into_iter().collect::<Vec<_>>();
        DisjointSet {
            ranks,
            parents,
        }
    }

    pub fn find(&self, i: usize) -> usize {
        let mut parent = self.parents[i];
        while parent != self.parents[parent] {
            parent = self.parents[parent];
        }
        parent
    }

    pub fn union(&mut self, i: usize, j: usize) -> bool {
        let ip = self.find(i);
        let jp = self.find(j);
        if ip == jp {
            return false;
        }
        if self.ranks[ip] < self.ranks[jp] {
            self.parents[ip] = self.parents[jp];
        } else if self.parents[ip] > self.parents[jp] {
            self.parents[jp] = self.parents[ip];
        } else {
            self.parents[jp] = self.parents[ip];
            self.ranks[ip] += 1;
        }
        true
    }
}
use std::collections::{HashSet, HashMap};

impl Solution {
    pub fn equations_possible(equations: Vec<String>) -> bool {
        let mut hashset: HashSet<char> = HashSet::new();
        for i in 0..equations.len() {
            let char1 = equations[i].chars().nth(0).unwrap();
            let char2 = equations[i].chars().nth(3).unwrap();
            hashset.insert(char1);
            hashset.insert(char2);
        }
        let chars = hashset.into_iter().collect::<Vec<char>>();
        let mut hashmap: HashMap<char, usize> = HashMap::new();
        for i in 0..chars.len() {
            hashmap.insert(chars[i], i);
        }
        let mut disjoint_set = DisjointSet::new(chars.len());
        for i in 0..equations.len() {
            let char1 = equations[i].chars().nth(1).unwrap();
            let char2 = equations[i].chars().nth(2).unwrap();
            if char1 == '=' && char2 == '=' {
                let char0 = equations[i].chars().nth(0).unwrap();
                let char3 = equations[i].chars().nth(3).unwrap();    
                let k1 = hashmap.get(&char0).unwrap();
                let k2 = hashmap.get(&char3).unwrap();
                disjoint_set.union(*k1, *k2);
            }
        }
        for i in 0..equations.len() {
            let char1 = equations[i].chars().nth(1).unwrap();
            let char2 = equations[i].chars().nth(2).unwrap();
            if char1 == '!' && char2 == '=' {
                let char0 = equations[i].chars().nth(0).unwrap();
                let char3 = equations[i].chars().nth(3).unwrap();    
                let k1 = hashmap.get(&char0).unwrap();
                let k2 = hashmap.get(&char3).unwrap();
                if disjoint_set.find(*k1) == disjoint_set.find(*k2) {
                    return false;
                }
            }
        }
        true
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_990() {
        assert_eq!(Solution::equations_possible(vec_string!["a==b","b!=a"]), false);
        assert_eq!(Solution::equations_possible(vec_string!["b==a","a==b"]), true);
    }
}

```

---
title: 737. sentence similarity ii
date: '2022-05-04'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0737 sentence similarity ii
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={737}/>

We can represent a sentence as an array of words, for example, the sentence "I am happy with leetcode" can be represented as arr <TeX>=</TeX> ["I","am",happy","with","leetcode"].



Given two sentences sentence1 and sentence2 each represented as a string array and given an array of string pairs similarPairs where similarPairs[i] <TeX>=</TeX> [xi, yi] indicates that the two words xi and yi are similar.



Return true if sentence1 and sentence2 are similar, or false if they are not similar.



Two sentences are similar if:



They have the same length (i.e., the same number of words)

sentence1[i] and sentence2[i] are similar.

Notice that a word is always similar to itself, also notice that the similarity relation is transitive. For example, if the words a and b are similar, and the words b and c are similar, then a and c are similar.



 



 > Example 1:



 > Input: sentence1 <TeX>=</TeX> ["great","acting","skills"], sentence2 <TeX>=</TeX> ["fine","drama","talent"], similarPairs <TeX>=</TeX> [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]

 > Output: true

 > Explanation: The two sentences have the same length and each word i of sentence1 is also similar to the corresponding word in sentence2.

 > Example 2:



 > Input: sentence1 <TeX>=</TeX> ["I","love","leetcode"], sentence2 <TeX>=</TeX> ["I","love","onepiece"], similarPairs <TeX>=</TeX> [["manga","onepiece"],["platform","anime"],["leetcode","platform"],["anime","manga"]]

 > Output: true

 > Explanation: "leetcode" --> "platform" --> "anime" --> "manga" --> "onepiece".

 > Since "leetcode is similar to "onepiece" and the first two words are the same, the two sentences are similar.

 > Example 3:



 > Input: sentence1 <TeX>=</TeX> ["I","love","leetcode"], sentence2 <TeX>=</TeX> ["I","love","onepiece"], similarPairs <TeX>=</TeX> [["manga","hunterXhunter"],["platform","anime"],["leetcode","platform"],["anime","manga"]]

 > Output: false

 > Explanation: "leetcode" is not similar to "onepiece".

 



**Constraints:**



 > 1 <TeX>\leq</TeX> sentence1.length, sentence2.length <TeX>\leq</TeX> 1000

 > 1 <TeX>\leq</TeX> sentence1[i].length, sentence2[i].length <TeX>\leq</TeX> 20

 > sentence1[i] and sentence2[i] consist of lower-case and upper-case English letters.

 > 0 <TeX>\leq</TeX> similarPairs.length <TeX>\leq</TeX> 2000

 > similarPairs[i].length <TeX>=</TeX><TeX>=</TeX> 2

 > 1 <TeX>\leq</TeX> xi.length, yi.length <TeX>\leq</TeX> 20

 > xi and yi consist of English letters.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
pub struct DisjointSet {
    pub parents: Vec<usize>,
    pub ranks: Vec<usize>,
}

impl DisjointSet {
    pub fn new(n: usize) -> Self {
        let parents = (0..n).into_iter().collect::<Vec<_>>();
        let ranks: Vec<usize> = vec![1; n];
        DisjointSet {
            parents,
            ranks
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
            self.parents[ip] = jp;
        } else if self.ranks[ip] > self.ranks[jp] {
            self.parents[jp] = ip;
        } else {
            self.parents[jp] = ip;
            self.ranks[ip] += 1;
        }
        true
    }
}
use std::collections::{HashSet, HashMap};

impl Solution {
    pub fn are_sentences_similar_two(sentence1: Vec<String>, sentence2: Vec<String>, similar_pairs: Vec<Vec<String>>) -> bool {
        let mut hashmap : HashMap<String, usize> = HashMap::new();
        for i in 0..similar_pairs.len() {
            for j in 0..similar_pairs[i].len() {
                let s = &similar_pairs[i][j];
                if !hashmap.contains_key(s) {
                    let size = hashmap.len();
                    hashmap.insert(s.clone(), size);
                }
            }
        }        
        let mut disjoint_set = DisjointSet::new(hashmap.len());
        for i in 0..similar_pairs.len() {
            let start = similar_pairs[i][0].clone();
            let end = similar_pairs[i][1].clone();
            let k0 = hashmap.get(&start).unwrap();
            let k1 = hashmap.get(&end).unwrap();
            disjoint_set.union(*k1, *k0);
        }
        let n = sentence1.len();
        for i in 0..n {
            let k1 = hashmap.get(&sentence1[i]).unwrap();
            let k2 = hashmap.get(&sentence2[i]).unwrap();
            if disjoint_set.find(*k1) != disjoint_set.find(*k2) {
                return false;
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
    fn test_737() {
        assert_eq!(Solution::are_sentences_similar_two(
            vec_string!["great","acting","skills"], 
            vec_string!["fine","drama","talent"], 
            vec![vec_string!["great","good"],vec_string!["fine","good"],vec_string!["drama","acting"],vec_string!["skills","talent"]]
        ), true);
        assert_eq!(Solution::are_sentences_similar_two(
            vec_string!["I","love","leetcode"], 
            vec_string!["I","love","onepiece"], 
            vec![vec_string!["manga","onepiece"],vec_string!["platform","anime"],vec_string!["leetcode","platform"],vec_string!["anime","manga"]]
        ), true);
        assert_eq!(Solution::are_sentences_similar_two(
            vec_string!["I","love","leetcode"], 
            vec_string!["I","love","onepiece"], 
            vec![vec_string!["manga","hunterXhunter"],vec_string!["platform","anime"],vec_string!["leetcode","platform"],vec_string!["anime","manga"]]
        ), false);
    }
}

```

---
title: 642. design search autocomplete system
date: '2022-04-11'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0642 design search autocomplete system
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={642}/>

Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#').



You are given a string array sentences and an integer array times both of length n where sentences[i] is a previously typed sentence and times[i] is the corresponding number of times the sentence was typed. For each input character except '#', return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.



Here are the specific rules:



The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.

The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).

If less than 3 hot sentences exist, return as many as you can.

When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.

Implement the AutocompleteSystem class:



AutocompleteSystem(String[] sentences, int[] times) Initializes the object with the sentences and times arrays.

List input(char c) This indicates that the user typed the character c.

Returns an empty array [] if c <TeX>=</TeX><TeX>=</TeX> '#' and stores the inputted sentence in the system.

Returns the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed. If there are fewer than 3 matches, return them all.

 



 > Example 1:



 > Input

 > ["AutocompleteSystem", "input", "input", "input", "input"]

 > [[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]

 > Output

 > [null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]



 > Explanation

 > AutocompleteSystem obj <TeX>=</TeX> new AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]);

 > obj.input("i"); // return ["i love you", "island", "i love leetcode"]. There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.

 > obj.input(" "); // return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".

 > obj.input("a"); // return []. There are no sentences that have prefix "i a".

 > obj.input("#"); // return []. The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.

 



**Constraints:**



 > n <TeX>=</TeX><TeX>=</TeX> sentences.length

 > n <TeX>=</TeX><TeX>=</TeX> times.length

 > 1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 100

 > 1 <TeX>\leq</TeX> sentences[i].length <TeX>\leq</TeX> 100

 > 1 <TeX>\leq</TeX> times[i] <TeX>\leq</TeX> 50

 > c is a lowercase English letter, a hash '#', or space ' '.

 > Each tested sentence will be a sequence of characters c that end with the character '#'.

 > Each tested sentence will have a length in the range [1, 200].

 > The words in each input sentence are separated by single spaces.

 > At most 5000 calls will be made to input.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

use std::collections::HashMap;
use std::collections::HashSet;
use std::collections::BinaryHeap;
struct AutocompleteSystem {
    trie: Vec<HashMap<char, usize>>,
    end_nodes: HashSet<usize>,
    times_hashmap: HashMap<String, i32>, 
    current_node: usize,
    current_chars: Vec<char>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl AutocompleteSystem {

    fn new(sentences: Vec<String>, times: Vec<i32>) -> Self {
        let mut trie: Vec<HashMap<char, usize>> = vec![HashMap::new()];
        let mut end_nodes: HashSet<usize> = HashSet::new();
        let mut times_hashmap: HashMap<String, i32> = HashMap::new();
        let n = sentences.len();
        for i in 0..n {
            times_hashmap.insert(sentences[i].clone(), times[i]);
        }
        for i in 0..n {
            let mut curr = 0usize; // root
            for ch in sentences[i].chars() {
                if trie[curr].contains_key(&ch) {
                    curr = trie[curr][&ch];
                } else {
                    let trie_size = trie.len();
                    trie.push(HashMap::new());
                    trie[curr].insert(ch,  trie_size);
                    curr = trie.len() - 1;
                }
            }
            end_nodes.insert(curr);
        }
        let current_node = 0usize;
        //println!("trie: {:?}", trie);
        //println!("end_nodes: {:?}", end_nodes);
        //println!("times_hashmap: {:?}", times_hashmap);
        let current_chars: Vec<char> = vec![];
        Self {trie, end_nodes, times_hashmap, current_node, current_chars}
    }
    fn search_substrings(&self, node: usize) -> Vec<String> {
        let mut results: Vec<String> = vec![];
        if self.trie[node].len() == 0 {
            return vec!["".to_string()];
        }
        for (ch, node_id) in self.trie[node].iter() {
            let sub_results = self.search_substrings(*node_id);
            for i in 0..sub_results.len() {
                results.push(format!("{}{}", ch, sub_results[i]));
            }
        }
        if self.end_nodes.contains(&node) {
            results.push("".to_string());
        }
        results
    }
    fn input(&mut self, c: char) -> Vec<String> {
        println!("c: {}", c);
        if c == '#' {
            let current_string = self.current_chars.iter().collect::<String>();
            if self.times_hashmap.contains_key(&current_string) {
                *self.times_hashmap.get_mut(&current_string).unwrap() += 1;
            } else {
                self.times_hashmap.insert(current_string.clone(), 1);
                let mut curr = 0usize; // root
                for ch in current_string.chars() {
                    if self.trie[curr].contains_key(&ch) {
                        curr = self.trie[curr][&ch];
                    } else {
                        let trie_size = self.trie.len();
                        self.trie.push(HashMap::new());
                        self.trie[curr].insert(ch,  trie_size);
                        curr = self.trie.len() - 1;
                    }
                }
                self.end_nodes.insert(curr);    
            }
            self.current_node = 0;
            self.current_chars = vec![];
            return vec![];
        } else {
            self.current_chars.push(c);
            if !self.trie[self.current_node].contains_key(&c) {
                // self.current_chars.push(c);
                return vec![];
            }
            self.current_node = self.trie[self.current_node][&c];
            let substrings: Vec<String> = self.search_substrings(self.current_node);
            let current_string = self.current_chars.iter().collect::<String>();
            let mut min_heap: BinaryHeap<(i32, String)> = BinaryHeap::new();
            // let mut results: Vec<(i32, String)> = vec![];

            for i in 0..substrings.len() {
                let result = format!("{}{}", current_string, substrings[i]);
                let score = self.times_hashmap[&result];
                if min_heap.len() < 3 {
                    min_heap.push((-score, result));
                } else {
                    if -score <= min_heap.peek().unwrap().0 {
                        min_heap.push((-score, result));
                        min_heap.pop();
                    } 
                }
                //results.push((-score, result));
            }
            //results.sort();
            //let results_size = usize::min(3, results.len());
            let mut ans: Vec<String> = vec![];
            /*
            for i in 0..results_size {
                ans.push(results[i].1.clone());
            }
            */
            while !min_heap.is_empty() {
                let (_, result) = min_heap.pop().unwrap();
                ans.push(result);
            }
            ans.reverse();
            return ans;
        }
        unreachable!()
    }
}

/**
 * Your AutocompleteSystem object will be instantiated and called as such:
 * let obj = AutocompleteSystem::new(sentences, times);
 * let ret_1: Vec<String> = obj.input(c);
 */

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_642() {
        let mut obj = AutocompleteSystem::new(vec_string!["i love you", "island", "iroman", "i love leetcode"], vec![5, 3, 2, 2]);
        assert_eq!(obj.input('i'), vec_string!["i love you", "island", "i love leetcode"]); // return ["i love you", "island", "i love leetcode"]. There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
        assert_eq!(obj.input(' '), vec_string!["i love you", "i love leetcode"]); // return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
        assert_eq!(obj.input('a').len(), 0); // return []. There are no sentences that have prefix "i a".
        assert_eq!(obj.input('#').len(), 0); // return []. The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search

        assert_eq!(obj.input('i'), vec_string!["i love you", "island", "i love leetcode"]); // return ["i love you", "island", "i love leetcode"]. There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
        assert_eq!(obj.input(' '), vec_string!["i love you", "i love leetcode"]); // return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
        assert_eq!(obj.input('a').len(), 0); // return []. There are no sentences that have prefix "i a".
        assert_eq!(obj.input('#').len(), 0); // return []. The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search

        assert_eq!(obj.input('i'), vec_string!["i love you", "island", "i love leetcode"]); // return ["i love you", "island", "i love leetcode"]. There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
        assert_eq!(obj.input(' '), vec_string!["i love you", "i love leetcode"]); // return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
        assert_eq!(obj.input('a').len(), 0); // return []. There are no sentences that have prefix "i a".
        assert_eq!(obj.input('#').len(), 0); // return []. The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search

    }
}

```

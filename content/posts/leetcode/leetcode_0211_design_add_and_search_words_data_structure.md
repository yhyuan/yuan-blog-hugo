---
title: 211. design add and search words data structure
date: '2021-10-28'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0211 design add and search words data structure
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={211}/>
 

  Design a data structure that supports adding new words and finding if a string matches any previously added string.

  Implement the WordDictionary class:

  

  	WordDictionary() Initializes the object.

  	void addWord(word) Adds word to the data structure, it can be matched later.

  	bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

  

   

  Example:

  

  Input

  ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]

  [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

  Output

  [null,null,null,null,false,true,true,true]

  Explanation

  WordDictionary wordDictionary <TeX>=</TeX> new WordDictionary();

  wordDictionary.addWord("bad");

  wordDictionary.addWord("dad");

  wordDictionary.addWord("mad");

  wordDictionary.search("pad"); // return False

  wordDictionary.search("bad"); // return True

  wordDictionary.search(".ad"); // return True

  wordDictionary.search("b.."); // return True

  

   

  **Constraints:**

  

  	1 <TeX>\leq</TeX> word.length <TeX>\leq</TeX> 500

  	word in addWord consists lower-case English letters.

  	word in search consist of  '.' or lower-case English letters.

  	At most 50000 calls will be made to addWord and search.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashSet;
struct WordDictionary {
    set: HashSet<String>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl WordDictionary {

    /** Initialize your data structure here. */
    fn new() -> Self {
        let set: HashSet<String> = HashSet::new();
        Self {set}
    }
    
    fn add_word(&mut self, word: String) {
        self.set.insert(word);        
    }
    
    fn search(&self, word: String) -> bool {
        let n = word.len();
        let chars: Vec<char> = word.chars().collect();
        let dot_count = (0..word.len()).into_iter().filter(|&i| chars[i] == '.').count();
        if dot_count == 0 {
            return self.set.contains(&word);
        }
        if dot_count == n {
            for word in self.set.iter() {
                if word.len() == n {
                    return true;
                }
            }
            return false;
        }
        for test_word in self.set.iter() {
            if test_word.len() == n {
                let word_chars: Vec<char> = test_word.chars().collect();
                //println!("test_word: {}, word: {}", test_word, word);
                let mut is_matched = true;
                for i in 0..n {
                    if chars[i] != '.' && word_chars[i] != chars[i] {
                        is_matched = false;
                        break;
                    }
                }
                if is_matched {
                    return true;
                }
            }
        }
        false
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * let obj = WordDictionary::new();
 * obj.add_word(word);
 * let ret_2: bool = obj.search(word);
 */

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_211() {
        
        let mut dict = WordDictionary::new();
        dict.add_word("bad".to_owned());
        dict.add_word("dad".to_owned());
        dict.add_word("mad".to_owned());
        assert_eq!(dict.search("pad".to_owned()), false);
        assert_eq!(dict.search("bad".to_owned()), true);
        assert_eq!(dict.search(".ad".to_owned()), true);
        assert_eq!(dict.search("da.".to_owned()), true);
        
        let mut dict = WordDictionary::new();
        dict.add_word("a".to_owned());
        assert_eq!(dict.search(".".to_owned()), true);
        
    }
}

```

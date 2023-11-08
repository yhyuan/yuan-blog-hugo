---
title: 208. implement trie prefix tree
date: '2021-10-25'
tags: ['leetcode', 'rust', 'python', 'medium']
draft: false
description: Solution for leetcode 0208 implement trie prefix tree
---

 

  A [trie](https://en.wikipedia.org/wiki/Trie) (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

  Implement the Trie class:

  

  	Trie() Initializes the trie object.

  	void insert(String word) Inserts the string word into the trie.

  	boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.

  	boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

  

   

 >   Example 1:

  

 >   Input

 >   ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]

 >   [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

 >   Output

 >   [null, null, true, false, true, null, true]

 >   Explanation

 >   Trie trie <TeX>=</TeX> new Trie();

 >   trie.insert("apple");

 >   trie.search("apple");   // return True

 >   trie.search("app");     // return False

 >   trie.startsWith("app"); // return True

 >   trie.insert("app");

 >   trie.search("app");     // return True

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> word.length, prefix.length <TeX>\leq</TeX> 2000

 >   	word and prefix consist only of lowercase English letters.

 >   	At most 3  10^4 calls in total will be made to insert, search, and startsWith.


## Solution
### Python
```python
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.isEnd = False
        self.count = 0
        self.children = {}
        
class Trie:

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            if word[i] in node.children:
                node = node.children[word[i]]
            else:
                new_node = TrieNode(word[i])
                node.children[word[i]] = new_node
                node = new_node
        node.isEnd = True
        node.count += 1
        return

    def search(self, word: str) -> bool:
        node = self.root 
        for i in range(len(word)):
            if word[i] in node.children:
                node = node.children[word[i]]
            else:
                return False
        
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            if prefix[i] in node.children:
                node = node.children[prefix[i]]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```
### Rust
```rust
pub struct Solution {}


// submission codes start here
/* 
#[derive(Default)]
struct Trie {
    is_end: bool,
    nodes: [Option<Box<Trie>>; 26],
}

impl Trie {

    fn new() -> Self {
        Default::default()
    }
    
    fn insert(&mut self, word: String) {
        let mut curr = self;
        for i in word.chars().map(|ch| (ch as u8 - 'a' as u8) as usize) {
            curr = curr.nodes[i].get_or_insert_with(|| Box::new(Trie::new())); // Option get_or_insert_with
        }
        curr.is_end = true;
    }
    
    fn search(&self, word: String) -> bool {
        self.find(word).map_or(false, |t| t.is_end)
    }
    
    fn starts_with(&self, prefix: String) -> bool {
        self.find(prefix).is_some()
    }

    fn find(&self, word: String) -> Option<&Trie> {
        let mut curr = self;
        for i in word.chars().map(|ch| (ch as u8 - 'a' as u8) as usize) {
            curr = curr.nodes[i].as_ref()?;
        }
        Some(curr)
    }
}
*/
use std::collections::HashMap;
#[derive(PartialEq, Eq, Clone, Debug, Default)]
struct Trie {
    children: HashMap<char, Trie>,
    end: bool,
}

impl Trie {

    fn new() -> Self {
        Self::default()
    }
    
    fn insert(&mut self, word: String) {
        let mut curr = self;
        for c in word.chars() {
            curr = curr.children.entry(c).or_default();
        }
        curr.end = true;
    }
    
    fn search(&self, word: String) -> bool {
        let mut curr = self;
        for c in word.chars() {
            if let Some(child) = curr.children.get(&c) {
                curr = child;
            } else {
                return false;
            }
        }
        curr.end
    }
    
    fn starts_with(&self, prefix: String) -> bool {
        let mut curr = self;
        for c in prefix.chars() {
            if let Some(child) = curr.children.get(&c) {
                curr = child;
            } else {
                return false;
            }
        }
        true
    }
}
/**
 * Your Trie object will be instantiated and called as such:
 * let obj = Trie::new();
 * obj.insert(word);
 * let ret_2: bool = obj.search(word);
 * let ret_3: bool = obj.starts_with(prefix);
 */

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_208() {
        let mut trie = Trie::new();
        trie.insert("apple".to_owned());
        assert_eq!(trie.search("apple".to_owned()), true); // returns true
        assert_eq!(trie.search("app".to_owned()), false);
        assert_eq!(trie.starts_with("app".to_owned()), true); // returns true
        trie.insert("app".to_owned());
        assert_eq!(trie.search("app".to_owned()), true); // returns true
    }
}

```

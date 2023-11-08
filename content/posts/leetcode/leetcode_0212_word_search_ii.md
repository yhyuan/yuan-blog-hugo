---
title: 212. word search ii
date: '2021-10-29'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0212 word search ii
---

 

  Given an m x n board of characters and a list of strings words, return all words on the board.

  Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/11/07/search1.jpg)

 >   Input: board <TeX>=</TeX> [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words <TeX>=</TeX> ["oath","pea","eat","rain"]

 >   Output: ["eat","oath"]

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2020/11/07/search2.jpg)

 >   Input: board <TeX>=</TeX> [["a","b"],["c","d"]], words <TeX>=</TeX> ["abcb"]

 >   Output: []

  

   

  **Constraints:**

  

 >   	m <TeX>==</TeX> board.length

 >   	n <TeX>==</TeX> board[i].length

 >   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 12

 >   	board[i][j] is a lowercase English letter.

 >   	1 <TeX>\leq</TeX> words.length <TeX>\leq</TeX> 3  10^4

 >   	1 <TeX>\leq</TeX> words[i].length <TeX>\leq</TeX> 10

 >   	words[i] consists of lowercase English letters.

 >   	All the strings of words are unique.


## Solution
The first solution is to use each word and DFS to search to grid. It will trigger time out. The better solution is to build a trie tree firstly. Then, search each position in the grid as the starting points by using the trie tree. If a word is found, it is added to the result. Since the m, n <TeX>\leq</TeX> 12. So it is faster to do it. 
### Python
```python
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.isEnd = False
        self.count = 0
        self.word = ""
        self.children = {}
class Trie:
    def __init__(self):
        self.root = TrieNode("")
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                newNode = TrieNode(ch)
                node.children[ch] = newNode
                node = newNode
        node.isEnd = True
        node.word = word
        node.count += 1
        return 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        n = len(words)
        for i in range(n):
            trie.insert(words[i])
        m = len(board)
        n = len(board[0])
        ans = set([])
        def dfs(i, j, node):
            c = board[i][j]
            if c in node.children:
                nextNode = node.children[c]
                board[i][j] = " "
                if nextNode.isEnd:
                    ans.add(nextNode.word)
                diffs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for diff in diffs:
                    n_i = i + diff[0]
                    n_j = j + diff[1]
                    if n_i >= 0 and n_j >= 0 and n_i < m and n_j < n and board[n_i][n_j] != " ":
                        dfs(n_i, n_j, nextNode)
                board[i][j] = c
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.root)
        return list(ans)
```
### Rust
```rust
pub struct Solution {}


// submission codes start here

use std::collections::HashMap;
#[derive(Default)]
pub struct Trie {
    children: HashMap<char, Trie>,
    end: Option<String>,
}

impl Trie {
/*
    fn new() -> Self {
        Self::default()
    }
*/    
    fn insert(&mut self, word: String) {
        let mut curr = self;
        for c in word.chars() {
            curr = curr.children.entry(c).or_default();
        }
        curr.end = Some(word);
    }
    /*
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
    */
}

/*
impl Solution {
    pub fn find_word_helper(board: &Vec<Vec<char>>, chars: &Vec<char>, index: usize, position: (usize, usize), marked: &mut Vec<Vec<bool>>) -> bool {
        let m = board.len() as i32;
        let n = board[0].len() as i32;
        if chars.len() == index {
            return true;
        }
        let options: Vec<(usize, usize)> = [(1, 0), (-1, 0), (0, 1), (0, -1)].into_iter()
            .map(|&delta| (delta.0 + position.0 as i32, delta.1 + position.1 as i32))
            .filter(|&coor| coor.0 >= 0 && coor.0 < m && coor.1 >= 0 && coor.1 < n)
            .map(|coor| (coor.0 as usize, coor.1 as usize))
            .filter(|coor| board[coor.0][coor.1] == chars[index] && !marked[coor.0][coor.1])
            .collect();
        for &option in options.iter() {
            marked[option.0][option.1] = true;
            if Solution::find_word_helper(board, chars, index + 1, option, marked) {
                return true;
            }
            marked[option.0][option.1] = false;
        }
        false
    }
    pub fn find_word(board: &Vec<Vec<char>>, chars: &Vec<char>) -> bool {
        let m = board.len();
        let n = board[0].len();
        let ch = chars[0];
        let mut start_positions: Vec<(usize, usize)> = vec![];
        for i in 0..m {
            for j in 0..n {
                if board[i][j] == ch {
                    start_positions.push((i, j));
                }
            }
        }
        if start_positions.len() == 0 {
            return false;
        }
        for &position in start_positions.iter() {
            let mut marked: Vec<Vec<bool>> = vec![vec![false; n]; m];
            marked[position.0][position.1] = true;
            if Solution::find_word_helper(board, chars, 1, position, &mut marked) {
                return true;
            }
        }
        false
    }
    pub fn find_words(board: Vec<Vec<char>>, words: Vec<String>) -> Vec<String> {
        let mut results: Vec<String> = vec![];
        for word in words {
            let chars: Vec<char> = word.chars().collect();
            if Self::find_word(&board, &chars) {
                results.push(word);
            }
        }
        results
    }
}
*/
impl Solution {
    pub fn find_words(board: Vec<Vec<char>>, words: Vec<String>) -> Vec<String> {
        let mut board = board;
        let mut trie = Trie::default();
        for word in words {
            trie.insert(word);
        }
        let m = board.len();
        let n = board[0].len();
        let mut res: Vec<String> = vec![];
        for i in 0..m {
            for j in 0..n {
                //start from [i][j]
                Self::dfs(i, j, &mut board, &mut res, &mut trie, m, n);
            }
        }
        res
    }
    pub fn dfs(i: usize, j: usize, board: &mut Vec<Vec<char>>, all: &mut Vec<String>, trie: &mut Trie, m: usize, n: usize) {
        let c = board[i][j];
        if let Some(trie) = trie.children.get_mut(&c) {
            board[i][j] = ' ';
            if trie.end.is_some() {
                all.push(trie.end.take().unwrap());
            }
            if i + 1 < m {
                Self::dfs(i + 1, j, board, all, trie, m, n);
            }
            if j + 1 < n {
                Self::dfs(i, j + 1, board, all, trie, m, n);
            }
            if i > 0 {
                Self::dfs(i - 1, j, board, all, trie, m, n);
            }
            if j > 0 {
                Self::dfs(i, j - 1, board, all, trie, m, n);
            }
            board[i][j] = c;
        }
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_212() {
        assert_eq!(Solution::find_words(
            vec![vec!['o','a','a','n'],vec!['e','t','a','e'],vec!['i','h','k','r'],vec!['i','f','l','v']],
            vec!["oath".to_string(),"pea".to_string(),"eat".to_string(),"rain".to_string()]),
            vec!["oath".to_string(), "eat".to_string()]);
        let empty: Vec<String> = vec![];
        assert_eq!(Solution::find_words(
            vec![vec!['a','b'],vec!['c','d']],
            vec!["abcd".to_string()]),
            empty);    
    }
}

```

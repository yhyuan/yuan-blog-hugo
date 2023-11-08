---
title: 1268. Search Suggestions System
date: '2022-07-26'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 1268. Search Suggestions System
---


You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

 >  Example 1:

 >  Input: products <TeX>=</TeX> ["mobile","mouse","moneypot","monitor","mousepad"], searchWord <TeX>=</TeX> "mouse"
 >  Output: [
 >  ["mobile","moneypot","monitor"],
 >  ["mobile","moneypot","monitor"],
 >  ["mouse","mousepad"],
 >  ["mouse","mousepad"],
 >  ["mouse","mousepad"]
 >  ]
 >  Explanation: products sorted lexicographically <TeX>=</TeX> ["mobile","moneypot","monitor","mouse","mousepad"]
 >  After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
 >  After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

 >  Example 2:

 >  Input: products <TeX>=</TeX> ["havana"], searchWord <TeX>=</TeX> "havana"
 >  Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

 >  Example 3:

 >  Input: products <TeX>=</TeX> ["bags","baggage","banner","box","cloths"], searchWord <TeX>=</TeX> "bags"
 >  Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

**Constraints:**

 >  1 <TeX>\leq</TeX> products.length <TeX>\leq</TeX> 1000

 >  1 <TeX>\leq</TeX> products[i].length <TeX>\leq</TeX> 3000

 >  1 <TeX>\leq</TeX> sum(products[i].length) <TeX>\leq</TeX> 2 * 104

 >  All the strings of products are unique.

 >  products[i] consists of lowercase English letters.

 >  1 <TeX>\leq</TeX> searchWord.length <TeX>\leq</TeX> 1000

 >  searchWord consists of lowercase English letters.


## Solution
We will use Trie to solve this problem. 
### Python
```python
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.isEnd = False
        self.count = 0
        self.children = {}
        
class Trie(object):
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                new_node = TrieNode(ch)
                node.children[ch] = new_node
                node = new_node
        node.isEnd = True
        node.count += 1

    def dfs(self, node, prefix):
        if node.isEnd:
            self.output.append((prefix + node.char, node.count))
        for ch in node.children:
            self.dfs(node.children[ch], prefix + node.char)
        
    def query(self, prefix):
        self.output = []
        node = self.root
        for ch in prefix:
            if ch in node.children:
                node = node.children[ch]
            else:
                return []
        # remove last ch because node contains it.
        self.dfs(node, prefix[:-1])
        return self.output
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        n = len(products)
        trie = Trie()
        words = set(products)
        for i in range(n):
            trie.insert(products[i])
        ans = []
        for i in range(len(searchWord)):
            res = trie.query(searchWord[:i + 1])
            res = list(map(lambda r: r[0], res))
            res.sort()
            if len(res) > 3:
                res = res[:3]
            ans = ans + [res]
        return ans
```

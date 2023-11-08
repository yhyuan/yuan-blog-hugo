---
title: 297. serialize and deserialize binary tree
date: '2021-12-24'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0297 serialize and deserialize binary tree
---

 

  Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

  Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

  Clarification: The input/output format is the same as [how LeetCode serializes a binary tree](/faq/#binary-tree). You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg)

 >   Input: root <TeX>=</TeX> [1,2,3,null,null,4,5]

 >   Output: [1,2,3,null,null,4,5]

  

 >   Example 2:

  

 >   Input: root <TeX>=</TeX> []

 >   Output: []

  

 >   Example 3:

  

 >   Input: root <TeX>=</TeX> [1]

 >   Output: [1]

  

 >   Example 4:

  

 >   Input: root <TeX>=</TeX> [1,2]

 >   Output: [1,2]

  

   

  **Constraints:**

  

 >   	The number of nodes in the tree is in the range [0, 10^4].

 >   	-1000 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 1000


## Solution
### Rust
```rust
pub struct Solution {}
use crate::util::tree::{TreeNode, to_tree};


// submission codes start here

// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
use std::iter::Peekable;
use std::vec::IntoIter;
struct Codec;
enum Tok {
    Op(char),
    Num(i32),
}
/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Codec {
    fn new() -> Self {
        Codec {}
    }

    fn serialize(&self, root: Option<Rc<RefCell<TreeNode>>>) -> String {
        let mut res = "".to_string();
        Self::serialize_tree(&root, &mut res);
        res
    }
	fn serialize_tree(root: &Option<Rc<RefCell<TreeNode>>>, s: &mut String) {
        s.push('(');
        if let Some(node) = root {
            let node = node.borrow();
            *s += &format!("{}", node.val);
            Self::serialize_tree(&node.left, s);
            Self::serialize_tree(&node.right, s);
        }
        s.push(')');
    }
    fn deserialize(&self, data: String) -> Option<Rc<RefCell<TreeNode>>> {
        let tokens = Self::parse_tokens(data);
        let mut it = tokens.into_iter().peekable();
        Self::parse_tree(&mut it)
    }
    fn parse_tokens(data: String) -> Vec<Tok> {
        let mut it = data.chars().peekable();
        let mut res: Vec<Tok> = vec![];
        while let Some(c) = it.next() {
            if c == '(' || c == ')' {
                res.push(Tok::Op(c));
            } else {
                let mut sign = 1;
                let mut x = 0;
                if c == '-' {
                    sign = -1;
                } else {
                    x = (c as u8 - b'0') as i32;
                }
                while let Some('0'..='9') = it.peek() {
                    x *= 10;
                    x += (it.next().unwrap() as u8 - b'0') as i32;
                }
                res.push(Tok::Num(sign * x));
            }
        }
        res
    }
    fn parse_tree(it: &mut Peekable<IntoIter<Tok>>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut res: Option<Rc<RefCell<TreeNode>>> = None;
        it.next();
        match it.peek() {
            Some(&Tok::Num(x)) => {
                it.next();
                res = Some(Rc::new(RefCell::new(TreeNode{val: x, left: Self::parse_tree(it), right: Self::parse_tree(it)})));
                //res = tree!(x, Self::parse_tree(it), Self::parse_tree(it))
            },
            Some(Tok::Op(')')) => {},
            _ => panic!(),
        }
        it.next();
        res
    }
}

/**
 * Your Codec object will be instantiated and called as such:
 * let obj = Codec::new();
 * let data: String = obj.serialize(strs);
 * let ans: Option<Rc<RefCell<TreeNode>>> = obj.deserialize(data);
 */

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_297() {
        let obj = Codec::new();
        let data: String = obj.serialize(tree![1,2,3,null,null,4,5]);
        assert_eq!(data, "(1(2()())(3(4()())(5()())))".to_string());
        let ans: Option<Rc<RefCell<TreeNode>>> = obj.deserialize(data);
        assert_eq!(ans, tree![1,2,3,null,null,4,5])
    }
}

```

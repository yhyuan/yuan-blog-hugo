---
title: 257. binary tree paths
date: '2021-12-01'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0257 binary tree paths
---

 

  Given the root of a binary tree, return all root-to-leaf paths in any order.

  A leaf is a node with no children.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/03/12/paths-tree.jpg)

 >   Input: root <TeX>=</TeX> [1,2,3,null,5]

 >   Output: ["1->2->5","1->3"]

  

 >   Example 2:

  

 >   Input: root <TeX>=</TeX> [1]

 >   Output: ["1"]

  

   

  **Constraints:**

  

 >   	The number of nodes in the tree is in the range [1, 100].

 >   	-100 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 100


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
use std::cell::{RefCell, Ref};
type TreeLink = Option<Rc<RefCell<TreeNode>>>;
trait Inorder {
    fn inorder(&self, visit: &mut dyn FnMut(i32, &Vec<i32>), path: &mut Vec<i32>);
}
impl Inorder for TreeLink {
    fn inorder(&self, visit: &mut dyn FnMut(i32, &Vec<i32>), path: &mut Vec<i32>) {
        if let Some(node) = self {
            let node: Ref<TreeNode> = node.borrow();
            path.push(node.val);
            if node.left.is_none() && node.right.is_none() {
                visit(node.val, path);
            }
            node.left.inorder(visit, path);
            node.right.inorder(visit, path);
            path.pop();
        }    
    }
}
impl Solution {
    pub fn binary_tree_paths(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<String> {
        let mut results: Vec<String> = Vec::new();
        let mut path: Vec<i32> = vec![];
        root.inorder(&mut |x, path| {
            let path_string: String = path.iter().map(|val| format!("{}", val)).collect::<Vec<String>>().join("->");
            results.push(path_string);
        }, &mut path);
        results
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_257() {
        assert_eq!(Solution::binary_tree_paths(tree![1,2,3,null,5]), vec!["1->2->5".to_string(),"1->3".to_string()]);
    }
}

```

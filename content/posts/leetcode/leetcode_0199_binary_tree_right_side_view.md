---
title: 199. binary tree right side view
date: '2021-10-16'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0199 binary tree right side view
---

 

  Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/02/14/tree.jpg)

 >   Input: root <TeX>=</TeX> [1,2,3,null,5,null,4]

 >   Output: [1,3,4]

  

 >   Example 2:

  

 >   Input: root <TeX>=</TeX> [1,null,3]

 >   Output: [1,3]

  

 >   Example 3:

  

 >   Input: root <TeX>=</TeX> []

 >   Output: []

  

   

  **Constraints:**

  

 >   	The number of nodes in the tree is in the range [0, 100].

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
    fn inorder(&self, visit: &mut dyn FnMut(i32, usize), layer: usize);
}
impl Inorder for TreeLink {
    fn inorder(&self, visit: &mut dyn FnMut(i32, usize), layer: usize) {
        if let Some(node) = self {
            let node: Ref<TreeNode> = node.borrow();
            node.left.inorder(visit, layer + 1);
            visit(node.val, layer);
            node.right.inorder(visit, layer + 1);
        }    
    }
}
impl Solution {
    pub fn right_side_view(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut res:Vec<Vec<i32>> = vec![];
        root.inorder(&mut |x, layer| {
            if res.len() < layer + 1 {
                for i in res.len()..layer + 1 {
                    res.push(vec![]);
                }
            }
            res[layer].push(x);
        }, 0);
        res.into_iter().map(|nums| nums[nums.len() - 1]).collect()
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_199() {
        assert_eq!(Solution::right_side_view(tree![1,2,3,null,5,null,4]), vec![1,3,4]);
        assert_eq!(Solution::right_side_view(tree![1,null,3]), vec![1,3]);
        //assert_eq!(Solution::right_side_view(tree![]), );
    }
}

```

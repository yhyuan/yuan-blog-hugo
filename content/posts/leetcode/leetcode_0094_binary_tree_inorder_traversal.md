---
title: 94. binary tree inorder traversal
date: '2021-08-03'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0094 binary tree inorder traversal
---

 

  Given the root of a binary tree, return the inorder traversal of its nodes' values.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)

 >   Input: root <TeX>=</TeX> [1,null,2,3]

 >   Output: [1,3,2]

  

 >   Example 2:

  

 >   Input: root <TeX>=</TeX> []

 >   Output: []

  

 >   Example 3:

  

 >   Input: root <TeX>=</TeX> [1]

 >   Output: [1]

  

 >   Example 4:

 >   ![](https://assets.leetcode.com/uploads/2020/09/15/inorder_5.jpg)

 >   Input: root <TeX>=</TeX> [1,2]

 >   Output: [2,1]

  

 >   Example 5:

 >   ![](https://assets.leetcode.com/uploads/2020/09/15/inorder_4.jpg)

 >   Input: root <TeX>=</TeX> [1,null,2]

 >   Output: [1,2]

  

   

  **Constraints:**

  

 >   	The number of nodes in the tree is in the range [0, 100].

 >   	-100 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 100

  

   

 >   Follow up: Recursive solution is trivial, could you do it iteratively?


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
    fn inorder(&self, visit: &mut dyn FnMut(i32));
}
impl Inorder for TreeLink {
    fn inorder(&self, visit: &mut dyn FnMut(i32)) {
        if let Some(node) = self {
            let node: Ref<TreeNode> = node.borrow();
            //Self::inorder(&node.left, visit);
            node.left.inorder(visit);
            visit(node.val);
            //Self::inorder(&node.right, visit);
            node.right.inorder(visit);
        }    
    }
}
impl Solution {
    pub fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut res = Vec::new();
        root.inorder(&mut |x| {
            res.push(x);
        });
        res
    }
}
/*
impl Solution {
    fn inorder_traversal_helper<F: FnMut(i32)>(root: Option<&Rc<RefCell<TreeNode>>>, consumer: &mut F) {
        if let Some(node) = root {
            Solution::inorder_traversal_helper(node.borrow().left.as_ref(), consumer);
            //consumer(root.as_ref().unwrap().borrow().val);
            consumer(node.borrow().val);
            Solution::inorder_traversal_helper(node.borrow().right.as_ref(), consumer);
        }
    }
    pub fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut res = Vec::new();
        Solution::inorder_traversal_helper(root.as_ref(), &mut (|v| res.push(v)));
        res
    }
}
*/
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_94() {
        assert_eq!(
            Solution::inorder_traversal(tree![1, null, 2, 3]),
            vec![1, 3, 2]
        );
        assert_eq!(
            Solution::inorder_traversal(tree![1, 2, 3, 4, 5, 6, 7]),
            vec![4, 2, 5, 1, 6, 3, 7]
        );
    }
}

```

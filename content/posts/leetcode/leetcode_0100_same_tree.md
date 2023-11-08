---
title: 100. same tree
date: '2021-08-09'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0100 same tree
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={100}/>
 

  Given the roots of two binary trees p and q, write a function to check if they are the same or not.

  Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)

 >   Input: p <TeX>=</TeX> [1,2,3], q <TeX>=</TeX> [1,2,3]

 >   Output: true

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)

 >   Input: p <TeX>=</TeX> [1,2], q <TeX>=</TeX> [1,null,2]

 >   Output: false

  

 >   Example 3:

 >   ![](https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg)

 >   Input: p <TeX>=</TeX> [1,2,1], q <TeX>=</TeX> [1,1,2]

 >   Output: false

  

   

  **Constraints:**

  

 >   	The number of nodes in both trees is in the range [0, 100].

 >   	-10^4 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 10^4


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
impl Solution {
    /*
    pub fn is_same_tree(p: Option<Rc<RefCell<TreeNode>>>, q: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let mut stack: Vec<(Option<Rc<RefCell<TreeNode>>>, Option<Rc<RefCell<TreeNode>>>)> = vec![];
        stack.push((p, q));
        while !stack.is_empty() {
            let pair:(Option<Rc<RefCell<TreeNode>>>, Option<Rc<RefCell<TreeNode>>>) = stack.pop().unwrap();
            match pair {
                (Some(p), Some(q)) if p == q => {
                    let p = p.borrow();
                    let q = q.borrow();
                    stack.push((p.left.clone(), q.left.clone()));
                    stack.push((p.right.clone(), q.right.clone()));
                }
                (None, None) => {}
                _ => {
                    return false;
                }
            }
        }
        true
    }
    */
    pub fn is_same_tree(p: Option<Rc<RefCell<TreeNode>>>, q: Option<Rc<RefCell<TreeNode>>>) -> bool {
        fn helper(p: &Option<Rc<RefCell<TreeNode>>>, q: &Option<Rc<RefCell<TreeNode>>>) -> bool {
            match (p, q) {
                (Some(p), Some(q)) if p == q => {
                    let p = p.borrow();
                    let q = q.borrow();

                    helper(&p.left, &q.left) && helper(&p.right, &q.right)
                },
                (None, None) => true,
                _ => false
            }
        }

        helper(&p, &q)
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_100() {
        assert_eq!(
            Solution::is_same_tree(tree![1, 2, 3, 4, null, 5], tree![1, 2, 3, 4, null, 5]),
            true
        )
    }
}

```

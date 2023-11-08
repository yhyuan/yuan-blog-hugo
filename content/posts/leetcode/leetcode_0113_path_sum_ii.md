---
title: 113. path sum ii
date: '2021-08-22'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0113 path sum ii
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={113}/>
 

  Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

  A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg)

 >   Input: root <TeX>=</TeX> [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum <TeX>=</TeX> 22

 >   Output: [[5,4,11,2],[5,8,4,5]]

 >   Explanation: There are two paths whose sum equals targetSum:

 >   5 + 4 + 11 + 2 <TeX>=</TeX> 22

 >   5 + 8 + 4 + 5 <TeX>=</TeX> 22

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg)

 >   Input: root <TeX>=</TeX> [1,2,3], targetSum <TeX>=</TeX> 5

 >   Output: []

  

 >   Example 3:

  

 >   Input: root <TeX>=</TeX> [1,2], targetSum <TeX>=</TeX> 0

 >   Output: []

  

   

  **Constraints:**

  

 >   	The number of nodes in the tree is in the range [0, 5000].

 >   	-1000 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 1000

 >   	-1000 <TeX>\leq</TeX> targetSum <TeX>\leq</TeX> 1000


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
trait Preorder {
    fn preorder(&self, visit: &mut dyn FnMut(i32, &Vec<i32>, i32), path: &mut Vec<i32>, path_sum: i32);
}
impl Preorder for TreeLink {
    fn preorder(&self, visit: &mut dyn FnMut(i32, &Vec<i32>,i32), path: &mut Vec<i32>, path_sum: i32) {
        if let Some(node) = self {
            let node: Ref<TreeNode> = node.borrow();
            if node.left.is_none() && node.right.is_none() {
                visit(node.val, path, path_sum);
                return;
            }
            path.push(node.val);
            let left_depth = node.left.preorder(visit, path, path_sum + node.val);
            let right_depth = node.right.preorder(visit, path, path_sum + node.val);
            path.pop();
        }
    }
}
impl Solution {
    pub fn path_sum(root: Option<Rc<RefCell<TreeNode>>>, target_sum: i32) -> Vec<Vec<i32>> {
        let mut res: Vec<Vec<i32>> = vec![];
        let mut path: Vec<i32> = vec![];
        root.preorder(&mut |x, path, path_sum| {
            if x + path_sum == target_sum {
                let mut res_path = path.clone();
                res_path.push(x);
                res.push(res_path);
            }
        }, &mut path, 0);
        res
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_113() {
        assert_eq!(
            Solution::path_sum(tree![5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1], 22),
            vec![vec![5, 4, 11, 2], vec![5, 8, 4, 5]]
        );
    }
}

```

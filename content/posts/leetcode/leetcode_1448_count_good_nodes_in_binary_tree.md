---
title: 1448. count good nodes in binary tree
date: '2022-08-06'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 1448 count good nodes in binary tree
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1448}/>
 

  Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

  

  Return the number of good nodes in the binary tree.

  

   

 >   Example 1:

  

 >   ![](https://assets.leetcode.com/uploads/2020/04/02/test_sample_1.png)

  

  

 >   Input: root <TeX>=</TeX> [3,1,4,3,null,1,5]

 >   Output: 4

 >   Explanation: Nodes in blue are good.

 >   Root Node (3) is always a good node.

 >   Node 4 -> (3,4) is the maximum value in the path starting from the root.

 >   Node 5 -> (3,4,5) is the maximum value in the path

 >   Node 3 -> (3,1,3) is the maximum value in the path.

  

 >   Example 2:

  

 >   ![](https://assets.leetcode.com/uploads/2020/04/02/test_sample_2.png)

  

  

 >   Input: root <TeX>=</TeX> [3,3,null,4,2]

 >   Output: 3

 >   Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

  

 >   Example 3:

  

  

 >   Input: root <TeX>=</TeX> [1]

 >   Output: 1

 >   Explanation: Root is considered as good.

  

   

  **Constraints:**

  

  

 >   	The number of nodes in the binary tree is in the range [1, 10^5].

 >   	Each node's value is between [-10^4, 10^4].


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
    fn preorder(&self, visit: &mut dyn FnMut(i32, i32), max_val: i32);
}
impl Preorder for TreeLink {
    fn preorder(&self, visit: &mut dyn FnMut(i32, i32), max_val: i32) {
        if let Some(node) = self {
            let node: Ref<TreeNode> = node.borrow();
            visit(node.val, max_val);
            let new_max_val = i32::max(node.val, max_val);
            node.left.preorder(visit, new_max_val);
            node.right.preorder(visit, new_max_val);
        }
    }
}
impl Solution {
    pub fn good_nodes(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut res = 0i32;
        root.preorder(&mut |val, max_val| {
            if val >= max_val {
                res += 1;
            }
        }, i32::MIN);
        res
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1448() {
        assert_eq!(Solution::good_nodes(tree![3,1,4,3,null,1,5]), 4);
        assert_eq!(Solution::good_nodes(tree![3,3,null,4,2]), 3);
        assert_eq!(Solution::good_nodes(tree![1]), 1);
    }
}

```

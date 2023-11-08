---
title: 450. delete node in a bst
date: '2022-03-13'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0450 delete node in a bst
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={450}/>
 

  Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

  Basically, the deletion can be divided into two stages:

  <ol>

  	Search for a node to remove.

  	If the node is found, delete the node.

  </ol>

  Follow up: Can you solve it with time complexity O(height of tree)?

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/09/04/del_node_1.jpg)

 >   Input: root <TeX>=</TeX> [5,3,6,2,4,null,7], key <TeX>=</TeX> 3

 >   Output: [5,4,6,2,null,null,7]

 >   Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.

 >   One valid answer is [5,4,6,2,null,null,7], shown in the above BST.

 >   Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

 >   ![](https://assets.leetcode.com/uploads/2020/09/04/del_node_supp.jpg)

  

 >   Example 2:

  

 >   Input: root <TeX>=</TeX> [5,3,6,2,4,null,7], key <TeX>=</TeX> 0

 >   Output: [5,3,6,2,4,null,7]

 >   Explanation: The tree does not contain a node with value <TeX>=</TeX> 0.

  

 >   Example 3:

  

 >   Input: root <TeX>=</TeX> [], key <TeX>=</TeX> 0

 >   Output: []

  

   

  **Constraints:**

  

 >   	The number of nodes in the tree is in the range [0, 10^4].

 >   	-10^5 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 10^5

 >   	Each node has a unique value.

 >   	root is a valid binary search tree.

 >   	-10^5 <TeX>\leq</TeX> key <TeX>\leq</TeX> 10^5


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
use std::cmp::Ordering::*;
trait Delete {
    fn delete(self, key: i32) -> Option<Rc<RefCell<TreeNode>>>;
    fn smallest(&self) -> i32;
}
impl Delete for Option<Rc<RefCell<TreeNode>>> {
    fn delete(self, key: i32) -> Option<Rc<RefCell<TreeNode>>> {
        if let Some(node) = self {
            let mut node = node.borrow_mut();
            let left = node.left.take();
            let right = node.right.take();
            let val = node.val;
            match key.cmp(&val) {
                Equal => match (left, right) {
                    (None, None) => None,
                    (None, Some(right)) => Some(right),
                    (Some(left), None) => Some(left),
                    (left, right) => {
                        let smallest = right.smallest();
                        Some(Rc::new(RefCell::new(TreeNode {
                            val: smallest,
                            left,
                            right: right.delete(smallest)
                        })))
                    }
                },
                Less => Some(Rc::new(RefCell::new(TreeNode {
                    val,
                    left: left.delete(key),
                    right
                }))),
                Greater => Some(Rc::new(RefCell::new(TreeNode {
                    val,
                    left,
                    right: right.delete(key)
                }))),
            }
        } else {
            None
        }
    }
    fn smallest(&self) -> i32 {
        if let Some(node) = self {
            let node = node.borrow();
            let val = node.val;
            if node.left.is_some() {
                node.left.smallest()
            } else {
                val
            }
        } else {
            unreachable!()
        }
    }
}
impl Solution {
    pub fn delete_node(root: Option<Rc<RefCell<TreeNode>>>, key: i32) -> Option<Rc<RefCell<TreeNode>>> {
        root.delete(key)
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_450() {
        assert_eq!(Solution::delete_node(tree![5,3,6,2,4,null,7], 3), tree![5,4,6,2,null,null,7]);
        assert_eq!(Solution::delete_node(tree![5,3,6,2,4,null,7], 0), tree![5,3,6,2,4,null,7]);
        assert_eq!(Solution::delete_node(tree![], 0), tree![]);
    }
}

```

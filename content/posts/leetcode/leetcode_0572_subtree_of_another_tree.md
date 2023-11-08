---
title: 572. subtree of another tree
date: '2022-04-07'
tags: ['leetcode', 'rust', 'python', 'easy']
draft: false
description: Solution for leetcode 0572 subtree of another tree
---



Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg)
>   Input: root <TeX>=</TeX> [3,4,5,1,2], subRoot <TeX>=</TeX> [4,1,2]
>   Output: true
>   Example 2:
>   ![](https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg)
>   Input: root <TeX>=</TeX> [3,4,5,1,2,null,null,null,null,0], subRoot <TeX>=</TeX> [4,1,2]
>   Output: false
**Constraints:**
>   	The number of nodes in the root tree is in the range [1, 2000].
>   	The number of nodes in the subRoot tree is in the range [1, 1000].
>   	-10^4 <TeX>\leq</TeX> root.val <TeX>\leq</TeX> 10^4
>   	-10^4 <TeX>\leq</TeX> subRoot.val <TeX>\leq</TeX> 10^4


## Solution
Traverse the root and find the node with the same value of the root of searched tree. Then, in order traverse the found nodes and the root of the searched tree and compare the results to make sure they are same or not.


### Python
```python
class Solution:
def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
def findNodes(root, val):
if root.left is None and root.right is None:
if root.val == val:
return [root]
else:
return []
if root.left is None:
results = findNodes(root.right, val)
if root.val == val:
return [root] + results
else:
return results
if root.right is None:
results = findNodes(root.left, val)
if root.val == val:
return [root] + results
else:
return results
rightResults = findNodes(root.right, val)
leftResults = findNodes(root.left, val)
if root.val == val:
return leftResults + [root] + rightResults
else:
return leftResults + rightResults
def inorder(root):
if root.left is None and root.right is None:
return [root.val]
if root.left is None:
results = inorder(root.right)
return [root.val] + results
if root.right is None:
results = inorder(root.left)
return results + [root.val]
rightResults = inorder(root.right)
leftResults = inorder(root.left)
return leftResults + [root.val] + rightResults

def compare(root1, root2):
values1 = inorder(root1)
values2 = inorder(root2)
if len(values1) != len(values2):
return False
for i in range(len(values1)):
if values1[i] != values2[i]:
return False
return True

startNodes = findNodes(root, subRoot.val)
for i in range(len(startNodes)):
res = compare(startNodes[i], subRoot)
if res:
return True
return False
```


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
pub fn is_subtree_helper(root: Option<&Rc<RefCell<TreeNode>>>, sub_root: Option<&Rc<RefCell<TreeNode>>>, search_mode: bool) -> bool {
if root.is_none() && sub_root.is_none() {
return true;
}
if root.is_none() && !sub_root.is_none() {
return false;
}
if !root.is_none() && sub_root.is_none() {
return false;
}
let node = root.unwrap().borrow();
let val = node.val;
let sub_root_node = sub_root.unwrap().borrow();
let sub_val = sub_root_node.val;
let left = node.left.as_ref();
let right = node.right.as_ref();
let sub_root_left = sub_root_node.left.as_ref();
let sub_root_right = sub_root_node.right.as_ref();
//println!("before val: {}, sub_val: {}", val, sub_val);
if search_mode {
return val == sub_val && Self::is_subtree_helper(left, sub_root_left, true)
&& Self::is_subtree_helper(right, sub_root_right, true)
}
if Self::is_subtree_helper(left, sub_root, false) || Self::is_subtree_helper(right, sub_root, false) {
return true;
}
val == sub_val && Self::is_subtree_helper(left, sub_root_left, true) && Self::is_subtree_helper(right, sub_root_right, true)
}
pub fn is_subtree(root: Option<Rc<RefCell<TreeNode>>>, sub_root: Option<Rc<RefCell<TreeNode>>>) -> bool {
Self::is_subtree_helper(root.as_ref(), sub_root.as_ref(), false)
}
}
// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_572() {
assert_eq!(Solution::is_subtree(tree![3,4,5,1,null,2], tree![3, 1, 2]), false);
assert_eq!(Solution::is_subtree(tree![1,1], tree![1]), true);
}
}

```

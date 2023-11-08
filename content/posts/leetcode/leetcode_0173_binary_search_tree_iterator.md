---
title: 173. binary search tree iterator
date: '2021-10-07'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0173 binary search tree iterator
---



Implement the BSTIterator class that represents an iterator over the [in-order traversal](https://en.wikipedia.org/wiki/Tree_traversal#In-order_(LNR)) of a binary search tree (BST):



BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.

boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.

int next() Moves the pointer to the right, then returns the number at the pointer.



Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2018/12/25/bst-tree.png)
>   Input
>   ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
>   [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
>   Output
>   [null, 3, 7, true, 9, true, 15, true, 20, false]
>   Explanation
>   BSTIterator bSTIterator <TeX>=</TeX> new BSTIterator([7, 3, 15, null, null, 9, 20]);
>   bSTIterator.next();    // return 3
>   bSTIterator.next();    // return 7
>   bSTIterator.hasNext(); // return True
>   bSTIterator.next();    // return 9
>   bSTIterator.hasNext(); // return True
>   bSTIterator.next();    // return 15
>   bSTIterator.hasNext(); // return True
>   bSTIterator.next();    // return 20
>   bSTIterator.hasNext(); // return False
**Constraints:**
>   	The number of nodes in the tree is in the range [1, 10^5].
>   	0 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 10^6
>   	At most 10^5 calls will be made to hasNext, and next.
>   Follow up:
>   	Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?


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
node.left.inorder(visit);
visit(node.val);
node.right.inorder(visit);
}
}
}

struct BSTIterator {
nums: Vec<i32>
}


/**
* `&self` means the method takes an immutable reference.
* If you need a mutable reference, change it to `&mut self` instead.
*/
impl BSTIterator {

fn new(root: Option<Rc<RefCell<TreeNode>>>) -> Self {
let mut nums = Vec::new();
root.inorder(&mut |x| {
nums.push(x);
});
nums.reverse();
Self{nums}
}

fn next(&mut self) -> i32 {
self.nums.pop().unwrap()
}

fn has_next(&self) -> bool {
self.nums.len() > 0
}
}

/**
* Your BSTIterator object will be instantiated and called as such:
* let obj = BSTIterator::new(root);
* let ret_1: i32 = obj.next();
* let ret_2: bool = obj.has_next();
*/

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_173() {
let mut iterator = BSTIterator::new(tree![7, 3, 15, null, null, 9, 20]);
assert_eq!(iterator.next(), 3); // return 3
assert_eq!(iterator.next(), 7); // return 7
assert_eq!(iterator.has_next(), true); // return true
assert_eq!(iterator.next(), 9); // return 9
assert_eq!(iterator.has_next(), true); // return true
assert_eq!(iterator.next(), 15); // return 15
assert_eq!(iterator.has_next(), true); // return true
assert_eq!(iterator.next(), 20); // return 20
assert_eq!(iterator.has_next(), false); // return false
}
}

```

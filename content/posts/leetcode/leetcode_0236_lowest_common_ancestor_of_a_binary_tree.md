---
title: 236. lowest common ancestor of a binary tree
date: '2021-11-22'
tags: ['leetcode', 'rust', 'python', 'medium']
draft: false
description: Solution for leetcode 0236 lowest common ancestor of a binary tree
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={236}/>
 

  Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

  According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): &ldquo;The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).&rdquo;

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

 >   Input: root <TeX>=</TeX> [3,5,1,6,2,0,8,null,null,7,4], p <TeX>=</TeX> 5, q <TeX>=</TeX> 1

 >   Output: 3

 >   Explanation: The LCA of nodes 5 and 1 is 3.

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

 >   Input: root <TeX>=</TeX> [3,5,1,6,2,0,8,null,null,7,4], p <TeX>=</TeX> 5, q <TeX>=</TeX> 4

 >   Output: 5

 >   Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

  

 >   Example 3:

  

 >   Input: root <TeX>=</TeX> [1,2], p <TeX>=</TeX> 1, q <TeX>=</TeX> 2

 >   Output: 1

  

   

  **Constraints:**

  

 >   	The number of nodes in the tree is in the range [2, 10^5].

 >   	-10^9 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 10^9

 >   	All Node.val are unique.

 >   	p !<TeX>=</TeX> q

 >   	p and q will exist in the tree.


## Solution
The key is to find a path from root to the node. We will find two paths and compare them to find the last common node. This node will be lowest common ancestor. 
### Python
```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findPath(root, p, path):
            if root is None:
                return None
            if root.val == p.val:
                path = path + [root]
                return path
            if root.left is None:
                return findPath(root.right, p, path + [root])
            if root.right is None:
                return findPath(root.left, p, path + [root])
            rightPath = findPath(root.right, p, path + [root])
            leftPath = findPath(root.left, p, path + [root])
            if rightPath is None:
                return leftPath
            return rightPath
        p_path = findPath(root, p, [])
        q_path = findPath(root, q, [])        
        ans = root
        min_len = min(len(p_path), len(q_path))
        for i in range(min_len):
            if p_path[i] == q_path[i]:
                ans = p_path[i]
            else:
                break
        return ans
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
use std::cell::{RefCell, Ref};
type TreeLink = Option<Rc<RefCell<TreeNode>>>;
trait Postorder {
    fn postorder(&self, visit: &mut dyn FnMut(i32, &Vec<i32>), path: &mut Vec<i32>);
}
impl Postorder for TreeLink {
    fn postorder(&self, visit: &mut dyn FnMut(i32, &Vec<i32>), path: &mut Vec<i32>) {
        if let Some(node) = self {
            let node: Ref<TreeNode> = node.borrow();
            path.push(node.val);
            visit(node.val, path);
            node.left.postorder(visit, path);
            node.right.postorder(visit, path);
            path.pop();
        }    
    }
}

impl Solution {
    pub fn lowest_common_ancestor(root: Option<Rc<RefCell<TreeNode>>>, p: Option<Rc<RefCell<TreeNode>>>, q: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut path: Vec<i32> = vec![];
        let mut p_path: Vec<i32> = vec![];
        let mut q_path: Vec<i32> = vec![];
        let p_val = p.unwrap().borrow().val;
        let q_val = q.unwrap().borrow().val;

        root.postorder(&mut |x, path| {
            if x == p_val {
                p_path = path.clone();
            }
            if x == q_val {
                q_path = path.clone();
            }
        }, &mut path);
        let mut i = 0;
        while i < p_path.len() && i < q_path.len() && p_path[i] == q_path[i] {
            i += 1;
        }
        Some(Rc::new(RefCell::new(TreeNode::new(p_path[i - 1]))))
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_236() {
        assert_eq!(
            Solution::lowest_common_ancestor(tree![3,5,1,6,2,0,8,null,null,7,4], 
                Some(Rc::new(RefCell::new(TreeNode::new(5)))), 
                Some(Rc::new(RefCell::new(TreeNode::new(1))))), 
                Some(Rc::new(RefCell::new(TreeNode::new(3)))));
        assert_eq!(
            Solution::lowest_common_ancestor(tree![3,5,1,6,2,0,8,null,null,7,4], 
                Some(Rc::new(RefCell::new(TreeNode::new(5)))), 
                Some(Rc::new(RefCell::new(TreeNode::new(4))))), 
                Some(Rc::new(RefCell::new(TreeNode::new(5)))));    
    }
}

```

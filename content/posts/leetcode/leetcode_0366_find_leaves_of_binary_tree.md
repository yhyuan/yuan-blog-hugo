---
title: 366. find leaves of binary tree
date: '2022-01-27'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0366 find leaves of binary tree
---


Given the root of a binary tree, collect a tree's nodes as if you were doing this:



Collect all the leaf nodes.

Remove all the leaf nodes.

Repeat until the tree is empty.

 



 > Example 1:





 > Input: root <TeX>=</TeX> [1,2,3,4,5]

 > Output: [[4,5,3],[2],[1]]

 > Explanation:

 > [[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.

 > Example 2:



 > Input: root <TeX>=</TeX> [1]

 > Output: [[1]]

 



**Constraints:**



 > The number of nodes in the tree is in the range [1, 100].

 > -100 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 100


## Solution
### Rust
```rust
pub struct Solution {}
use crate::util::tree::{TreeNode, to_tree};


// submission codes start here
/*
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root: Optional[TreeNode], heights):
        if root is None:
            return
        if root.left is None and root.right is None:
            heights.append((0, root.val))
            return 0

        if root.left is None:
            right_height = self.height(root.right, heights)
            heights.append((right_height + 1, root.val))
            return right_height + 1

        if root.right is None:
            left_height = self.height(root.left, heights)
            heights.append((left_height + 1, root.val))
            return left_height + 1

        right_height = self.height(root.right, heights)
        left_height = self.height(root.left, heights)
        height = max(right_height, left_height) + 1
        heights.append((height, root.val))
        return height
    
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        heights = []
        self.height(root, heights)
        heights.sort()
        print(heights)
        currentHeight = -1
        res = []
        row = []
        for height in heights:
            if currentHeight != height[0]:
                if currentHeight != -1:
                    res.append(row.copy())
                row = [height[1]]
                currentHeight = height[0]
            else:
                row.append(height[1])
        res.append(row)
        return res

class Solution:
    def height(self, root: Optional[TreeNode], heights):
        if root is None:
            return
        if root.left is None and root.right is None:
            if len(heights) == 0:
                heights.append([])
            heights[0].append(root.val)
            return 0

        if root.left is None:
            right_height = self.height(root.right, heights)
            if len(heights) == right_height + 1:
                heights.append([])
            heights[right_height + 1].append(root.val)
            return right_height + 1

        if root.right is None:
            left_height = self.height(root.left, heights)
            if len(heights) == left_height + 1:
                heights.append([])
            heights[left_height + 1].append(root.val)
            return left_height + 1

        right_height = self.height(root.right, heights)
        left_height = self.height(root.left, heights)
        height = max(right_height, left_height)
        if len(heights) == height + 1:
            heights.append([])
        heights[height + 1].append(root.val)
        return height + 1
    
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        heights = []
        self.height(root, heights)
        return heights
*/
use std::rc::Rc;
use std::cell::{RefCell, Ref};
use std::collections::HashMap;
type TreeLink = Option<Rc<RefCell<TreeNode>>>;
trait Postorder {
    fn postorder(&self, visited: &mut dyn FnMut(i32, i32)) -> i32;
}
impl Postorder for TreeLink {
    fn postorder(&self, visited: &mut dyn FnMut(i32, i32)) -> i32 {
        if let Some(node) = self {
            let node: Ref<TreeNode> = node.borrow();
            let left_height = node.left.postorder(visited);
            let right_height = node.right.postorder(visited);
            let height = 1 + i32::max(left_height, right_height);
            visited(node.val, height);
            return height;
        }
        return -1;
    }
}
impl Solution {
    pub fn find_leaves(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut heights: Vec<Vec<i32>> = vec![];
        root.postorder(&mut |node_val, height| {
            let height = height as usize;
            // println!("val: {}, height: {}", node_val, height);
            if heights.len() <= height {
                for _ in heights.len()..height + 1 {
                    heights.push(vec![])
                }
            }
            heights[height].push(node_val);
        });
        heights
    }
}


// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_366() {
        assert_eq!(Solution::find_leaves(tree![1,2,3,4,5]), vec![vec![5, 3, 4], vec![2], vec![1]]);
        assert_eq!(Solution::find_leaves(tree![1]), vec![vec![1]]);
    }
}

```

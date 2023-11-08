---
title: 124. binary tree maximum path sum
date: '2021-08-31'
tags: ['leetcode', 'rust', 'python', 'hard']
draft: false
description: Solution for leetcode 0124 binary tree maximum path sum
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={124}/>
 

  A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

  The path sum of a path is the sum of the node's values in the path.

  Given the root of a binary tree, return the maximum path sum of any path.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg)

 >   Input: root <TeX>=</TeX> [1,2,3]

 >   Output: 6

 >   Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 <TeX>=</TeX> 6.

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg)

 >   Input: root <TeX>=</TeX> [-10,9,20,null,null,15,7]

 >   Output: 42

 >   Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 <TeX>=</TeX> 42.

  

   

  **Constraints:**

  

 >   	The number of nodes in the tree is in the range [1, 3  10^4].

 >   	-1000 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 1000


## Solution
Solution:

The key to solve this problem is to find max sum for a path which starts at lower level and ends at one specific node. We can define it as F(n). The max sum for this node can be the maximum value of the following three cases:

It only contains this node. We will return node.val

It is the combination of the result of the left branch and node.val

It is the combination of the result of the right branch and node.val

F(n) = max(node.val, F(n.left) + node.val, F(n.right) + node.val)

Meanwhile, we can define the max sum of a path that pass node n. It could be four cases:

It only contains this node. It will be node.val

It could be this node plus the result from the left branch. 

It could be this node plus the result from the right branch. 

It could be this node plus the result from the left branch and the result from right branch.

So the result at each node will be 

P(n) = max(node.val, F(n.left) + node.val, F(n.right) + node.val, F(n.right) + node.val + F(n.left). 

The maximum of P(n) is the final result.

### Python
```python
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Find the max path sum for a path ends at root. 
        def helper(root: Optional[TreeNode], maxPathSum):
            if root.left is None and root.right is None:
                maxPathSum[0] = max(maxPathSum[0], root.val)
                return root.val
            if root.left is None:
                r = helper(root.right, maxPathSum)
                maxPathSum[0] = max(maxPathSum[0], root.val, r + root.val)
                return max(root.val, r + root.val)
            if root.right is None:
                l = helper(root.left, maxPathSum)
                maxPathSum[0] = max(maxPathSum[0], root.val, l + root.val)
                return max(root.val, l + root.val)
            r = helper(root.right, maxPathSum)
            l = helper(root.left, maxPathSum)
            maxPathSum[0] = max(maxPathSum[0], root.val, r + root.val , l + root.val, r + root.val + l)
            return max(root.val, l + root.val, r + root.val)
        if root is None:
            return -float('inf')
        maxPathSum = [-float('inf')]
        helper(root, maxPathSum)
        return maxPathSum[0]
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
/*
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn max_path_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut max = i32::min_value();
        Solution::postorder(root.as_ref(), &mut max);
        max
      }
      fn postorder(root: Option<&Rc<RefCell<TreeNode>>>, max: &mut i32) -> i32 {
        if let Some(node) = root {
            let left = Solution::postorder(node.borrow().left.as_ref(), max);
            let right = Solution::postorder(node.borrow().right.as_ref(), max);
            *max = i32::max(
                node.borrow().val + i32::max(left, 0) + i32::max(right, 0),
                *max,
            );
            node.borrow().val + i32::max(i32::max(left, right), 0)
        } else {
            0
        }
    }
}
*/
use std::rc::Rc;
use std::cell::{RefCell, Ref};
type TreeLink = Option<Rc<RefCell<TreeNode>>>;
trait Postorder {
    fn postorder(&self, visit: &mut dyn FnMut(i32, i32, i32)) -> i32;
}
impl Postorder for TreeLink {
    fn postorder(&self, visit: &mut dyn FnMut(i32, i32, i32)) -> i32 {
        if let Some(node) = self {
            let node: Ref<TreeNode> = node.borrow();
            let left = node.left.postorder(visit);
            let right = node.right.postorder(visit);
            visit(node.val, left, right);
            return node.val + i32::max(i32::max(left, right), 0);
        }
        0i32
    }
}
impl Solution {
    pub fn max_path_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut max = i32::min_value();
        root.postorder(&mut |x, left, right| {
            max = i32::max(
                x + i32::max(left, 0) + i32::max(right, 0),
                max
            );
        });
        max
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_124() {
        assert_eq!(Solution::max_path_sum(tree![1, 2, 3]), 6);
        assert_eq!(
            Solution::max_path_sum(tree![-10, 9, 20, null, null, 15, 7]),
            42
        );
        assert_eq!(
            Solution::max_path_sum(tree![5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1]),
            48
        );
        assert_eq!(Solution::max_path_sum(tree![-3]), -3);
    }
}

```

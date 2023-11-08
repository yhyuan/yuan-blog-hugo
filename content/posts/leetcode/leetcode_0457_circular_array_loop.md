---
title: 457. Circular Array Loop
date: '2022-03-13'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 0457. Circular Array Loop
---

 
You are playing a game involving a circular array of non-zero integers nums. Each nums[i] denotes the number of indices forward/backward you must move if you are located at index i:

If nums[i] is positive, move nums[i] steps forward, and

If nums[i] is negative, move nums[i] steps backward.

Since the array is circular, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on the last element.

A cycle in the array consists of a sequence of indices seq of length k where:

Following the movement rules above results in the repeating index sequence seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...

Every nums[seq[j]] is either all positive or all negative.

k > 1

Return true if there is a cycle in nums, or false otherwise.

 > Example 1:

 > Input: nums <TeX>=</TeX> [2,-1,1,2,2]
 > Output: true
 > Explanation:
 > There is a cycle from index 0 -> 2 -> 3 -> 0 -> ...
 > The cycle's length is 3.

 > Example 2:

 > Input: nums <TeX>=</TeX> [-1,2]
 > Output: false
 > Explanation:
 > The sequence from index 1 -> 1 -> 1 -> ... is not a cycle because the sequence's length is 1.
 > By definition the sequence's length must be strictly greater than 1 to be a cycle.

 > Example 3:

 > Input: nums <TeX>=</TeX> [-2,1,-1,-2,-2]
 > Output: false
 > Explanation:
 > The sequence from index 1 -> 2 -> 1 -> ... is not a cycle because nums[1] is positive, but nums[2] is negative.
 > Every nums[seq[j]] must be either all positive or all negative.

**Constraints:**

 > 1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 5000

 > -1000 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 1000

 > nums[i] !<TeX>=</TeX> 0

 > Follow up: Could you solve it in O(n) time complexity and O(1) extra space complexity?


## Solution
The key is to define a findNextIndex function. It will remove the circle with one element and the circle with wrong direction. The time complexity is O(N^2) and the space complexity is O(1).

### Python
```python
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        def findNextIndex(index, direction):
            if (nums[index] > 0) != direction:
                return -1
            ans = (index + nums[index]) % len(nums)
            if ans < 0:
                ans + len(nums)
            if ans == index: # one element cycle
                return -1
            return ans
        def helper(index, direction):
            slow = index
            fast = index
            while True:
                slow = findNextIndex(slow, direction)
                fast = findNextIndex(fast, direction)
                if fast != -1:
                    fast = findNextIndex(fast, direction)
                if slow == -1 or fast == -1 or slow == fast:
                    break
            if slow != -1 and slow == fast:
                return True
            return False
            
        for i in range(n):
            if helper(i, nums[i] > 0):
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
use std::cmp::Ordering::*;
trait Delete {
    fn delete(self, key: i32) -> Option<Rc<RefCell<TreeNode>>>;
    fn smallest(&self) -> i32;
}
impl Delete for Option<Rc<RefCell<TreeNode>>> {
    fn delete(self, key: i32) -> Option<Rc<RefCell<TreeNode>>> {
        if let Some(node) <TeX>=</TeX> self {
            let mut node <TeX>=</TeX> node.borrow_mut();
            let left <TeX>=</TeX> node.left.take();
            let right <TeX>=</TeX> node.right.take();
            let val <TeX>=</TeX> node.val;
            match key.cmp(&val) {
                Equal <TeX>=</TeX>> match (left, right) {
                    (None, None) <TeX>=</TeX>> None,
                    (None, Some(right)) <TeX>=</TeX>> Some(right),
                    (Some(left), None) <TeX>=</TeX>> Some(left),
                    (left, right) <TeX>=</TeX>> {
                        let smallest <TeX>=</TeX> right.smallest();
                        Some(Rc::new(RefCell::new(TreeNode {
                            val: smallest,
                            left,
                            right: right.delete(smallest)
                        })))
                    }
                },
                Less <TeX>=</TeX>> Some(Rc::new(RefCell::new(TreeNode {
                    val,
                    left: left.delete(key),
                    right
                }))),
                Greater <TeX>=</TeX>> Some(Rc::new(RefCell::new(TreeNode {
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
        if let Some(node) <TeX>=</TeX> self {
            let node <TeX>=</TeX> node.borrow();
            let val <TeX>=</TeX> node.val;
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

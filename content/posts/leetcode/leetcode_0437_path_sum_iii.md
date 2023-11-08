---
title: 437. Path Sum III
date: '2022-03-12'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 0437. Path Sum III
---


Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

> Example 1:
> Input: root <TeX>=</TeX> [10,5,-3,3,2,null,11,3,-2,null,1], targetSum <TeX>=</TeX> 8
> Output: 3
> Explanation: The paths that sum to 8 are shown.
> Example 2:
> Input: root <TeX>=</TeX> [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum <TeX>=</TeX> 22
> Output: 3
**Constraints:**
> The number of nodes in the tree is in the range [0, 1000].
> -109 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 109
> -1000 <TeX>\leq</TeX> targetSum <TeX>\leq</TeX> 1000


## Solution
We can divide the path to two categories:

Root node is included. We can define a helper function to find the path in this category. Then, the result we will find the is left branch result plus right branch result with new target Sum: old target Sum minus root value. If the root value is as same as target Sum, we have find one path.

Root node is not included. It means we need to the search the left and right branch with the same settings in the main problem.


### Python
```python
class Solution:
def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:


# root is included
def helper(root, targetSum):
if root is None:
return 0
ans = 0
if root.val == targetSum:
ans += 1
return ans + helper(root.left, targetSum - root.val) + helper(root.right, targetSum - root.val)

if root is None:
return 0
ans = helper(root, targetSum)


# print("root.val: {}, ans: {}".format(root.val, ans))


# print(ans)
if root.left is None and root.right is None:
return ans
if root.left is None:
return ans + self.pathSum(root.right, targetSum)
if root.right is None:
return ans + self.pathSum(root.left, targetSum)
ans += self.pathSum(root.left, targetSum)
ans += self.pathSum(root.right, targetSum)
return ans
```

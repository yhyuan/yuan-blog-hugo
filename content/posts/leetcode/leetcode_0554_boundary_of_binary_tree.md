---
title: 545. Boundary of Binary Tree
date: '2022-04-01'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 0545. Boundary of Binary Tree
---

The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.

The left boundary is the set of nodes defined by the following:

The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.

If a node in the left boundary and has a left child, then the left child is in the left boundary.

If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.

The leftmost leaf is not in the left boundary.

The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

Given the root of a binary tree, return the values of its boundary.

> Example 1:
> Input: root <TeX>=</TeX> [1,null,2,3,4]
> Output: [1,3,4,2]
> Explanation:
> - The left boundary is empty because the root does not have a left child.
> - The right boundary follows the path starting from the root's right child 2 -> 4.
>   4 is a leaf, so the right boundary is [2].
> - The leaves from left to right are [3,4].
> Concatenating everything results in [1] + [] + [3,4] + [2] <TeX>=</TeX> [1,3,4,2].
> Example 2:
> Input: root <TeX>=</TeX> [1,2,3,4,5,6,null,null,null,7,8,9,10]
> Output: [1,2,4,7,8,9,10,6,3]
> Explanation:
> - The left boundary follows the path starting from the root's left child 2 -> 4.
>   4 is a leaf, so the left boundary is [2].
> - The right boundary follows the path starting from the root's right child 3 -> 6 -> 10.
>   10 is a leaf, so the right boundary is [3,6], and in reverse order is [6,3].
> - The leaves from left to right are [4,7,8,9,10].
> Concatenating everything results in [1] + [2] + [4,7,8,9,10] + [6,3] <TeX>=</TeX> [1,2,4,7,8,9,10,6,3].
**Constraints:**
> The number of nodes in the tree is in the range [1, 104].
> -1000 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 1000


## Solution
Firstly, let's deal with corn cases firstly. If a tree is None or a tree only contains one node, we will return empty array or array with root value.

We develop two functions. The first is to find the boundary and the second one is used to find the leaves. The first function allows to use a boolean to search left or search right. If we search left, we will search left if there is a left branch. otherwise, we will search right until we reach a leaf node. We ill not include leaf node and the root in the boundary.

The leaf node search is to find the node without children.



### Python
```python
def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
def findBoundary(root, isLeft):
if isLeft and root.left is None:
return []
if not isLeft and root.right is None:
return []
node = root
result = []
while node.left is not None or node.right is not None:
if isLeft:
node = node.left if node.left is not None else node.right
else:
node = node.right if node.right is not None else node.left
if node.left is not None or node.right is not None:
result.append(node.val) # not leaf node
return result

leaves = []
def findLeaves(root):
if root.left is None and root.right is None:
leaves.append(root.val)
return
if root.left is None:
findLeaves(root.right)
return
if root.right is None:
findLeaves(root.left)
return
findLeaves(root.left)
findLeaves(root.right)
return

if root is None:
return []
if root.left is None and root.right is None:
return [root.val]
leftBoundary = findBoundary(root, True)
rightBoundary = findBoundary(root, False)
findLeaves(root)
rightBoundary.reverse()
return [root.val] + leftBoundary + leaves + rightBoundary
```

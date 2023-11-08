---
title: 2385. Amount of Time for Binary Tree to Be Infected
date: '2022-09-28'
tags: ['leetcode', 'python']
draft: false
description: Solution for leetcode 2385. Amount of Time for Binary Tree to Be Infected
---


You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.

The node is adjacent to an infected node.

Return the number of minutes needed for the entire tree to be infected.

> Example 1:
> Input: root = [1,5,3,null,4,10,6,9,2], start = 3
> Output: 4
> Explanation: The following nodes are infected during:
> - Minute 0: Node 3
> - Minute 1: Nodes 1, 10 and 6
> - Minute 2: Node 5
> - Minute 3: Node 4
> - Minute 4: Nodes 9 and 2
> It takes 4 minutes for the whole tree to be infected so we return 4.
> Example 2:
> Input: root = [1], start = 1
> Output: 0
> Explanation: At minute 0, the only node in the tree is infected so we return 0.
**Constraints:**
> The number of nodes in the tree is in the range [1, 105].
> 1 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 105
> Each node has a unique value.
> A node with a value of start exists in the tree.


## Solution
Solution: Convert the tree to a graph and BFS it.


### Python
```python


# Definition for a binary tree node.


# class TreeNode:


#     def __init__(self, val=0, left=None, right=None):


#         self.val = val


#         self.left = left


#         self.right = right
class Solution:
def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
def buildGraph(root):
graph = {}
def helper(root):
if root is None:
return
if root.left is None and root.right is None:
return
if root.left is None:
graph[root.val] = graph.get(root.val, []) + [root.right.val]
graph[root.right.val]  = graph.get(root.right.val, []) + [root.val]
helper(root.right)
return
if root.right is None:
graph[root.val] = graph.get(root.val, []) + [root.left.val]
graph[root.left.val]  = graph.get(root.left.val, []) + [root.val]
helper(root.left)
return
graph[root.val] = graph.get(root.val, []) + [root.right.val, root.left.val]
graph[root.right.val]  = graph.get(root.right.val, []) + [root.val]
graph[root.left.val]  = graph.get(root.left.val, []) + [root.val]
helper(root.right)
helper(root.left)
return
helper(root)
return graph
graph = buildGraph(root)
q = deque([start])
visited = set([start])
steps = 0
while len(q) > 0:
n = len(q)
for _ in range(n):
v = q.popleft()
if not v in graph:
continue
for neighbor in graph[v]:
if not neighbor in visited:
q.append(neighbor)
visited.add(neighbor)
steps += 1
return steps - 1
```

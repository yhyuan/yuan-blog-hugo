---
title: 863. All Nodes Distance K in Binary Tree
date: '2022-06-01'
tags: ['leetcode', 'python', 'hard']
draft: false
description: Solution for leetcode 0863. All Nodes Distance K in Binary Tree
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={863}/>
 
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 > Example 1:

 > Input: root <TeX>=</TeX> [3,5,1,6,2,0,8,null,null,7,4], target <TeX>=</TeX> 5, k <TeX>=</TeX> 2
 > Output: [7,4,1]
 > Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

 > Example 2:

 > Input: root <TeX>=</TeX> [1], target <TeX>=</TeX> 1, k <TeX>=</TeX> 3
 > Output: []

**Constraints:**

 > The number of nodes in the tree is in the range [1, 500].

 > 0 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 500

 > All the values Node.val are unique.

 > target is the value of one of the nodes in the tree.

 > 0 <TeX>\leq</TeX> k <TeX>\leq</TeX> 1000

## Solution
Convert it to a graph and use BFS to solve it. Pay attention to corner cases:

There is one node in the tree.

k = 0

### Python
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = {}
        def buildGraph(root, graph):
            if root is None:
                return
            if root.left is None and root.right is None:
                return
            if root.left is None:
                graph[root.val] = graph.get(root.val, []) + [root.right.val]
                graph[root.right.val] = graph.get(root.right.val, []) + [root.val]
                buildGraph(root.right, graph)
                return
            if root.right is None:
                graph[root.val] = graph.get(root.val, []) + [root.left.val]
                graph[root.left.val] = graph.get(root.left.val, []) + [root.val]
                buildGraph(root.left, graph)
                return
            graph[root.val] = graph.get(root.val, []) + [root.left.val, root.right.val]
            graph[root.right.val] = graph.get(root.right.val, []) + [root.val]
            graph[root.left.val] = graph.get(root.left.val, []) + [root.val]
            buildGraph(root.left, graph)
            buildGraph(root.right, graph)
            return
        
        if root.left == None and root.right == None:
            if root.val == target.val and k == 0:
                return [root.val]
            return []
        
        if k == 0:
            return [target.val]
        buildGraph(root, graph)
        q = deque([target.val])
        visited = set([target.val])
        steps = 0
        while len(q) > 0:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                neighbors = graph[node]
                for neighbor in neighbors:
                    if not neighbor in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            steps += 1
            if steps == k:
                break
        ans = []
        while len(q) > 0:
            node = q.popleft()
            ans.append(node)
        return ans

```

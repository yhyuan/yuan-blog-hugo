---
title: 2371. Minimize Maximum Value in a Grid
date: '2022-09-28'
tags: ['leetcode', 'python']
draft: false
description: Solution for leetcode 2371. Minimize Maximum Value in a Grid
---



You are given an m x n integer matrix grid containing distinct positive integers.

You have to replace each integer in the matrix with a positive integer satisfying the following conditions:

The relative order of every two elements that are in the same row or column should stay the same after the replacements.

The maximum number in the matrix after the replacements should be as small as possible.

The relative order stays the same if for all pairs of elements in the original matrix such that grid[r1][c1] > grid[r2][c2] where either r1 <TeX>=</TeX><TeX>=</TeX> r2 or c1 <TeX>=</TeX><TeX>=</TeX> c2, then it must be true that grid[r1][c1] > grid[r2][c2] after the replacements.

For example, if grid <TeX>=</TeX> [[2, 4, 5], [7, 3, 9]] then a good replacement could be either grid <TeX>=</TeX> [[1, 2, 3], [2, 1, 4]] or grid <TeX>=</TeX> [[1, 2, 3], [3, 1, 4]].

Return the resulting matrix. If there are multiple answers, return any of them.

> Example 1:
> Input: grid <TeX>=</TeX> [[3,1],[2,5]]
> Output: [[2,1],[1,2]]
> Explanation: The above diagram shows a valid replacement.
> The maximum number in the matrix is 2. It can be shown that no smaller value can be obtained.
> Example 2:
> Input: grid <TeX>=</TeX> [[10]]
> Output: [[1]]
> Explanation: We replace the only number in the matrix with 1.
**Constraints:**
> m <TeX>==</TeX> grid.length
> n <TeX>==</TeX> grid[i].length
> 1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 1000
> 1 <TeX>\leq</TeX> m * n <TeX>\leq</TeX> 105
> 1 <TeX>\leq</TeX> grid[i][j] <TeX>\leq</TeX> 109
> grid consists of distinct integers.


## Solution



### Python
```python
class Solution:
def minScore(self, grid: List[List[int]]) -> List[List[int]]:
m = len(grid)
n = len(grid[0])
if m == 1 and n == 1:
return [[1]]
def buildGraph(grid):
m = len(grid)
n = len(grid[0])
graph = {}
for i in range(m):
items = list(map(lambda j: (grid[i][j], (i, j)), range(n)))
items.sort()
for j in range(n):
(_, pos) = items[j]
ends = list(map(lambda k: items[k][1], range(j + 1, n)))
if pos in graph:
graph[pos] = graph[pos] + ends
else:
graph[pos] = ends
for j in range(n):
items = list(map(lambda i: (grid[i][j], (i, j)), range(m)))
items.sort()
for i in range(m):
(_, pos) = items[i]
ends = list(map(lambda k: items[k][1], range(i + 1, m)))
if pos in graph:
graph[pos] = graph[pos] + ends
else:
graph[pos] = ends
return graph
graph = buildGraph(grid)
def calculateIndegree(graph):
indegree = {}
for start in graph:
for end in graph[start]:
if end in indegree:
indegree[end] += 1
else:
indegree[end] = 1
if not start in indegree:
indegree[start] = 0
return indegree
indegree = calculateIndegree(graph)
q = deque()
for node in indegree:
if indegree[node] == 0:
q.append(node)
steps = 1
while len(q) > 0:
n = len(q)


#print("n: {}".format(n))
for _ in range(n):
node = q.popleft()
del indegree[node]
grid[node[0]][node[1]] = steps
if node in graph:
for neighbor in graph[node]:
if neighbor in indegree:
indegree[neighbor] -= 1
if indegree[neighbor] == 0:
q.append(neighbor)
steps += 1
return grid

```

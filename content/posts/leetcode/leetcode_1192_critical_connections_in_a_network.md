---
title: 1192. critical connections in a network
date: '2022-07-18'
tags: ['leetcode', 'rust', 'python', 'hard']
draft: false
description: Solution for leetcode 1192 critical connections in a network
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1192}/>
 

  There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] <TeX>=</TeX> [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

  A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

  Return all critical connections in the network in any order.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2019/09/03/1537_ex1_2.png)

 >   Input: n <TeX>=</TeX> 4, connections <TeX>=</TeX> [[0,1],[1,2],[2,0],[1,3]]

 >   Output: [[1,3]]

 >   Explanation: [[3,1]] is also accepted.

  

 >   Example 2:

  

 >   Input: n <TeX>=</TeX> 2, connections <TeX>=</TeX> [[0,1]]

 >   Output: [[0,1]]

  

   

  **Constraints:**

  

 >   	2 <TeX>\leq</TeX> n <TeX>\leq</TeX> 10^5

 >   	n - 1 <TeX>\leq</TeX> connections.length <TeX>\leq</TeX> 10^5

 >   	0 <TeX>\leq</TeX> ai, bi <TeX>\leq</TeX> n - 1

 >   	ai !<TeX>=</TeX> bi

 >   	There are no repeated connections.


## Solution
Solution: We will use Tarjan's Bridge-Finding Algorithm (TBFA) to solve this problem. The bridge is defined as an edge. If this edge is removed, the graph will become unconnected. The time complexity is O(V + E).

The current edge (v,to) is a bridge if and only if none of the vertices to and its descendants in the DFS traversal tree has a back-edge to vertex v or any of its ancestors. Indeed, this condition means that there is no other way from v to to except for edge (v,to).

So, let tin[v] denote entry time for node v. We introduce an array low which will let us check the fact for each vertex v. low[v] is the minimum of tin[v], the entry times tin[p] for each node p that is connected to node v via a back-edge (v,p) and the values of low[to] for each vertex to which is a direct descendant of v in the DFS tree:

```
low[v] = min(tin[v], tin[p], low[to])
tin[p]: for all p for which (v,p) is a back edge
low[to]: for all to for which (v,to) is a tree edge
```
Now, there is a back edge from vertex v or one of its descendants to one of its ancestors if and only if vertex v has a child to for which low[to]≤tin[v]. If low[to]=tin[v], the back edge comes directly to v, otherwise it comes to one of the ancestors of v.

Thus, the current edge (v,to) in the DFS tree is a bridge if and only if low[to]>tin[v].

We need to define 
visited: to mark whether a node has been visited.

parent: to mark the parent for a node in DFS tree.

disc: to mark the discovery time of a node.

low: low[i] = min(disc[i], disc[p], low[to]) i->p is a back edge and i -> to is a tree edge. 

edge i -> to is a bridge if and only if low[to] > disc[i]

```
visited = [False] * n
parent = [-1] * n
disc = [-1] * n
low = [-1] * n
res = []
time = [1]
def dfs(u):
    visited[u] = True
    disc[u] = time[0]
    low[u] = disc[u]
    time[0] = time[0] + 1
    for v in graph[u]:
        if not visited[v]:
            parent[v] = u
            dfs(v)
            low[u] = min(low[u], low[v])
            if low[v] > disc[u]:
                res.append([u, v])
        else: #back edge.
            if v != parent[u]:
                low[u] = min(low[u], disc[v])
    time[0] = time[0] - 1
```

```
Articulation points represent vulnerabilities in a connected network – single points whose failure would split the network into 2 or more components. 
 # u is an articulation point in following cases
 # (1) u is root of DFS tree and has two or more children.
if parent[u] == -1 and children > 1:
    ap[u] = True
#(2) If u is not root and low value of one of its #child is more than discovery value of u.
if parent[u] != -1 and low[v] >= disc[u]:
    ap[u] = True 
```
### Python
```python
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # Tarjan's Bridge-Finding Algorithm (TBFA).
        graph = [[]] * n
        for i in range(len(connections)):
            start = connections[i][0]
            end   = connections[i][1]
            graph[start] = graph[start] + [end]
            graph[end] = graph[end] + [start]
        visited = [False] * n
        parent = [-1] * n
        disc = [-1] * n
        low = [-1] * n
        res = []
        time = [1]
        def dfs(index):
            visited[index] = True
            disc[index] = time[0]
            low[index] = time[0]
            time[0] = time[0] + 1
            for neighbor in graph[index]:
                if not visited[neighbor]:
                    parent[neighbor] = index
                    dfs(neighbor)
                    low[index] = min(low[index], low[neighbor])
                    if low[neighbor] > disc[index]:
                        res.append([index, neighbor])
                else:
                    if neighbor != parent[index]:
                        low[index] = min(low[index], disc[neighbor])
            time[0] = time[0] - 1
            
        for i in range(n):
            if not visited[i]:
                dfs(i)
        return res
```
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashSet;
impl Solution {
    pub fn dfs(u: usize, graph: &Vec<Vec<usize>>, visited: &mut Vec<bool>, parent: &mut Vec<usize>, disc: &mut Vec<usize>, low: &mut Vec<usize>, res: &mut Vec<Vec<i32>>, time: &mut usize) {
        visited[u] = true;
        disc[u] = *time;
        low[u] = *time;
        *time += 1;
        for &v in graph[u].iter() {
            if !visited[v] {
                parent[v] = u;
                Self::dfs(v, graph, visited, parent, disc, low, res, time);
                low[u] = usize::min(low[u], low[v]);
                if low[v] > disc[u] {
                    res.push(vec![u as i32, v as i32]);
                }
            } else {
                if v != parent[u] {
                    low[u] = usize::min(low[u], disc[v]);
                }
            }
        }
        *time -= 1;
    }
    pub fn critical_connections(n: i32, connections: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = n as usize;
        let mut graph: Vec<Vec<usize>> = vec![vec![]; n];
        for i in 0..connections.len() {
            let start = connections[i][0] as usize;
            let end   = connections[i][1] as usize;
            graph[start].push(end);
            graph[end].push(start);
        }
        let mut visited: Vec<bool> = vec![false; n];
        let mut parent: Vec<usize> = vec![usize::MAX; n];
        let mut disc: Vec<usize> = vec![usize::MAX; n];
        let mut low: Vec<usize> = vec![usize::MAX; n];
        let mut res: Vec<Vec<i32>> = vec![];
        let mut time = 1usize;
        for i in 0..n {
            if !visited[i] {
                Self::dfs(i, &graph, &mut visited, &mut parent, &mut disc, &mut low, &mut res, &mut time);
            }
        }
        /*
        println!("visited: {:?}", visited);
        println!("parent: {:?}", parent);
        println!("disc: {:?}", disc);
        println!("low: {:?}", low);
        println!("res: {:?}", res);
        */
        res
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1192() {
        assert_eq!(Solution::critical_connections(4, vec![vec![0,1],vec![1,2],vec![2,0],vec![1,3]]), vec![vec![1,3]]);
        assert_eq!(Solution::critical_connections(2, vec![vec![0,1]]), vec![vec![0,1]]);
    }
}

```

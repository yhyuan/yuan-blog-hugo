---
title: 1697. checking existence of edge length limited paths
date: '2022-08-23'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1697 checking existence of edge length limited paths
---



An undirected graph of n nodes is defined by edgeList, where edgeList[i] <TeX>=</TeX> [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] <TeX>=</TeX> [pj, qj, limitj], your task is to determine for each queries[j] whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj .

Return a boolean array answer, where answer.length <TeX>=</TeX><TeX>=</TeX> queries.length and the j^th value of answer is true if there is a path for queries[j] is true, and false otherwise.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2020/12/08/h.png)
>   Input: n <TeX>=</TeX> 3, edgeList <TeX>=</TeX> [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries <TeX>=</TeX> [[0,1,2],[0,2,5]]
>   Output: [false,true]
>   Explanation: The above figure shows the given graph. Note that there are two overlapping edges between 0 and 1 with distances 2 and 16.
>   For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return false for this query.
>   For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, thus we return true for this query.
>   Example 2:
>   ![](https://assets.leetcode.com/uploads/2020/12/08/q.png)
>   Input: n <TeX>=</TeX> 5, edgeList <TeX>=</TeX> [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries <TeX>=</TeX> [[0,4,14],[1,4,13]]
>   Output: [true,false]
>   Exaplanation: The above figure shows the given graph.
**Constraints:**
>   	2 <TeX>\leq</TeX> n <TeX>\leq</TeX> 10^5
>   	1 <TeX>\leq</TeX> edgeList.length, queries.length <TeX>\leq</TeX> 10^5
>   	edgeList[i].length <TeX>=</TeX><TeX>=</TeX> 3
>   	queries[j].length <TeX>=</TeX><TeX>=</TeX> 3
>   	0 <TeX>\leq</TeX> ui, vi, pj, qj <TeX>\leq</TeX> n - 1
>   	ui !<TeX>=</TeX> vi
>   	pj !<TeX>=</TeX> qj
>   	1 <TeX>\leq</TeX> disi, limitj <TeX>\leq</TeX> 10^9
>   	There may be multiple edges between two nodes.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
pub struct DisjointSet {
parents: Vec<usize>,
ranks: Vec<usize>,
count: usize
}

impl DisjointSet {
pub fn new(n: usize) -> Self {
let parents = (0..n).into_iter().collect::<Vec<_>>();
let ranks = vec![1usize; n];
let count = n;
DisjointSet {
parents,
ranks,
count
}
}

pub fn find(&mut self, i: usize) -> usize {
let mut root = self.parents[i];
while root != self.parents[root] {
root = self.parents[root];
}
let mut p = self.parents[i];
while p != self.parents[p] {
let tmp = self.parents[p];
self.parents[p] = root;
p = tmp;
}
root
}

pub fn union(&mut self, i: usize, j: usize) -> bool {
let ip = self.find(i);
let jp = self.find(j);
if ip == jp {
return false;
}
if self.ranks[ip] < self.ranks[jp] {
self.parents[ip] = self.parents[jp];
} else {
self.parents[jp] = self.parents[ip];
if self.ranks[ip] == self.ranks[jp] {
self.ranks[ip] += 1;
}
}
self.count -= 1;
true
}
}
use std::collections::HashMap;
impl Solution {
pub fn distance_limited_paths_exist(n: i32, edge_list: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<bool> {
let mut edge_list = edge_list;
edge_list.sort_by(|a, b| a[2].partial_cmp(&b[2]).unwrap());
//println!("edge_list: {:?}", edge_list);
let mut queries_map: HashMap<(usize, usize, usize), Vec<usize>> = HashMap::new();
for i in 0..queries.len() {
let key = (queries[i][0] as usize, queries[i][1] as usize, queries[i][2] as usize);
if queries_map.contains_key(&key) {
//println!("key: {:?}", key);
queries_map.get_mut(&key).unwrap().push(i);
} else {
queries_map.insert(key, vec![i]);
}
}
let mut queries = queries;
queries.sort_by(|a, b| a[2].partial_cmp(&b[2]).unwrap());
//println!("queries: {:?}", queries);
let n = n as usize;
//vec.sort_by(|a, b| a.partial_cmp(b).unwrap());
let mut disjoint_set = DisjointSet::new(n);
let mut result = vec![false; queries.len()];
let mut start_index = 0usize;
for i in 0..queries.len() {
let start = queries[i][0] as usize;
let end = queries[i][1] as usize;
let limit = queries[i][2] as usize;
for j in start_index..edge_list.len() {
if edge_list[j][2] as usize >= limit {
start_index = j;
break;
}
let k1 = edge_list[j][0] as usize;
let k2 = edge_list[j][1] as usize;
disjoint_set.union(k1, k2);
}
let r = disjoint_set.find(start) == disjoint_set.find(end);
let indices = queries_map.get(&(start, end, limit)).unwrap();
for &w in indices {
result[w] = r;
}
}
result
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_1697() {
assert_eq!(Solution::distance_limited_paths_exist(3, vec![vec![0,1,2],vec![1,2,4],vec![2,0,8],vec![1,0,16]], vec![vec![0,1,2],vec![0,2,5]]), vec![false, true]);
assert_eq!(Solution::distance_limited_paths_exist(3, vec![vec![0,1,2],vec![1,2,4],vec![2,0,8],vec![1,0,16]], vec![vec![0,1,2],vec![0,2,5]]), vec![false, true]);
assert_eq!(Solution::distance_limited_paths_exist(5, vec![
vec![0,3,528],vec![3,0,44],vec![0,2,493],vec![3,4,989],vec![2,1,929],vec![3,0,900],vec![1,2,26],vec![4,0,684],vec![2,1,742],vec![4,0,881],vec![3,0,855],vec![4,2,322],vec![3,1,523],vec![2,1,362],vec![1,3,101],vec![4,0,862],vec![0,2,206],vec![4,1,972],vec![1,2,64],vec![1,0,459],vec![4,3,576],vec![2,1,726],vec![2,4,448],vec![0,1,293],vec![0,4,460],vec![4,2,920],vec![2,0,354],vec![2,0,54],vec![3,1,411],vec![2,4,419],vec![0,3,823],vec![4,1,72],vec![2,3,900],vec![2,0,954],vec![1,3,826],vec![2,3,730],vec![3,0,694]
], vec![
vec![1,3,538],vec![1,2,1033],vec![0,4,366],vec![1,2,877],vec![1,4,939],vec![3,0,1088],vec![2,1,665],vec![2,3,209],vec![3,1,1469],vec![0,3,389],vec![3,0,1086],vec![1,4,1499],vec![0,3,554],vec![3,0,1634],vec![3,4,1216],vec![0,4,1465],vec![2,4,1641],vec![4,1,1271],vec![2,0,1020],vec![3,2,692],vec![3,0,1605],vec![0,4,898],vec![2,0,1573],vec![4,0,1573],vec![3,1,627],vec![4,1,769],vec![0,3,188],vec![1,0,1077],vec![1,2,1564],vec![1,3,1597],vec![1,0,1274],vec![1,4,71],vec![0,2,1544],vec![2,4,1149],vec![4,3,1449],vec![2,1,1716],vec![4,0,1659],vec![2,4,1722],vec![0,1,1761],vec![4,0,1496],vec![1,3,430],vec![2,3,1888],vec![1,4,618],vec![1,2,16],vec![4,2,1132],vec![0,2,233],vec![2,3,1696],vec![0,3,1960],vec![0,2,1070],vec![2,4,1676],vec![3,2,1362],vec![2,0,1066],vec![1,0,711],vec![3,2,286],vec![4,2,386],vec![3,2,1368],vec![4,3,1283],vec![1,3,1041],vec![1,4,1933],vec![1,3,1213],vec![0,4,36],vec![4,2,1148],vec![0,2,1301],vec![1,4,531],vec![0,3,120],vec![4,2,1919],vec![2,1,1503],vec![2,0,471],vec![3,4,922],vec![3,1,1854],vec![4,0,126],vec![1,0,1421],vec![0,1,1902],vec![0,1,214],vec![2,3,303],vec![0,2,677],vec![1,3,1756],vec![1,4,1119],vec![3,2,20],vec![2,1,1932],vec![2,4,1019],vec![1,4,976],vec![1,2,1383],vec![3,1,249],vec![3,0,817],vec![1,0,247],vec![1,4,1168],vec![0,4,1460],vec![1,4,1864],vec![1,2,521],vec![4,1,291],vec![1,3,1714],vec![2,3,1567],vec![3,0,1421],vec![0,1,613],vec![4,2,326],vec![1,4,251],vec![4,2,391],vec![1,4,1244],vec![3,2,764],vec![3,0,766],vec![3,2,337],vec![3,0,1917],vec![1,0,219],vec![2,1,616],vec![0,2,1568],vec![2,1,1952],vec![3,0,1026],vec![1,4,946],vec![1,0,1597],vec![1,3,1151],vec![4,0,1793],vec![3,4,1138],vec![1,2,1030],vec![1,4,640],vec![4,0,1396],vec![3,4,1548],vec![0,4,866],vec![4,2,1331],vec![2,4,490],vec![2,1,1952],vec![2,1,1642],vec![2,4,741],vec![3,1,246],vec![0,3,213],vec![3,1,690],vec![2,0,569],vec![1,4,1847],vec![3,0,118],vec![1,3,1413],vec![4,1,1194],vec![4,0,1975],vec![2,0,1050],vec![4,0,1324],vec![4,3,109],vec![1,4,623],vec![3,1,362],vec![1,4,1797],vec![1,0,430],vec![0,2,1357],vec![2,0,49],vec![2,0,884],vec![0,3,168],vec![3,0,1692],vec![1,3,1118],vec![1,2,1419],vec![0,2,868],vec![0,4,758],vec![2,1,1360],vec![0,4,677],vec![1,2,400],vec![4,0,155],vec![1,2,1234],vec![4,3,1469],vec![4,0,771],vec![0,1,543],vec![0,1,1702],vec![4,3,1713],vec![4,3,930],vec![1,0,1338],vec![1,3,771],vec![3,4,738],vec![3,1,1697],vec![4,0,1859],vec![2,1,720],vec![1,4,13],vec![0,2,1486],vec![4,3,1195],vec![0,1,459],vec![1,2,890],vec![3,0,1932],vec![1,0,673],vec![1,4,914],vec![3,4,670],vec![2,0,110],vec![3,1,1635],vec![0,2,857]
]),
vec![true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,false,true,true,true,true,true,true,true,true,true,true,true,false,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,false,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,false,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,false,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,false,true,true,true,true,true,true,true,true,true,true,true]);

}
}

```

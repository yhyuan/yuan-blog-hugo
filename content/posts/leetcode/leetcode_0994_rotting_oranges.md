---
title: 994. rotting oranges
date: '2022-06-25'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0994 rotting oranges
---



You are given an m x n grid where each cell can have one of three values:



0 representing an empty cell,

1 representing a fresh orange, or

2 representing a rotten orange.



Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)
>   Input: grid <TeX>=</TeX> [[2,1,1],[1,1,0],[0,1,1]]
>   Output: 4
>   Example 2:
>   Input: grid <TeX>=</TeX> [[2,1,1],[0,1,1],[1,0,1]]
>   Output: -1
>   Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
>   Example 3:
>   Input: grid <TeX>=</TeX> [[0,2]]
>   Output: 0
>   Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
**Constraints:**
>   	m <TeX>=</TeX><TeX>=</TeX> grid.length
>   	n <TeX>=</TeX><TeX>=</TeX> grid[i].length
>   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 10
>   	grid[i][j] is 0, 1, or 2.


## Solution
We will use BFS to solve this problem. We add the rotten orange's positions as the starting points and add fresh orange's position in the BFS process. We will return until all fresh oranges are gone. Pay special attention to the corn cases. For example, there is no rotten and fresh orange.


### Python
```python
def orangesRotting(self, grid: List[List[int]]) -> int:
m = len(grid)
n = len(grid[0])
fresh = 0
q = deque()
visited = set()
for i in range(m):
for j in range(n):
if grid[i][j] == 1:
fresh += 1
if grid[i][j] == 2: # rotton
q.append((0, (i, j)))
visited.add((i, j))

if fresh == 0 and len(q) == 0:
return 0
while len(q) > 0:
(steps, (i, j)) = q.popleft()
if grid[i][j] == 1:
fresh -= 1
if fresh == 0:
return steps
diffs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for diff in diffs:
n_i = i + diff[0]
n_j = j + diff[1]
if n_i >= 0 and n_j >= 0 and n_i < m and n_j < n and not (n_i, n_j) in visited:
visited.add((n_i, n_j))
if grid[n_i][n_j] == 1:
q.append((steps + 1, (n_i, n_j)))
return -1
```


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::VecDeque;
impl Solution {
pub fn oranges_rotting(grid: Vec<Vec<i32>>) -> i32 {
let rows = grid.len();
let cols = grid[0].len();
let mut good_count = 0;
//let mut good_count = grid.iter().map(|row| row.iter().filter(|v| v == &&1).sum()).count();
let mut q :VecDeque<(usize, usize)> = VecDeque::new();
let mut visited: Vec<Vec<bool>> = vec![vec![false; cols]; rows];
for i in 0..rows {
for j in 0..cols {
if grid[i][j] == 2 {
q.push_back((i, j));
visited[i][j] = true;
}
if grid[i][j] == 0 {
visited[i][j] = true;
}
if grid[i][j] == 1 {
good_count += 1;
}
}
}
if good_count == 0 {
return 0;
}
let mut step = 1;
while !q.is_empty() {
let count = q.len();
// println!("count: {}, good_count: {}", count, good_count);
for _ in 0..count {
let (i, j) = q.pop_front().unwrap();
let neighbors = vec![(-1, 0), (1, 0), (0, -1), (0, 1)].iter()
.map(|&(dx, dy)| (i as i32 + dx, j as i32 + dy))
.filter(|&(x, y)| x >= 0 && y >= 0 && x < rows as i32 && y < cols as i32 && !visited[x as usize][y as usize])
.map(|(x, y)| (x as usize, y as usize))
.collect::<Vec<_>>();
//println!();
for (x, y) in neighbors {
visited[x][y] = true;
good_count -= 1;
if good_count == 0 {
return step;
}

q.push_back((x, y));
}
}
step += 1;
}
-1
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_994() {
assert_eq!(Solution::oranges_rotting(vec![vec![2,1,1],vec![1,1,0],vec![0,1,1]]), 4);
}
}

```

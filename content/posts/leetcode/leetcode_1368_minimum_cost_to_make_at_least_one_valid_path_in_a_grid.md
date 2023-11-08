---
title: 1368. minimum cost to make at least one valid path in a grid
date: '2022-08-03'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1368 minimum cost to make at least one valid path in a grid
---

 

  Given a m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:

  	1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])

  	2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])

  	3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])

  	4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])

  

  Notice that there could be some invalid signs on the cells of the grid which points outside the grid.

  You will initially start at the upper left cell (0,0). A valid path in the grid is a path which starts from the upper left cell (0,0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path doesn't have to be the shortest.

  You can modify the sign on a cell with cost <TeX>=</TeX> 1. You can modify the sign on a cell one time only.

  Return the minimum cost to make the grid have at least one valid path.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/02/13/grid1.png)

 >   Input: grid <TeX>=</TeX> [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]

 >   Output: 3

 >   Explanation: You will start at point (0, 0).

 >   The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost <TeX>=</TeX> 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost <TeX>=</TeX> 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost <TeX>=</TeX> 1 --> (3, 3)

 >   The total cost <TeX>=</TeX> 3.

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2020/02/13/grid2.png)

 >   Input: grid <TeX>=</TeX> [[1,1,3],[3,2,2],[1,1,4]]

 >   Output: 0

 >   Explanation: You can follow the path from (0, 0) to (2, 2).

  

 >   Example 3:

 >   ![](https://assets.leetcode.com/uploads/2020/02/13/grid3.png)

 >   Input: grid <TeX>=</TeX> [[1,2],[4,3]]

 >   Output: 1

  

 >   Example 4:

  

 >   Input: grid <TeX>=</TeX> [[2,2,2],[2,2,2]]

 >   Output: 3

  

 >   Example 5:

  

 >   Input: grid <TeX>=</TeX> [[4]]

 >   Output: 0

  

   

  **Constraints:**

  

 >   	m <TeX>=</TeX><TeX>=</TeX> grid.length

 >   	n <TeX>=</TeX><TeX>=</TeX> grid[i].length

 >   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 100


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::VecDeque;
impl Solution {
    pub fn min_cost(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut visited: Vec<Vec<bool>> = vec![vec![false; n]; m];
        let mut q: VecDeque<(usize, usize, i32)> = VecDeque::new();
        q.push_back((0, 0, 0));
        let d = vec![(0, 1), (0, -1), (1, 0), (-1, 0)];
        while !q.is_empty() {
            let (x, y, cost) = q.pop_front().unwrap();
            if x == m - 1 && y == n - 1 {
                return cost;
            }
            if visited[x][y] {
                continue;
            }
            visited[x][y] = true;
            for (i, &(dx, dy)) in d.iter().enumerate() {
                let nx = x as i32 + dx;
                let ny = y as i32 + dy;
                if nx < 0 || nx == m as i32 || ny < 0 || ny == n as i32 {
                    continue;
                }
                if i == grid[x][y] as usize - 1 {
                    q.push_front((nx as usize, ny as usize, cost));
                } else {
                    q.push_back((nx as usize, ny as usize, cost + 1));
                }
            }
        }
        -1
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1368() {
        assert_eq!(Solution::min_cost(vec![vec![3,4,3],vec![2,2,2],vec![2,1,1],vec![4,3,2],vec![2,1,4],vec![2,4,1],vec![3,3,3],vec![1,4,2],vec![2,2,1],vec![2,1,1],vec![3,3,1],vec![4,1,4],vec![2,1,4],vec![3,2,2],vec![3,3,1],vec![4,4,1],vec![1,2,2],vec![1,1,1],vec![1,3,4],vec![1,2,1],vec![2,2,4],vec![2,1,3],vec![1,2,1],vec![4,3,2],vec![3,3,4],vec![2,2,1],vec![3,4,3],vec![4,2,3],vec![4,4,4]]), 18);
        assert_eq!(Solution::min_cost(vec![vec![1,1,1,1],vec![2,2,2,2],vec![1,1,1,1],vec![2,2,2,2]]), 3);
        assert_eq!(Solution::min_cost(vec![vec![1,1,3],vec![3,2,2],vec![1,1,4]]), 0);
        assert_eq!(Solution::min_cost(vec![vec![1,2],vec![4,3]]), 1);
    }
}

```

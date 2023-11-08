---
title: 417. pacific atlantic water flow
date: '2022-03-06'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0417 pacific atlantic water flow
---

 

  There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

  The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

  The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

  Return a 2D list of grid coordinates result where result[i] <TeX>=</TeX> [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg)

 >   Input: heights <TeX>=</TeX> [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

 >   Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

  

 >   Example 2:

  

 >   Input: heights <TeX>=</TeX> [[2,1],[1,2]]

 >   Output: [[0,0],[0,1],[1,0],[1,1]]

  

   

  **Constraints:**

  

 >   	m <TeX>=</TeX><TeX>=</TeX> heights.length

 >   	n <TeX>=</TeX><TeX>=</TeX> heights[r].length

 >   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 200

 >   	0 <TeX>\leq</TeX> heights[r][c] <TeX>\leq</TeX> 10^5


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::VecDeque;

impl Solution {
    pub fn helper(heights: &Vec<Vec<i32>>, visited: &mut Vec<Vec<bool>>, top_left: bool) {
        let rows = heights.len();
        let cols = heights[0].len();
        let mut q: VecDeque<(usize, usize)> = VecDeque::new();
        if top_left {
            for i in 0..cols {
                q.push_back((0, i));
            }
            for i in 1..rows {
                q.push_back((i, 0));
            }
        } else {
            for i in 0..cols {
                q.push_back((rows - 1, i));
            }
            for i in 0..rows - 1 {
                q.push_back((i, cols - 1));
            }
        }
        while !q.is_empty() {
            let (i, j) = q.pop_front().unwrap();
            let height = heights[i][j];
            visited[i][j] = true;
            let neighbors = vec![(-1, 0), (1, 0), (0, -1), (0, 1)].iter()
                .map(|&(dx, dy)| (dx + i as i32, dy + j as i32))
                .filter(|&(x, y)| x >= 0 && y >= 0 && x < rows as i32 && y < cols as i32 && heights[x as usize][y as usize] >= height && !visited[x as usize][y as usize])
                .collect::<Vec<_>>();
            for k in 0..neighbors.len() {
                let (x, y) = neighbors[k];
                q.push_back((x as usize, y as usize));
            }
        }
    }
    pub fn pacific_atlantic(heights: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let rows = heights.len();
        let cols = heights[0].len();
        let mut visited_top_left = vec![vec![false; cols]; rows];
        Self::helper(&heights, &mut visited_top_left, true);
        let mut visited_bottom_right = vec![vec![false; cols]; rows];
        Self::helper(&heights, &mut visited_bottom_right, false);
        let mut results: Vec<Vec<i32>> = vec![];
        for i in 0..rows {
            for j in 0..cols {
                if visited_top_left[i][j] && visited_bottom_right[i][j] {
                    results.push(vec![i as i32, j as i32]);
                }
            }
        }
        results
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_417() {
        assert_eq!(Solution::pacific_atlantic(vec![
            vec![1,2,2,3,5],
            vec![3,2,3,4,4],
            vec![2,4,5,3,1],
            vec![6,7,1,4,5],
            vec![5,1,1,2,4]]), 
            vec![
                vec![0,4],
                vec![1,3],
                vec![1,4],
                vec![2,2],
                vec![3,0],
                vec![3,1],
                vec![4,0]]);
    }
}

```

---
title: 317. shortest distance from all buildings
date: '2022-01-07'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0317 shortest distance from all buildings
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={317}/>

You are given an m x n grid grid of values 0, 1, or 2, where:



each 0 marks an empty land that you can pass by freely,

each 1 marks a building that you cannot pass through, and

each 2 marks an obstacle that you cannot pass through.

You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.



Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.



The total travel distance is the sum of the distances between the houses of the friends and the meeting point.



The distance is calculated using Manhattan Distance, where distance(p1, p2) <TeX>=</TeX> |p2.x - p1.x| + |p2.y - p1.y|.



 



 > Example 1:





 > Input: grid <TeX>=</TeX> [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

 > Output: 7

 > Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).

 > The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1<TeX>=</TeX>7 is minimal.

 > So return 7.

 > Example 2:



 > Input: grid <TeX>=</TeX> [[1,0]]

 > Output: 1

 > Example 3:



 > Input: grid <TeX>=</TeX> [[1]]

 > Output: -1

 



**Constraints:**



 > m <TeX>=</TeX><TeX>=</TeX> grid.length

 > n <TeX>=</TeX><TeX>=</TeX> grid[i].length

 > 1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 50

 > grid[i][j] is either 0, 1, or 2.

 > There will be at least one building in the grid.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::VecDeque;
impl Solution {
    pub fn bfs(grid: &Vec<Vec<i32>>, dists: &mut Vec<Vec<i32>>, nums: &mut Vec<Vec<i32>>, i: usize, j: usize) {
        let m = grid.len();
        let n = grid[0].len();
        let neighbor = vec![(1, 0), (-1, 0), (0, 1), (0, -1)];
        let mut queue: VecDeque<(usize, usize)> = VecDeque::new();
        queue.push_back((i, j));
        let mut visited: Vec<Vec<bool>> = vec![vec![false; n]; m];
        let mut dist = 0;
        while !queue.is_empty() {
            dist += 1;
            let size = queue.len();
            for _ in 0..size {
                let (x, y) = queue.pop_front().unwrap();
                //println!("x: {}, y: {}, dist: {}", x, y, dist);
                for &(dx, dy) in neighbor.iter() {
                    let nx = x as i32 + dx;
                    let ny = y as i32 + dy;
                    if nx >= 0 && ny >= 0 && nx < m as i32 && ny < n as i32 && grid[nx as usize][ny as usize] == 0 && !visited[nx as usize][ny as usize] {
                        let nx = nx as usize;
                        let ny = ny as usize;
                        visited[nx][ny] = true;
                        if dists[nx][ny] == i32::MAX {
                            dists[nx][ny] = dist;
                        } else {
                            dists[nx][ny] += dist;
                        }
                        nums[nx][ny] += 1;
                        queue.push_back((nx, ny));
                    }
                }
            }
        }
    }
    pub fn shortest_distance(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();

        let mut dists: Vec<Vec<i32>> = vec![vec![i32::MAX; n]; m];
        let mut nums: Vec<Vec<i32>> = vec![vec![0; n]; m];
        let mut building_count = 0;
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 {
                    building_count += 1;
                    Self::bfs(&grid, &mut dists, &mut nums, i, j);
                    //println!("dists: {:?}", dists);
                }
            }
        }
        let mut res = i32::MAX;
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 0 && dists[i][j] > 0 && nums[i][j] == building_count {
                    res = i32::min(res, dists[i][j]);
                }
            }
        }
        if res == i32::MAX {-1} else {res}
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_317() {
        assert_eq!(Solution::shortest_distance(vec![vec![1,2, 0]]), -1);
        assert_eq!(Solution::shortest_distance(vec![vec![1,0,2,0,1],vec![0,0,0,0,0],vec![0,0,1,0,0]]), 7);
        assert_eq!(Solution::shortest_distance(vec![vec![1,0]]), 1);
        assert_eq!(Solution::shortest_distance(vec![vec![1]]), -1);
    }
}

```

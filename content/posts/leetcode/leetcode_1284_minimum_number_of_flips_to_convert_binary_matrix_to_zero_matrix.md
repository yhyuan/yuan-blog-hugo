---
title: 1284. minimum number of flips to convert binary matrix to zero matrix
date: '2022-07-27'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1284 minimum number of flips to convert binary matrix to zero matrix
---

 

  Given a m x n binary matrix mat. In one step, you can choose one cell and flip it and all the four neighbors of it if they exist (Flip is changing 1 to 0 and 0 to 1). A pair of cells are called neighbors if they share one edge.

  Return the minimum number of steps required to convert mat to a zero matrix or -1 if you cannot.

  A binary matrix is a matrix with all cells equal to 0 or 1 only.

  A zero matrix is a matrix with all cells equal to 0.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2019/11/28/matrix.png)

 >   Input: mat <TeX>=</TeX> [[0,0],[0,1]]

 >   Output: 3

 >   Explanation: One possible solution is to flip (1, 0) then (0, 1) and finally (1, 1) as shown.

  

 >   Example 2:

  

 >   Input: mat <TeX>=</TeX> [[0]]

 >   Output: 0

 >   Explanation: Given matrix is a zero matrix. We don't need to change it.

  

 >   Example 3:

  

 >   Input: mat <TeX>=</TeX> [[1,1,1],[1,0,1],[0,0,0]]

 >   Output: 6

  

 >   Example 4:

  

 >   Input: mat <TeX>=</TeX> [[1,0,0],[1,0,0]]

 >   Output: -1

 >   Explanation: Given matrix can't be a zero matrix

  

   

  **Constraints:**

  

 >   	m <TeX>=</TeX><TeX>=</TeX> mat.length

 >   	n <TeX>=</TeX><TeX>=</TeX> mat[i].length

 >   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 3

 >   	mat[i][j] is either 0 or 1.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
// convert a matrix to a i32 number since 1 <= m, n <= 3
use std::collections::HashSet;
use std::collections::VecDeque;
impl Solution {
    pub fn calculate_next_state(state: i32, m: usize, n: usize, i: usize, j: usize) -> i32 {
        let diffs = vec![(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)];
        let flip_position: Vec<i32> = diffs.iter().map(|&(dx, dy)| (dx + i as i32, dy + j as i32))
            .filter(|&(x, y)| x >= 0 && y >= 0 && x < m as i32 && y < n as i32)
            .map(|(x, y)| (x as usize, y as usize))
            .map(|(x, y)| (x * n + y) as i32)
            .collect();
        let mut res = state;
        for i in 0..flip_position.len() {
            res = res ^ (1 << flip_position[i]);
        }
        res
    }
    pub fn min_flips(mat: Vec<Vec<i32>>) -> i32 {
        let m = mat.len();
        let n = mat[0].len();
        let mut inital_state = 0i32;
        let mut k = 0i32;
        for i in 0..m {
            for j in 0..n {
                if mat[i][j] == 1 {
                    inital_state = inital_state | (1 << k);
                }
                k += 1;
            }
        }
        if inital_state == 0 {
            return 0;
        }
        let mut q: VecDeque<(usize, i32)> = VecDeque::new();
        let mut visited: HashSet<i32> = HashSet::new();
        q.push_back((0, inital_state));
        visited.insert(inital_state);
        while !q.is_empty() {
            let (steps, state) = q.pop_front().unwrap();
            for i in 0..m {
                for j in 0..n {
                    let next_state = Self::calculate_next_state(state, m, n, i, j);
                    if !visited.contains(&next_state) {
                        if next_state == 0i32 {
                            return steps as i32 + 1;
                        }
                        visited.insert(next_state);
                        q.push_back((steps + 1, next_state));
                    }
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
    fn test_1284() {
        assert_eq!(Solution::min_flips(vec![vec![0,0], vec![0,1]]), 3);
        assert_eq!(Solution::min_flips(vec![vec![0]]), 0);
        assert_eq!(Solution::min_flips(vec![vec![1,0,0],vec![1,0,0]]), -1);
    }
}

```

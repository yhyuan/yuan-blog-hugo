---
title: 1263. minimum moves to move a box to their target location
date: '2022-07-26'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1263 minimum moves to move a box to their target location
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1263}/>
 

  A storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.

  The game is represented by an m x n grid of characters grid where each element is a wall, floor, or box.

  Your task is to move the box 'B' to the target position 'T' under the following rules:

  

  	The character 'S' represents the player. The player can move up, down, left, right in grid if it is a floor (empty cell).

  	The character '.' represents the floor which means a free cell to walk.

  	The character '#' represents the wall which means an obstacle (impossible to walk there).

  	There is only one box 'B' and one target cell 'T' in the grid.

  	The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a push.

  	The player cannot walk through the box.

  

  Return the minimum number of pushes to move the box to the target. If there is no way to reach the target, return -1.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2019/11/06/sample_1_1620.png)

 >   Input: grid <TeX>=</TeX> [["#","#","#","#","#","#"],

 >                  ["#","T","#","#","#","#"],

 >                  ["#",".",".","B",".","#"],

 >                  ["#",".","#","#",".","#"],

 >                  ["#",".",".",".","S","#"],

 >                  ["#","#","#","#","#","#"]]

 >   Output: 3

 >   Explanation: We return only the number of times the box is pushed.

 >   Example 2:

  

 >   Input: grid <TeX>=</TeX> [["#","#","#","#","#","#"],

 >                  ["#","T","#","#","#","#"],

 >                  ["#",".",".","B",".","#"],

 >                  ["#","#","#","#",".","#"],

 >                  ["#",".",".",".","S","#"],

 >                  ["#","#","#","#","#","#"]]

 >   Output: -1

  

 >   Example 3:

  

 >   Input: grid <TeX>=</TeX> [["#","#","#","#","#","#"],

 >                  ["#","T",".",".","#","#"],

 >                  ["#",".","#","B",".","#"],

 >                  ["#",".",".",".",".","#"],

 >                  ["#",".",".",".","S","#"],

 >                  ["#","#","#","#","#","#"]]

 >   Output: 5

 >   Explanation:  push the box down, left, left, up and up.

  

 >   Example 4:

  

 >   Input: grid <TeX>=</TeX> [["#","#","#","#","#","#","#"],

 >                  ["#","S","#",".","B","T","#"],

 >                  ["#","#","#","#","#","#","#"]]

 >   Output: -1

  

   

  **Constraints:**

  

 >   	m <TeX>=</TeX><TeX>=</TeX> grid.length

 >   	n <TeX>=</TeX><TeX>=</TeX> grid[i].length

 >   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 20

 >   	grid contains only characters '.', '#', 'S', 'T', or 'B'.

 >   	There is only one character 'S', 'B', and 'T' in the grid.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::cmp::Reverse;
use std::collections::HashSet;
use std::collections::BinaryHeap;
type State = (i32, i32, i32, i32);
impl Solution {
    fn min_push_box(grid: Vec<Vec<char>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut floors: HashSet<(i32, i32)> = HashSet::new();
        let mut state = (0, 0, 0, 0);
        let mut t = (0, 0);
        for i in 0..m {
            for j in 0..n {
                match grid[i][j] {
                    'S' => {
                        state.0 = i as i32;
                        state.1 = j as i32;
                        floors.insert((state.0, state.1));
                    }
                    'B' => {
                        state.2 = i as i32;
                        state.3 = j as i32;
                        floors.insert((state.2, state.3));
                    }
                    'T' => {
                        t = (i as i32, j as i32);
                        floors.insert(t);
                    }
                    '.' => {
                        floors.insert((i as i32, j as i32));
                    }
                    _ => {}
                }
            }
        }
        let mut queue: BinaryHeap<(Reverse<i32>, State)> = BinaryHeap::new();
        queue.push((Reverse(0), state));
        let mut visited: HashSet<State> = HashSet::new();
        visited.insert(state);
        let dirs = vec![(1, 0), (0, 1), (-1, 0), (0, -1)];
        while let Some((Reverse(step), state)) = queue.pop() {
            if (state.2, state.3) == t {
                return step;
            }
            for (di, dj) in &dirs {
                let pi = state.0 + di;
                let pj = state.1 + dj;
                let bi = state.2;
                let bj = state.3;
                if (state.2, state.3) == (pi, pj) {
                    let next_state = (pi, pj, bi + di, bj + dj);
                    if floors.contains(&(bi, bj)) && visited.insert(next_state) {
                        queue.push((Reverse(step + 1), next_state));
                    }
                } else {
                    let next_state = (pi, pj, bi, bj);
                    if floors.contains(&(pi, pj)) && visited.insert(next_state) {
                        queue.push((Reverse(step), next_state));
                    }
                }
            }
        }
        -1
    }
}
/*
use std::collections::VecDeque;
use std::collections::HashSet;
impl Solution {
    pub fn dfs(grid: &Vec<Vec<char>>, reachable: &mut Vec<Vec<bool>>, box_pos: (usize, usize), staff_pos: (usize, usize)) {
        let m = grid.len();
        let n = grid[0].len();
        reachable[staff_pos.0][staff_pos.1] = true;
        let next_staff_positions = vec![(-1, 0), (1, 0), (0, -1), (0, 1)].into_iter()
        .map(|(dx, dy)| (staff_pos.0 as i32 + dx, staff_pos.1 as i32 + dy))
        .filter(|&(x, y)| x >= 0 && y >= 0 && x < m as i32 && y < n as i32)
        .map(|(x,y)| (x as usize, y as usize))
        .filter(|&(x, y)| grid[x][y] != '#' && !reachable[x][y])
        .collect::<Vec<_>>();
        for i in 0..next_staff_positions.len() {
            let next_staff_position = next_staff_positions[i];
            if next_staff_position != box_pos {
                Self::dfs(grid, reachable, box_pos, next_staff_position);
            }
        }
    }
    pub fn find_position(grid: &Vec<Vec<char>>, ch: char) -> (usize, usize) {
        let m = grid.len();
        let n = grid[0].len();
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == ch {
                    return (i, j);
                }
            }
        }
        unreachable!()
    }
    pub fn bfs(grid: &Vec<Vec<char>>, staff_pos: (usize, usize),  box_pos: (usize, usize),  target_pos: (usize, usize)) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut visited: Vec<Vec<bool>> = vec![vec![false; n]; m];
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == '#' {
                    visited[i][j] = true;
                }
            }
        }
        let mut queue: VecDeque<((usize, usize), (usize, usize))> = VecDeque::new();
        queue.push_back((box_pos, staff_pos));
        let mut res = 0;
        while !queue.is_empty() {
            let size = queue.len();
            //println!("res: {}, size: {}", res, size);
            //println!("queue: {:?}", queue);
            for _ in 0..size {
                let (box_position, staff_position) = queue.pop_front().unwrap();
                if box_position == target_pos {
                    return res;
                }
                let mut reachable: Vec<Vec<bool>> = vec![vec![false; n]; m];
                Self::dfs(&grid, &mut reachable, box_position, staff_position);
                visited[box_position.0][box_position.1] = true;
                for (dx, dy) in vec![(-1, 0), (1, 0), (0, -1), (0, 1)] {
                    let x = box_position.0 as i32 + dx;
                    let y = box_position.1 as i32 + dy;
                    if x < 0 || y < 0 || x >= m as i32 || y >= n as i32 || grid[x as usize][y as usize] == '#' {
                        continue;
                    }
                    let x = box_position.0 as i32 - dx;
                    let y = box_position.1 as i32 - dy;
                    if x < 0 || y < 0 || x >= m as i32 || y >= n as i32 || grid[x as usize][y as usize] == '#' {
                        continue;
                    }
                    let next_box_pos = ((box_position.0 as i32 + dx) as usize,  (box_position.1 as i32 + dy) as usize);
                    let next_staff_pos = ((box_position.0 as i32 - dx) as usize,  (box_position.1 as i32 - dy) as usize);
                    if reachable[next_staff_pos.0][next_staff_pos.1] {
                        queue.push_back((next_box_pos, box_position));
                    }
                }
            }
            res += 1;
        }
        -1
    }
    pub fn bfs_staff(grid: &Vec<Vec<char>>, staff_pos: (usize, usize),  box_pos: (usize, usize), next_box_positions: HashSet<(usize, usize)>) -> HashSet<(usize, usize)> {
        let mut valid_next_box_positions: HashSet<(usize, usize)> = HashSet::new();
        let m = grid.len();
        let n = grid[0].len();
        let mut visited: Vec<Vec<bool>> = vec![vec![false; n]; m];
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == '#' {
                    visited[i][j] = true;
                }
            }
        }
        visited[box_pos.0][box_pos.1] = true;
        let mut queue: VecDeque<(usize, usize)> = VecDeque::new();
        queue.push_back(staff_pos);
        while !queue.is_empty() {
            let size = queue.len();
            for _ in 0..size {
                let staff_position = queue.pop_front().unwrap();
                visited[staff_position.0][staff_position.1] = true;
                if next_box_positions.contains(&staff_position) {

                }
            }
        }
        valid_next_box_positions
    }
    pub fn min_push_box(grid: Vec<Vec<char>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let staff_pos = Self::find_position(&grid, 'S');
        let target_pos = Self::find_position(&grid, 'T');
        let box_pos = Self::find_position(&grid, 'B');
        let mut grid = grid;
        grid[target_pos.0][target_pos.1] = '.';
        grid[box_pos.0][box_pos.1] = '.';
        grid[staff_pos.0][staff_pos.1] = '.';
        Self::bfs(&grid, staff_pos,  box_pos,  target_pos)
    }
}
*/
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1263() {

        assert_eq!(Solution::min_push_box(vec![
            vec!['#','#','#','#','#','#'],
            vec!['#','T','#','#','#','#'],
            vec!['#','.','.','B','.','#'],
            vec!['#','.','#','#','.','#'],
            vec!['#','.','.','.','S','#'],
            vec!['#','#','#','#','#','#']]
        ), 3);
        
        assert_eq!(Solution::min_push_box(vec![
            vec!['#','#','#','#','#','#'],
            vec!['#','T','#','#','#','#'],
            vec!['#','.','.','B','.','#'],
            vec!['#','#','#','#','.','#'],
            vec!['#','.','.','.','S','#'],
            vec!['#','#','#','#','#','#']]
        ), -1);
        assert_eq!(Solution::min_push_box(vec![
            vec!['#','#','#','#','#','#'],
            vec!['#','T','.','.','#','#'],
            vec!['#','.','#','B','.','#'],
            vec!['#','.','.','.','.','#'],
            vec!['#','.','.','.','S','#'],
            vec!['#','#','#','#','#','#']]
        ), 5);

        assert_eq!(Solution::min_push_box(vec![
            vec!['#','.','.','#','#','#','#','#'],
            vec!['#','.','.','T','#','.','.','#'],
            vec!['#','.','.','.','#','B','.','#'],
            vec!['#','.','.','.','.','.','.','#'],
            vec!['#','.','.','.','#','.','S','#'],
            vec!['#','.','.','#','#','#','#','#']]
        ), 7);        
    
        assert_eq!(Solution::min_push_box(vec![
            vec!['#','.','.','#','T','#','#','#','#'],
            vec!['#','.','.','#','.','#','.','.','#'],
            vec!['#','.','.','#','.','#','B','.','#'],
            vec!['#','.','.','.','.','.','.','.','#'],
            vec!['#','.','.','.','.','#','.','S','#'],
            vec!['#','.','.','#','.','#','#','#','#']]
        ), 8);

    }
}

```

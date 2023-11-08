---
title: 864. shortest path to get all keys
date: '2022-06-01'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0864 shortest path to get all keys
---

 

  You are given an m x n grid grid where:

  

  	'.' is an empty cell.

  	'#' is a wall.

  	'@' is the starting point.

  	Lowercase letters represent keys.

  	Uppercase letters represent locks.

  

  You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

  If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

  For some 1 <TeX>\leq</TeX> k <TeX>\leq</TeX> 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

  Return the lowest number of moves to acquire all keys. If it is impossible, return -1.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/07/23/lc-keys2.jpg)

 >   Input: grid <TeX>=</TeX> ["@.a.#","###.#","b.A.B"]

 >   Output: 8

 >   Explanation: Note that the goal is to obtain all the keys not to open all the locks.

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2021/07/23/lc-key2.jpg)

 >   Input: grid <TeX>=</TeX> ["@..aA","..B#.","....b"]

 >   Output: 6

  

 >   Example 3:

 >   ![](https://assets.leetcode.com/uploads/2021/07/23/lc-keys3.jpg)

 >   Input: grid <TeX>=</TeX> ["@Aa"]

 >   Output: -1

  

   

  **Constraints:**

  

 >   	m <TeX>=</TeX><TeX>=</TeX> grid.length

 >   	n <TeX>=</TeX><TeX>=</TeX> grid[i].length

 >   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 30

 >   	grid[i][j] is either an English letter, '.', '#', or '@'.

 >   	The number of keys in the grid is in the range [1, 6].

 >   	Each key in the grid is unique.

 >   	Each key in the grid has a matching lock.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
use std::collections::VecDeque;
impl Solution {
    pub fn bfs(grid: &mut Vec<Vec<char>>, hashmap: &HashMap<char, (usize, usize)>, pos: (usize, usize), keys: usize) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        if keys == 0 {
            return 0i32;
        }
        let mut visited = vec![vec![false; n]; m];
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == '#' || (grid[i][j] >= 'A' && grid[i][j] <= 'Z') {
                    visited[i][j] = true;
                }
            }
        }
        let mut q: VecDeque<(usize, usize)> = VecDeque::new();
        visited[pos.0][pos.1] = true;
        q.push_back(pos);
        let mut key_positions: Vec<((usize, usize), i32)> = vec![];
        let mut step = 0;
        while !q.is_empty() {
            let size = q.len();
            for _ in 0..size {
                let (x, y) = q.pop_front().unwrap();
                if grid[x][y] >= 'a' && grid[x][y] <= 'z' {
                    key_positions.push(((x, y), step));
                }
                let neighbors = vec![(-1, 0), (1, 0), (0, -1), (0, 1)].into_iter()
                    .map(|(dx, dy)| (x as i32 + dx, y as i32 + dy))
                    .filter(|&(x, y)| x >= 0 && y >= 0 && x < m as i32 && y < n as i32 && !visited[x as usize][y as usize])
                    .collect::<Vec<_>>();
                for i in 0..neighbors.len() {
                    let nx = neighbors[i].0 as usize;
                    let ny = neighbors[i].1 as usize;
                    visited[nx][ny] = true;
                    q.push_back((nx, ny));
                }                
            }
            step += 1;
        }
        //println!("key_positions: {:?}", key_positions);
        let mut res = i32::MAX;
        for i in 0..key_positions.len() {
            let (key_position, step) = key_positions[i];
            let key_letter = grid[key_position.0][key_position.1];
            let lock_letters: Vec<char> = key_letter.to_uppercase().collect::<Vec<_>>();
            let lock_letter = lock_letters[0];
            let lock_pos = hashmap.get(&lock_letter).unwrap();
            grid[lock_pos.0][lock_pos.1] = '.';
            grid[key_position.0][key_position.1] = '.';
            let result = Self::bfs(grid, hashmap, key_position, keys - 1);
            if result < i32::MAX {
                res = i32::min(res, result + step);
            }
            grid[lock_pos.0][lock_pos.1] = lock_letter;
            grid[key_position.0][key_position.1] = key_letter;
        }
        res
    }
    pub fn shortest_path_all_keys(grid: Vec<String>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut grid: Vec<Vec<char>> = grid.into_iter().map(|s| s.chars().collect::<Vec<_>>()).collect();
        let mut hashmap: HashMap<char, (usize, usize)> = HashMap::new();
        let mut starting_pos = (usize::MAX, usize::MAX);
        for i in 0..m {
            for j in 0..n {
                if (grid[i][j] >= 'a' && grid[i][j] <= 'z') || (grid[i][j] >= 'A' && grid[i][j] <= 'Z') {
                    hashmap.insert(grid[i][j], (i, j));
                }
                if grid[i][j] == '@' {
                    starting_pos = (i, j);
                }
            }
        }
        let keys = hashmap.len() / 2;
        let res = Self::bfs(&mut grid, &hashmap, starting_pos, keys);
        if res == i32::MAX {-1} else {res}
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_864() {
        /*
        assert_eq!(Solution::shortest_path_all_keys(vec_string!["@.a.#","###.#","b.A.B"]), 8);
        assert_eq!(Solution::shortest_path_all_keys(vec_string!["@..aA","..B#.","....b"]), 6);
        assert_eq!(Solution::shortest_path_all_keys(vec_string!["@Aa"]), -1);
        */
        assert_eq!(Solution::shortest_path_all_keys(vec_string!["@abcdeABCDEFf"]), -1);
    }
}

```

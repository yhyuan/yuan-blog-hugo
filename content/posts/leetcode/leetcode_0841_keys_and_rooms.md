---
title: 841. keys and rooms
date: '2022-05-26'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0841 keys and rooms
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={841}/>
 

  There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

  When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

  Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

   

 >   Example 1:

  

 >   Input: rooms <TeX>=</TeX> [[1],[2],[3],[]]

 >   Output: true

 >   Explanation: 

 >   We visit room 0 and pick up key 1.

 >   We then visit room 1 and pick up key 2.

 >   We then visit room 2 and pick up key 3.

 >   We then visit room 3.

 >   Since we were able to visit every room, we return true.

  

 >   Example 2:

  

 >   Input: rooms <TeX>=</TeX> [[1,3],[3,0,1],[2],[0]]

 >   Output: false

 >   Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.

  

   

  **Constraints:**

  

 >   	n <TeX>=</TeX><TeX>=</TeX> rooms.length

 >   	2 <TeX>\leq</TeX> n <TeX>\leq</TeX> 1000

 >   	0 <TeX>\leq</TeX> rooms[i].length <TeX>\leq</TeX> 1000

 >   	1 <TeX>\leq</TeX> sum(rooms[i].length) <TeX>\leq</TeX> 3000

 >   	0 <TeX>\leq</TeX> rooms[i][j] < n

 >   	All the values of rooms[i] are unique.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn dfs(rooms: &Vec<Vec<i32>>, visited: &mut Vec<bool>, room: usize) {
        visited[room] = true;
        let keys = &rooms[room];
        for i in 0..keys.len() {
            if visited[keys[i] as usize] {
                continue;
            }
            Self::dfs(rooms, visited, keys[i] as usize);
        }
    }

    pub fn can_visit_all_rooms(rooms: Vec<Vec<i32>>) -> bool {
        let n = rooms.len();
        let mut visited: Vec<bool> = vec![false; n];
        Self::dfs(&rooms, &mut visited, 0);
        for i in 0..n {
            if !visited[i] {
                return false;
            }
        }
        true
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_841() {
        assert_eq!(Solution::can_visit_all_rooms(vec![vec![1,3],vec![3,0,1],vec![2],vec![0]]), false);
        assert_eq!(Solution::can_visit_all_rooms(vec![vec![1],vec![2],vec![3],vec![]]), true);
    }
}

```

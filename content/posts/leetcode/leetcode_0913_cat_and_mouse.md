---
title: 913. cat and mouse
date: '2022-06-08'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0913 cat and mouse
---



A game on an undirected graph is played by two players, Mouse and Cat, who alternate turns.

The graph is given as follows: graph[a] is a list of all nodes b such that ab is an edge of the graph.

The mouse starts at node 1 and goes first, the cat starts at node 2 and goes second, and there is a hole at node 0.

During each player's turn, they must travel along one edge of the graph that meets where they are.  For example, if the Mouse is at node 1, it must travel to any node in graph[1].

Additionally, it is not allowed for the Cat to travel to the Hole (node 0.)

Then, the game can end in three ways:



If ever the Cat occupies the same node as the Mouse, the Cat wins.

If ever the Mouse reaches the Hole, the Mouse wins.

If ever a position is repeated (i.e., the players are in the same position as a previous turn, and it is the same player's turn to move), the game is a draw.



Given a graph, and assuming both players play optimally, return



1 if the mouse wins the game,

2 if the cat wins the game, or

0 if the game is a draw.





>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2020/11/17/cat1.jpg)
>   Input: graph <TeX>=</TeX> [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
>   Output: 0
>   Example 2:
>   ![](https://assets.leetcode.com/uploads/2020/11/17/cat2.jpg)
>   Input: graph <TeX>=</TeX> [[1,3],[0],[3],[0,2]]
>   Output: 1
**Constraints:**
>   	3 <TeX>\leq</TeX> graph.length <TeX>\leq</TeX> 50
>   	1 <TeX>\leq</TeX> graph[i].length < graph.length
>   	0 <TeX>\leq</TeX> graph[i][j] < graph.length
>   	graph[i][j] !<TeX>=</TeX> i
>   	graph[i] is unique.
>   	The mouse and the cat can always move.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::{HashSet, HashMap};
type State = (usize, usize, bool);
impl Solution {
pub fn get_next_states(graph: &Vec<HashSet<usize>>, state: State) -> Vec<State> {
if state.2 { // mouse move
graph[state.0].iter()
.map(|&neighbor| (neighbor, state.1, false)).collect::<Vec<_>>()
} else { //cat move
graph[state.1].iter()
.filter(|&neighbor| neighbor != &0)// cat can not go to 0
.map(|&neighbor| (state.0, neighbor, true)).collect::<Vec<_>>()
}
}
pub fn dfs(graph: &Vec<HashSet<usize>>, memo: &mut HashMap<State, i32>, visited: &mut HashSet<State>, state: State) -> i32 {
if state.0 == state.1 {
return 2;
}
if state.0 == 0 {
return 1;
}
if visited.contains(&state) {
return 0;
}
if memo.contains_key(&state) {
return memo[&state];
}
visited.insert(state);
let next_states = Self::get_next_states(&graph, state);
//println!("state: {:?}, next_states: {:?}", state, next_states);
let results = next_states.iter().map(|&state| Self::dfs(graph, memo, visited, state)).collect::<Vec<_>>();
let mouse_can_win = results.iter().find(|&r| r == &1).is_some();
let cat_can_win = results.iter().find(|&r| r == &2).is_some();
let can_draw = results.iter().find(|&r| r == &0).is_some();
//println!("state: {:?}, next_states: {:?}", state, next_states);
visited.remove(&state);
let res = if state.2 { // mouse move
if mouse_can_win {
1
} else if can_draw {
0
} else {
2
}
} else { //cat move
if cat_can_win {
2
} else if can_draw {
0
} else {
1
}
};
//println!("state: {:?}, next_states: {:?}, results:{:?}, res: {}", state, next_states, results, res);
memo.insert(state, res);
res
}
pub fn cat_mouse_game(graph: Vec<Vec<i32>>) -> i32 {
let n = graph.len();
let mut g: Vec<HashSet<usize>> = vec![HashSet::new(); n];
for i in 0..n {
for &j in graph[i].iter() {
g[i].insert(j as usize);
g[j as usize].insert(i);
}
}
let init_state: State = (1, 2, true); // mouse postion, cat position, is mouse move now?
let mut memo: HashMap<State, i32> = HashMap::new();
let mut visited: HashSet<State> = HashSet::new();
Self::dfs(&g, &mut memo, &mut visited, init_state)
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_913() {
//assert_eq!(Solution::cat_mouse_game(vec![vec![2,5],vec![3],vec![0,4,5],vec![1,4,5],vec![2,3],vec![0,2,3]]), 0);
//assert_eq!(Solution::cat_mouse_game(vec![vec![1,3],vec![0],vec![3],vec![0,2]]), 1);
// A bug.
assert_eq!(Solution::cat_mouse_game(vec![vec![5,6],vec![3,4],vec![6],vec![1,4,5],vec![1,3,5],vec![0,3,4,6],vec![0,2,5]]), 2);
}
}


```

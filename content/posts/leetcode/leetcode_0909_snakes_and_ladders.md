---
title: 909. snakes and ladders
date: '2022-06-07'
tags: ['leetcode', 'rust', 'python', 'medium']
draft: false
description: Solution for leetcode 0909 snakes and ladders
---



You are given an n x n integer matrix board where the cells are labeled from 1 to n^2 in a [Boustrophedon style](https://en.wikipedia.org/wiki/Boustrophedon) starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:



Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n^2)].



This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.





If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.

The game ends when you reach the square n^2.



A board square on row r and column c has a snake or ladder if board[r][c] !<TeX>=</TeX> -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n^2 do not have a snake or ladder.

Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.



For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.



Return the least number of moves required to reach the square n^2. If it is not possible to reach the square, return -1.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2018/09/23/snakes.png)
>   Input: board <TeX>=</TeX> [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
>   Output: 4
>   Explanation:
>   In the beginning, you start at square 1 (at row 5, column 0).
>   You decide to move to square 2 and must take the ladder to square 15.
>   You then decide to move to square 17 and must take the snake to square 13.
>   You then decide to move to square 14 and must take the ladder to square 35.
>   You then decide to move to square 36, ending the game.
>   This is the lowest possible number of moves to reach the last square, so return 4.
>   Example 2:
>   Input: board <TeX>=</TeX> [[-1,-1],[-1,3]]
>   Output: 1
**Constraints:**
>   	n <TeX>=</TeX><TeX>=</TeX> board.length <TeX>=</TeX><TeX>=</TeX> board[i].length
>   	2 <TeX>\leq</TeX> n <TeX>\leq</TeX> 20
>   	grid[i][j] is either -1 or in the range [1, n^2].
>   	The squares labeled 1 and n^2 do not have any ladders or snakes.


## Solution


### Python
```python
class Solution:
def snakesAndLadders(self, board: List[List[int]]) -> int:
def buildIdLookupDict(board):
lookupDict = {}
m = len(board)
n = len(board[0])
reverse = False
id = 1
for i in range(m - 1, -1, -1):
colIndex = reversed(range(n)) if reverse else range(n)
for j in colIndex:
lookupDict[(i, j)] = id
id += 1
reverse = not reverse
return lookupDict
lookupDict = buildIdLookupDict(board)
def buildSnakesAndLadders(board, lookupDict):
m = len(board)
n = len(board[0])
ans = {}
for i in range(m):
for j in range(n):
if board[i][j] != -1:
id = lookupDict[(i, j)]
ans[id] = board[i][j]
return ans
snakesAndLadders = buildSnakesAndLadders(board, lookupDict)

def findNeighbors(id, snakesAndLadders):
ans = []
for i in range(1, 7):
if id + i in snakesAndLadders:
ans.append(snakesAndLadders[id + i])
else:
ans.append(id + i)
return ans

q = deque([(0, 1)])
visited = set([1])
m = len(board)
n = len(board[0])
while len(q) > 0:
(steps, id) = q.popleft()
if id == m * n:
return steps
neighbors = findNeighbors(id, snakesAndLadders)
for neighbor in neighbors:
if not neighbor in visited:
visited.add(neighbor)
q.append((steps + 1, neighbor))
return -1
```


### Rust
```rust
use std::collections::VecDeque;
use std::collections::HashMap;
// use std::collections::BinaryHeap;
pub struct Solution {}


// submission codes start here
/*
class Solution:
def snakesAndLadders(self, board: List[List[int]]) -> int:
rows = len(board)
total_square = rows*rows

def next_square(step):
quot, rem = divmod(step-1, rows)
row = (rows - 1) - quot
if row%2 != rows%2:
col = rem
else:
col = (rows - 1) - rem
return row, col

dist = {1: 0} #square and step
queue = collections.deque([1])
while queue:
square = queue.popleft()
if square == total_square:
return dist[square]
for new_square in range(square+1, min(square+6, total_square) + 1):
r, c = next_square(new_square)
if board[r][c] != -1:
new_square = board[r][c]
if new_square not in dist:
dist[new_square] = dist[square] + 1
queue.append(new_square)
return -1
*/
impl Solution {
pub fn calculate_row_col(step: usize, rows: usize) -> (usize, usize) {
let quot = (step - 1) / rows;
let rem = (step - 1) % rows;
let row = (rows - 1) - quot;
let col = if row % 2 != rows % 2 {
rem
} else {
rows - 1 - rem
};
return (row, col);
}

pub fn snakes_and_ladders(board: Vec<Vec<i32>>) -> i32 {
let rows = board.len();
let total_square = rows * rows;
let mut dist: HashMap<usize, usize> = HashMap::new(); // HashMap::new();
dist.insert(1, 0);
let mut queue: VecDeque<usize> = VecDeque::with_capacity(rows * rows);
queue.push_back(1);
while let Some(square) = queue.pop_front() {
if square == total_square {
return dist[&square] as i32;
}
for new_square in square + 1..=usize::min(square + 6, total_square) {
let mut neighbor = new_square;
let (row, col) = Solution::calculate_row_col(neighbor, rows);
if board[row][col] != -1 {
neighbor = (board[row][col]) as usize;
}
if !dist.contains_key(&neighbor) {
dist.insert(neighbor, dist[&square] + 1);
queue.push_back(neighbor);
}
}
}
return -1;
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_909() {
let board = vec![vec![-1,-1,-1,-1,-1,-1],vec![-1,-1,-1,-1,-1,-1],vec![-1,-1,-1,-1,-1,-1],vec![-1,35,-1,-1,13,-1],vec![-1,-1,-1,-1,-1,-1],vec![-1,15,-1,-1,-1,-1]];
assert_eq!(Solution::snakes_and_ladders(board), 4);
let board = vec![vec![-1,-1],vec![-1,3]];
assert_eq!(Solution::snakes_and_ladders(board), 1);
let board = vec![vec![1,1,-1],vec![1,1,1],vec![-1,1,1]];
assert_eq!(Solution::snakes_and_ladders(board), -1);
let board = vec![
vec![-1,-1,-1,30,-1,144,124,135,-1,-1,-1,-1,-1],
vec![-1,-1,-1,-1,-1,-1,167,93,-1,-1,-1,-1,-1],
vec![-1,-1,-1,-1,-1,-1,-1,77,-1,-1,90,-1,-1],
vec![-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
vec![-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,122,-1],
vec![-1,-1,-1,23,-1,-1,-1,-1,-1,155,-1,-1,-1],
vec![-1,-1,140,29,-1,-1,-1,-1,-1,-1,-1,-1,-1],
vec![-1,-1,-1,-1,-1,115,-1,-1,-1,109,-1,-1,5],
vec![-1,57,-1,99,121,-1,-1,132,-1,-1,-1,-1,-1],
vec![-1,48,-1,-1,-1,68,-1,-1,-1,-1,31,-1,-1],
vec![-1,163,147,-1,77,-1,-1,114,-1,-1,80,-1,-1],
vec![-1,-1,-1,-1,-1,57,28,-1,-1,129,-1,-1,-1],
vec![-1,-1,-1,-1,-1,-1,-1,-1,-1,87,-1,-1,-1]];
assert_eq!(Solution::snakes_and_ladders(board), 6);
}
}

```

---
title: 348. Design Tic-Tac-Toe
date: '2022-01-19'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 0348. Design Tic-Tac-Toe
---

 Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

A move is guaranteed to be valid and is placed on an empty block.

Once a winning condition is reached, no more moves are allowed.

A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

Implement the TicTacToe class:

TicTacToe(int n) Initializes the object the size of the board n.

int move(int row, int col, int player) Indicates that the player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move.

Example 1:

Input
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
Output

[null, 0, 0, 0, 0, 0, 0, 1]

Explanation 
```
TicTacToe ticTacToe = new TicTacToe(3);
Assume that player 1 is "X" and player 2 is "O" in the board.
ticTacToe.move(0, 0, 1); // return 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

ticTacToe.move(0, 2, 2); // return 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

ticTacToe.move(2, 2, 1); // return 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

ticTacToe.move(1, 1, 2); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

ticTacToe.move(2, 0, 1); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

ticTacToe.move(1, 0, 2); // return 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
```

Constraints:

2 <TeX>\leq</TeX> n <TeX>\leq</TeX> 100

player is 1 or 2.

0 <TeX>\leq</TeX> row, col < n

(row, col) are unique for each different call to move.

At most n2 calls will be made to move.

Follow-up: Could you do better than O(n2) per move() operation?

## Python
### Python
```python
class TicTacToe:

    def __init__(self, n: int):
        # self.board = [["" for i in range(n)] for j in range(n)]
        self.rowsCount = [{"X": 0, "O": 0} for i in range(n)]
        self.columsCount = [{"X": 0, "O": 0} for i in range(n)]
        self.crossCount = {"X": 0, "O": 0}
        self.antiCrossCount = {"X": 0, "O": 0}
        
    def checkState(self):
        # 0 we 
        # print(self.board)
        n = len(self.rowsCount)
        for i in range(n):
            if self.rowsCount[i]["X"] == n:
                return 1
            if self.rowsCount[i]["O"] == n:
                return 2
            if self.columsCount[i]["X"] == n:
                return 1
            if self.columsCount[i]["O"] == n:
                return 2
        if self.crossCount["X"] == n:
            return 1
        if self.crossCount["O"] == n:
            return 2
        if self.antiCrossCount["X"] == n:
            return 1
        if self.antiCrossCount["O"] == n:
            return 2
        return 0

    def move(self, row: int, col: int, player: int) -> int:
        n = len(self.rowsCount)
        # if row < 0 or row >= n or col < 0 or col >= n or self.board[row][col] != ""
        if player == 1:
            self.rowsCount[row]["X"] += 1
            self.columsCount[col]["X"] += 1
            if row == col:
                self.crossCount["X"] += 1
            if row == n - 1 - col:
                self.antiCrossCount["X"] += 1
        else:
            self.rowsCount[row]["O"] += 1
            self.columsCount[col]["O"] += 1
            if row == col:
                self.crossCount["O"] += 1
            if row == n - 1 - col:
                self.antiCrossCount["O"] += 1
        
        return self.checkState()


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

```

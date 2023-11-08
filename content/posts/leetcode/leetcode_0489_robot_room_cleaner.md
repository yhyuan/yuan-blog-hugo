---
title: 489. Robot Room Cleaner
date: '2022-07-28'
tags: ['leetcode', 'python', 'hard']
draft: false
description: Solution for leetcode 489. Robot Room Cleaner
---


You are controlling a robot that is located somewhere in a room. The room is modeled as an m x n binary grid where 0 represents a wall and 1 represents an empty slot.

The robot starts at an unknown location in the room that is guaranteed to be empty, and you do not have access to the grid, but you can move the robot using the given API Robot.

You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room). The robot with the four given APIs can move forward, turn left, or turn right. Each turn is 90 degrees.

When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell.

Design an algorithm to clean the entire room using the following APIs:
```
interface Robot {
// returns true if next cell is open and robot moves into the cell.
// returns false if next cell is obstacle and robot stays on the current cell.
boolean move();

// Robot will stay on the same cell after calling turnLeft/turnRight.
// Each turn will be 90 degrees.
void turnLeft();
void turnRight();

// Clean the current cell.
void clean();
}
```
Note that the initial direction of the robot will be facing up. You can assume all four edges of the grid are all surrounded by a wall.



Custom testing:

The input is only given to initialize the room and the robot's position internally. You must solve this problem "blind,folded". In other words, you must control the robot using only the four mentioned APIs without knowing the room layout and the initial robot's position.



> Example 1:
> Input: room = [[1,1,1,1,1,0,1,1],[1,1,1,1,1,0,1,1],[1,0,1,1,1,1,1,1],[0,0,0,1,0,0,0,0],[1,1,1,1,1,1,1,1]], row = 1, col = 3
> Output: Robot cleaned all rooms.
> Explanation: All grids in the room are marked by either 0 or 1.
> 0 means the cell is blocked, while 1 means the cell is accessible.
> The robot initially starts at the position of row=1, col=3.
> From the top left corner, its position is one row below and three columns right.
> Example 2:
> Input: room = [[1]], row = 0, col = 0
> Output: Robot cleaned all rooms.
**Constraints:**
> m <TeX>==</TeX> room.length
> n <TeX>==</TeX> room[i].length
> 1 <TeX>\leq</TeX> m <TeX>\leq</TeX> 100
> 1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 200
> room[i][j] is either 0 or 1.
> 0 <TeX>\leq</TeX> row < m
> 0 <TeX>\leq</TeX> col < n
> room[row][col] <TeX>==</TeX> 1
> All the empty cells can be visited from the starting position.


## Solution
Let's firstly build a coordinate system. The original position of the robot is assumed to be (0, 0). Meanwhile, we can use number 0, 1, 2, 3 to represent the robot's direction in up, right, down, and left. Obviously, we can use (x, y, direction) to represent the state of the robot. So the initial state of robot will be (0, 0, 0).

At each state, the robot has three choices.

It can move forward in current direction. It may fail if it can move forward in current direction.

It can turn left.  new_direction = (direction + 4 - 1) % 4 # we add 4 to deal with corn case that direction = 0.

It can turn right.  new_direction = (direction + 1) % 4

If the current state of robot is (x, y, direction) and the robot move, the next position can be found by the following function.



### Python
```python
def next_position(x, y, direction):
if direction == 0: # North
new_x = x - 1
new_y = y
elif direction == 1: # East
new_x = x
new_y = y + 1
elif direction == 2: # South
new_x = x + 1
new_y = y
elif direction == 3: # West
new_x = x
new_y = y - 1
return (new_x, new_y)
```
Then, we can use DFS to search all possible states. We need to define an initial state: (0, 0, 0), a Set: visited to record the state the robot has visited, and a set: cleaned to record the position the robot has cleaned.

we can define the following function:

```python
def cleanRoomHelper(robot, state, visited, cleaned):


# robot move forward
next_state = next_position(state)
if not next_state in visited:
success = robot.move()
if success:
visited.add(next_state)
if not cleaned:
robot.clean()
cleaned.add(next_x, next_y)
cleanRoomHelper(robot, next_state, visited, cleaned)


# make sure robot return the state before move
robot.turnLeft()
robot.turnLeft()
robot.move()
robot.turnRight()
robot.turnRight()


# robot turn left
next_state = turn_left(state)
if not next_state in visited:
visited.add(next_state)
robot.turnLeft()
cleanRoomHelper(robot, next_state, visited, cleaned)


# robot need to return the state before turn
robot.turnRight()



# robot turn right
next_state = right(state)
if not next_state in visited:
visited.add(next_state)
robot.turnRight()
cleanRoomHelper(robot, next_state, visited, cleaned)


# robot need to return the state before turn
robot.turnLeft()
return
```
Finally, we can convert the pseudo code to Python code:

```python
class Solution:
def cleanRoom(self, robot):
"""
:type robot: Robot
:rtype: None
"""


#stack = []
def next_position(x, y, direction):
if direction == 0: # North
new_x = x - 1
new_y = y
elif direction == 1: # East
new_x = x
new_y = y + 1
elif direction == 2: # South
new_x = x + 1
new_y = y
elif direction == 3: # West
new_x = x
new_y = y - 1
return (new_x, new_y)

def cleanRoomHelper(robot, state, visited, cleaned):
(x, y, direction) = state
(next_x, next_y) = next_position(x, y, direction)
if not (next_x, next_y, direction) in visited:
success = robot.move()
if success:
visited.add((next_x, next_y, direction))
if not (next_x, next_y) in cleaned:
robot.clean()
cleaned.add((next_x, next_y))
cleanRoomHelper(robot, (next_x, next_y, direction), visited, cleaned)


# reset Robot back to origin state
robot.turnLeft()
robot.turnLeft()
robot.move()
robot.turnLeft()
robot.turnLeft()
turn_left_state = (x, y, (direction + 4 - 1) % 4)
if not turn_left_state in visited:
visited.add(turn_left_state)
robot.turnLeft()
cleanRoomHelper(robot, turn_left_state, visited, cleaned)
robot.turnRight() # return to initial state
turn_right_state = (x, y, (direction + 1) % 4)
if not turn_right_state in visited:
visited.add(turn_right_state)
robot.turnRight()
cleanRoomHelper(robot, turn_right_state, visited, cleaned)
robot.turnLeft() # return to initial state



# state: (x, y, direction)
visited = set([(0, 0, 0)])
cleaned = set([(0, 0)])
robot.clean()
cleanRoomHelper(robot, (0, 0, 0), visited, cleaned)
return

```

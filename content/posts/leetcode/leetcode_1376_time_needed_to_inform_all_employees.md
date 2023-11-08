---
title: 1376. time needed to inform all employees
date: '2022-08-04'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 1376 time needed to inform all employees
---



A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] <TeX>=</TeX> -1. Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.



>   Example 1:
>   Input: n <TeX>=</TeX> 1, headID <TeX>=</TeX> 0, manager <TeX>=</TeX> [-1], informTime <TeX>=</TeX> [0]
>   Output: 0
>   Explanation: The head of the company is the only employee in the company.
>   Example 2:
>   ![](https://assets.leetcode.com/uploads/2020/02/27/graph.png)
>   Input: n <TeX>=</TeX> 6, headID <TeX>=</TeX> 2, manager <TeX>=</TeX> [2,2,-1,2,2,2], informTime <TeX>=</TeX> [0,0,1,0,0,0]
>   Output: 1
>   Explanation: The head of the company with id <TeX>=</TeX> 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
>   The tree structure of the employees in the company is shown.
>   Example 3:
>   ![](https://assets.leetcode.com/uploads/2020/02/28/1730_example_3_5.PNG)
>   Input: n <TeX>=</TeX> 7, headID <TeX>=</TeX> 6, manager <TeX>=</TeX> [1,2,3,4,5,6,-1], informTime <TeX>=</TeX> [0,6,5,4,3,2,1]
>   Output: 21
>   Explanation: The head has id <TeX>=</TeX> 6. He will inform employee with id <TeX>=</TeX> 5 in 1 minute.
>   The employee with id <TeX>=</TeX> 5 will inform the employee with id <TeX>=</TeX> 4 in 2 minutes.
>   The employee with id <TeX>=</TeX> 4 will inform the employee with id <TeX>=</TeX> 3 in 3 minutes.
>   The employee with id <TeX>=</TeX> 3 will inform the employee with id <TeX>=</TeX> 2 in 4 minutes.
>   The employee with id <TeX>=</TeX> 2 will inform the employee with id <TeX>=</TeX> 1 in 5 minutes.
>   The employee with id <TeX>=</TeX> 1 will inform the employee with id <TeX>=</TeX> 0 in 6 minutes.
>   Needed time <TeX>=</TeX> 1 + 2 + 3 + 4 + 5 + 6 <TeX>=</TeX> 21.
>   Example 4:
>   Input: n <TeX>=</TeX> 15, headID <TeX>=</TeX> 0, manager <TeX>=</TeX> [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime <TeX>=</TeX> [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
>   Output: 3
>   Explanation: The first minute the head will inform employees 1 and 2.
>   The second minute they will inform employees 3, 4, 5 and 6.
>   The third minute they will inform the rest of employees.
>   Example 5:
>   Input: n <TeX>=</TeX> 4, headID <TeX>=</TeX> 2, manager <TeX>=</TeX> [3,3,-1,2], informTime <TeX>=</TeX> [0,0,162,914]
>   Output: 1076
**Constraints:**
>   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 10^5
>   	0 <TeX>\leq</TeX> headID < n
>   	manager.length <TeX>=</TeX><TeX>=</TeX> n
>   	0 <TeX>\leq</TeX> manager[i] < n
>   	manager[headID] <TeX>=</TeX><TeX>=</TeX> -1
>   	informTime.length <TeX>=</TeX><TeX>=</TeX> n
>   	0 <TeX>\leq</TeX> informTime[i] <TeX>\leq</TeX> 1000
>   	informTime[i] <TeX>=</TeX><TeX>=</TeX> 0 if employee i has no subordinates.
>   	It is guaranteed that all the employees can be informed.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::VecDeque;
impl Solution {
pub fn num_of_minutes(n: i32, head_id: i32, manager: Vec<i32>, inform_time: Vec<i32>) -> i32 {
let n = n as usize;
let mut graph: Vec<Vec<usize>> = vec![vec![]; n];
for i in 0..n {
if  manager[i] == -1 {
continue;
}
graph[ manager[i] as usize].push(i);
}
let mut q: VecDeque<(usize, usize)> = VecDeque::new();
q.push_back((head_id as usize, 0));
let mut result = i32::MIN;
while !q.is_empty() {
let (index, time) = q.pop_front().unwrap();
result = i32::max(time as i32, result);
let inform_time_index = inform_time[index] as usize;
for i in 0..graph[index].len() {
let v = graph[index][i];
q.push_back((v, time + inform_time_index));
}
}
result
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_1376() {
assert_eq!(Solution::num_of_minutes(6, 2, vec![2,2,-1,2,2,2], vec![0,0,1,0,0,0]), 1);
}
}

```

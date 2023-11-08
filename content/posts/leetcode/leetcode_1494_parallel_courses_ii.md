---
title: 1494. parallel courses ii
date: '2022-08-10'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1494 parallel courses ii
---



You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] <TeX>=</TeX> [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei. Also, you are given the integer k.

In one semester, you can take at most k courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.

Return the minimum number of semesters needed to take all courses. The testcases will be generated such that it is possible to take every course.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2020/05/22/leetcode_parallel_courses_1.png)
>   Input: n <TeX>=</TeX> 4, dependencies <TeX>=</TeX> [[2,1],[3,1],[1,4]], k <TeX>=</TeX> 2
>   Output: 3
>   Explanation: The figure above represents the given graph.
>   In the first semester, you can take courses 2 and 3.
>   In the second semester, you can take course 1.
>   In the third semester, you can take course 4.
>   Example 2:
>   ![](https://assets.leetcode.com/uploads/2020/05/22/leetcode_parallel_courses_2.png)
>   Input: n <TeX>=</TeX> 5, dependencies <TeX>=</TeX> [[2,1],[3,1],[4,1],[1,5]], k <TeX>=</TeX> 2
>   Output: 4
>   Explanation: The figure above represents the given graph.
>   In the first semester, you can take courses 2 and 3 only since you cannot take more than two per semester.
>   In the second semester, you can take course 4.
>   In the third semester, you can take course 1.
>   In the fourth semester, you can take course 5.
>   Example 3:
>   Input: n <TeX>=</TeX> 11, dependencies <TeX>=</TeX> [], k <TeX>=</TeX> 2
>   Output: 6
**Constraints:**
>   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 15
>   	1 <TeX>\leq</TeX> k <TeX>\leq</TeX> n
>   	0 <TeX>\leq</TeX> relations.length <TeX>\leq</TeX> n  (n-1) / 2
>   	relations[i].length <TeX>=</TeX><TeX>=</TeX> 2
>   	1 <TeX>\leq</TeX> prevCoursei, nextCoursei <TeX>\leq</TeX> n
>   	prevCoursei !<TeX>=</TeX> nextCoursei
>   	All the pairs [prevCoursei, nextCoursei] are unique.
>   	The given graph is a directed acyclic graph.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
use std::collections::HashSet;
impl Solution {
pub fn calculate_combination(courses: Vec<usize>, k: usize) -> Vec<Vec<usize>> {
let n = courses.len();
if k == 1 {
return (0..n).into_iter().map(|i| vec![courses[i]]).collect::<Vec<_>>();
}
let mut res: Vec<Vec<usize>> = vec![];
for i in 0..n {
let course = courses[i];
let remain_courses = (0..courses.len()).into_iter()
.filter(|&k| k != i)
.map(|k| courses[k]).collect::<Vec<_>>();
let mut pre_res = Self::calculate_combination(remain_courses, k - 1);
for j in 0..pre_res.len() {
pre_res[j].insert(0, course);
res.push(pre_res[j].clone());
}
}
res
}

pub fn dfs(graph: &mut Vec<HashSet<usize>>, in_degrees: &mut Vec<i32>, visited: &mut Vec<bool>, k: usize) -> i32 {
let n = graph.len();
let courses: Vec<usize> = (0..n).into_iter().filter(|&i| !visited[i]).collect::<Vec<_>>();
// reverse_graph[i].len() == 0 &&
if courses.len() == 0 {
return 0i32;
}
let in_degrees_zero_courses = courses.into_iter().filter(|&i| in_degrees[i] == 0).collect::<Vec<_>>();
//println!("in_degrees_zero_courses: {:?}", in_degrees_zero_courses);
if in_degrees_zero_courses.len() == 0 {
return 0i32;
}
let taken_options = if in_degrees_zero_courses.len() <= k {
vec![in_degrees_zero_courses]
} else {
Self::calculate_combination(in_degrees_zero_courses, k)
};
//println!("taken_options: {:?}", taken_options.len());
let mut result = i32::MAX;
for i in 0..taken_options.len() {
let option = &taken_options[i];
for &i in option.iter() {
visited[i] = true;
}
let mut in_dgree_decrease: Vec<i32> = vec![0; n];
//let mut removed_edges: Vec<(usize, usize)> = vec![];
for &i in option.iter() {
for &j in graph[i].iter() {
in_degrees[j] -= 1;
in_dgree_decrease[j] += 1;
}
}
let res = Self::dfs(graph, in_degrees, visited, k);
for k in 0..n {
in_degrees[k] += in_dgree_decrease[k];
}
for &i in option.iter() {
visited[i] = false;
}
result = i32::min(result, 1 + res);
}
result
}
pub fn min_number_of_semesters(n: i32, relations: Vec<Vec<i32>>, k: i32) -> i32 {
let n = n as usize;
let k = k as usize;
let mut in_degrees: Vec<i32> = vec![0i32; n];
let mut graph: Vec<HashSet<usize>> = vec![HashSet::new(); n];
//let mut reverse_graph: Vec<HashSet<usize>> = vec![HashSet::new(); n];
for i in 0..relations.len() {
let from = relations[i][0] as usize - 1;
let to = relations[i][1] as usize - 1;
graph[from].insert(to);
//reverse_graph[to].insert(from);
in_degrees[to] += 1;
}
let mut visited: Vec<bool> = vec![false; n];
let independent_courses = (0..n).into_iter().filter(|&i| in_degrees[i] == 0 && graph[i].len() == 0).collect::<Vec<_>>();
let days: usize = independent_courses.len() / k;
for i in 0..days * k {
visited[independent_courses[i]] = true;
}
days as i32 + Self::dfs(&mut graph, &mut in_degrees, &mut visited, k as usize)
}
}
*/
// https://alighters.github.io/blog/2020/09/20/1494-parallel-courses-ii/
impl Solution {
pub fn min_number_of_semesters(n: i32, relations: Vec<Vec<i32>>, k: i32) -> i32 {
let n = n as usize;
// step 1. save the courses we need to take as integer
// e.x.) if prerequisites for course 2 are courses 0 and 3 store integer value of `1001` to prerequisites[2]
let mut prerequisites: Vec<usize> = vec![0; n];
for relation in relations.iter() {
let from = relation[0] as usize - 1;
let to = relation[1] as usize - 1;
prerequisites[to] |= 1 << from;
}
// step 2. dp[courses] = what is the minimum number of days it takes to finish the course given that we have the `courses` left to take?
let mut dp: Vec<i32> = vec![i32::MAX; 1 << n];
dp[0] = 0; // no courses left to take == no more semester necessary
for i in 0..(1 << n) {
if dp[i] == i32::MAX {
continue;
}
// i = courses we have taken
let mut available_courses = 0;
for course in 0..n {
if (prerequisites[course] & i) == prerequisites[course] {
available_courses |= 1 << course;
}
}
available_courses &= !i;
let mut next_semester = available_courses;
while next_semester > 0 {
if next_semester.count_ones() <= k as u32 {
dp[(i | next_semester) as usize] = i32::min(dp[(i | next_semester) as usize], 1 + dp[i as usize]);
}
next_semester = (next_semester - 1) & available_courses;
}
}
dp[(1 << n) - 1]
}
}
// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_1494() {
assert_eq!(Solution::min_number_of_semesters(13, vec![vec![12,8],vec![2,4],vec![3,7],vec![6,8],vec![11,8],vec![9,4],vec![9,7],vec![12,4],vec![11,4],vec![6,4],vec![1,4],vec![10,7],vec![10,4],vec![1,7],vec![1,8],vec![2,7],vec![8,4],vec![10,8],vec![12,7],vec![5,4],vec![3,4],vec![11,7],vec![7,4],vec![13,4],vec![9,8],vec![13,8]], 9), 3);
//assert_eq!(Solution::min_number_of_semesters(4, vec![vec![2,1],vec![3,1],vec![1,4]], 2), 3);
//assert_eq!(Solution::min_number_of_semesters(5, vec![vec![2,1],vec![3,1],vec![4,1],vec![1,5]], 2), 4);
//assert_eq!(Solution::min_number_of_semesters(11, vec![], 2), 6);
}
}

```

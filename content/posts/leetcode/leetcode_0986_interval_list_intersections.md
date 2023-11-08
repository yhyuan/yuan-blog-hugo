---
title: 986. interval list intersections
date: '2022-06-22'
tags: ['leetcode', 'rust', 'medium', 'interval']
draft: false
description: Solution for leetcode 0986 interval list intersections
---



You are given two lists of closed intervals, firstList and secondList, where firstList[i] <TeX>=</TeX> [starti, endi] and secondList[j] <TeX>=</TeX> [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a < b) denotes the set of real numbers x with a <TeX>\leq</TeX> x <TeX>\leq</TeX> b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2019/01/30/interval1.png)
>   Input: firstList <TeX>=</TeX> [[0,2],[5,10],[13,23],[24,25]], secondList <TeX>=</TeX> [[1,5],[8,12],[15,24],[25,26]]
>   Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
>   Example 2:
>   Input: firstList <TeX>=</TeX> [[1,3],[5,9]], secondList <TeX>=</TeX> []
>   Output: []
>   Example 3:
>   Input: firstList <TeX>=</TeX> [], secondList <TeX>=</TeX> [[4,8],[10,12]]
>   Output: []
>   Example 4:
>   Input: firstList <TeX>=</TeX> [[1,7]], secondList <TeX>=</TeX> [[3,10]]
>   Output: [[3,7]]
**Constraints:**
>   	0 <TeX>\leq</TeX> firstList.length, secondList.length <TeX>\leq</TeX> 1000
>   	firstList.length + secondList.length ><TeX>=</TeX> 1
>   	0 <TeX>\leq</TeX> starti < endi <TeX>\leq</TeX> 10^9
>   	endi < starti+1
>   	0 <TeX>\leq</TeX> startj < endj <TeX>\leq</TeX> 10^9
>   	endj < startj+1


## Solution
Merge the points from two list. Then, record the starting and ending of  the time when the count reach 2.


### Python
```python
class Solution:
def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
def getPoints(intervals):
n = len(intervals)
points = []
for i in range(n):
start = intervals[i][0]
end = intervals[i][1]
points.append((start, 0))
points.append((end, 1))
return points
def merge(points1, points2):
ans = []
n1 = len(points1)
n2 = len(points2)
i = 0
j = 0
while i < n1 and j < n2:
if points1[i] < points2[j]:
ans.append(points1[i])
i += 1
else:
ans.append(points2[j])
j += 1
if i < n1:
for k in range(i, n1):
ans.append(points1[k])
if j < n2:
for k in range(j, n2):
ans.append(points2[k])
return ans

points1 = getPoints(firstList)
points2 = getPoints(secondList)
points = merge(points1, points2)
count = 0
ans = []
for i in range(len(points)):
if points[i][1] == 0:
count += 1
else:
count -= 1
if count == 2 and points[i][1] == 0:
start = points[i][0]
if count == 1 and points[i][1] == 1:
end = points[i][0]
ans.append([start, end])
return ans
```


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn interval_intersection_helper(first_list: &Vec<Vec<i32>>, k1: usize, second_list: &Vec<Vec<i32>>, k2: usize) -> Vec<Vec<i32>> {
let n1 = first_list.len();
let n2 = second_list.len();
if k1 == n1 || k2 == n2 {
return vec![];
}
let first_interval = &first_list[k1];
let second_interval = &second_list[k2];
if first_interval[0] <= second_interval[0] {
if second_interval[0] > first_interval[1]  {
Self::interval_intersection_helper(first_list, k1 + 1, second_list, k2)
} else {// second_interval[0] <= first_interval[1] and second_interval[0] >= first_interval[0]
if second_interval[1] <= first_interval[1] {
let mut pre_results = Self::interval_intersection_helper(first_list, k1, second_list, k2 + 1);
pre_results.insert(0, vec![second_interval[0], second_interval[1]]);
pre_results
} else {
let mut pre_results = Self::interval_intersection_helper(first_list, k1 + 1, second_list, k2);
pre_results.insert(0, vec![second_interval[0], first_interval[1]]);
pre_results
}
}
} else {
if first_interval[0] > second_interval[1]  {
Self::interval_intersection_helper(first_list, k1, second_list, k2 + 1)
} else {// second_interval[0] <= first_interval[1] and second_interval[0] >= first_interval[0]
if first_interval[1] <= second_interval[1] {
let mut pre_results = Self::interval_intersection_helper(first_list, k1 + 1, second_list, k2);
pre_results.insert(0, vec![first_interval[0], first_interval[1]]);
pre_results
} else {
let mut pre_results = Self::interval_intersection_helper(first_list, k1, second_list, k2 + 1);
pre_results.insert(0, vec![first_interval[0], second_interval[1]]);
pre_results
}
}
}
}
pub fn interval_intersection(first_list: Vec<Vec<i32>>, second_list: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
Self::interval_intersection_helper(&first_list, 0, &second_list, 0)
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_986() {
assert_eq!(Solution::interval_intersection(vec![vec![0,2],vec![5,10],vec![13,23],vec![24,25]],
vec![vec![1,5],vec![8,12],vec![15,24],vec![25,26]]),
vec![vec![1,2],vec![5,5],vec![8,10],vec![15,23],vec![24,24],vec![25,25]]);
}
}

```

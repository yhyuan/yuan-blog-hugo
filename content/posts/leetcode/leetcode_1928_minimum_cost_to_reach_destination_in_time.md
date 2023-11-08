---
title: 1928. minimum cost to reach destination in time
date: '2022-08-31'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 1928 minimum cost to reach destination in time
---

 

  There is a country of n cities numbered from 0 to n - 1 where all the cities are connected by bi-directional roads. The roads are represented as a 2D integer array edges where edges[i] <TeX>=</TeX> [xi, yi, timei] denotes a road between cities xi and yi that takes timei minutes to travel. There may be multiple roads of differing travel times connecting the same two cities, but no road connects a city to itself.

  Each time you pass through a city, you must pay a passing fee. This is represented as a 0-indexed integer array passingFees of length n where passingFees[j] is the amount of dollars you must pay when you pass through city j.

  In the beginning, you are at city 0 and want to reach city n - 1 in maxTime minutes or less. The cost of your journey is the summation of passing fees for each city that you passed through at some moment of your journey (including the source and destination cities).

  Given maxTime, edges, and passingFees, return the minimum cost to complete your journey, or -1 if you cannot complete it within maxTime minutes.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/06/04/leetgraph1-1.png)

  

 >   Input: maxTime <TeX>=</TeX> 30, edges <TeX>=</TeX> [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees <TeX>=</TeX> [5,1,2,20,20,3]

 >   Output: 11

 >   Explanation: The path to take is 0 -> 1 -> 2 -> 5, which takes 30 minutes and has $11 worth of passing fees.

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2021/06/04/copy-of-leetgraph1-1.png)

  

 >   Input: maxTime <TeX>=</TeX> 29, edges <TeX>=</TeX> [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees <TeX>=</TeX> [5,1,2,20,20,3]

 >   Output: 48

 >   Explanation: The path to take is 0 -> 3 -> 4 -> 5, which takes 26 minutes and has $48 worth of passing fees.

 >   You cannot take path 0 -> 1 -> 2 -> 5 since it would take too long.

  

 >   Example 3:

  

 >   Input: maxTime <TeX>=</TeX> 25, edges <TeX>=</TeX> [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees <TeX>=</TeX> [5,1,2,20,20,3]

 >   Output: -1

 >   Explanation: There is no way to reach city 5 from city 0 within 25 minutes.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> maxTime <TeX>\leq</TeX> 1000

 >   	n <TeX>=</TeX><TeX>=</TeX> passingFees.length

 >   	2 <TeX>\leq</TeX> n <TeX>\leq</TeX> 1000

 >   	n - 1 <TeX>\leq</TeX> edges.length <TeX>\leq</TeX> 1000

 >   	0 <TeX>\leq</TeX> xi, yi <TeX>\leq</TeX> n - 1

 >   	1 <TeX>\leq</TeX> timei <TeX>\leq</TeX> 1000

 >   	1 <TeX>\leq</TeX> passingFees[j] <TeX>\leq</TeX> 1000 

 >   	The graph may contain multiple edges between two nodes.

 >   	The graph does not contain self loops.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::{HashSet, HashMap};
impl Solution {
    pub fn dfs(graph: &Vec<HashSet<(usize, usize)>>, passing_fees: &Vec<i32>, memo: &mut HashMap<(i32, usize), i32>, index: usize, max_time: i32) -> i32 {
        if index == 0 {
            return 0i32;
        }
        if memo.contains_key(&(max_time, index)) {
            return memo[&(max_time, index)];
        }
        let mut res = i32::MAX;
        for &(neighbor, time) in graph[index].iter() {
            if max_time >= time as i32 {
                let cost = Self::dfs(graph, passing_fees, memo, neighbor, max_time - time as i32);
                if cost < i32::MAX {
                    res = i32::min(res, cost + passing_fees[neighbor]);
                }
            }
        }
        memo.insert((max_time, index), res);
        // println!("max_time: {}, index: {}, res: {}", max_time, index, res);
        res
    }
    pub fn min_cost(max_time: i32, edges: Vec<Vec<i32>>, passing_fees: Vec<i32>) -> i32 {
        let n = passing_fees.len();
        // let mut times_hashmap: HashMap<(usize, usize), usize> = HashMap::new();
        let mut graph: Vec<HashSet<(usize, usize)>> = vec![HashSet::new(); n];
        for i in 0..edges.len() {
            let start = edges[i][0] as usize;
            let end = edges[i][1] as usize;
            let time = edges[i][2] as usize;
            //times_hashmap.insert((start, end), time);
            //times_hashmap.insert((end, start), time);
            graph[start].insert((end, time));
            graph[end].insert((start, time));
        }
        //println!("n: {}", n);
        //println!("graph: {:?}", graph);

        let mut memo: HashMap<(i32, usize), i32> = HashMap::new();
        let cost = Self::dfs(&graph, &passing_fees, &mut memo, n - 1, max_time);
        // println!("memo: {:?}", memo);
        if cost == i32::MAX {-1} else {cost + passing_fees[n - 1]}
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1928() {
        assert_eq!(Solution::min_cost(24, 
            vec![vec![27,8,37],vec![9,36,15],vec![15,8,13],vec![30,8,12],vec![21,4,30],vec![22,33,46],vec![27,29,10],vec![35,32,35],vec![22,39,34],vec![9,45,14],vec![26,21,44],vec![13,36,14],vec![3,49,20],vec![28,44,11],vec![15,30,5],vec![26,49,36],vec![8,40,3],vec![28,25,1],vec![41,46,48],vec![38,24,8],vec![30,7,39],vec![14,3,36],vec![2,19,21],vec![12,39,37],vec![16,3,47],vec![11,31,22],vec![38,25,34],vec![42,6,47],vec![14,20,21],vec![33,8,35],vec![17,5,2],vec![36,19,3],vec![47,28,40],vec![37,33,35],vec![24,47,40],vec![7,15,26],vec![8,0,13],vec![40,34,10],vec![25,3,19],vec![44,9,5],vec![16,6,22],vec![34,35,39],vec![24,5,2],vec![3,22,16],vec![27,24,3],vec![35,5,29],vec![5,48,49],vec![12,22,8],vec![45,15,36],vec![2,35,36],vec![24,18,14],vec![24,49,3],vec![49,20,38],vec![41,24,25],vec![18,49,15],vec![24,4,23],vec![16,0,22],vec![41,46,34],vec![7,12,31],vec![9,5,13],vec![19,44,49],vec![8,25,8],vec![24,7,9],vec![4,33,38],vec![49,19,17],vec![11,31,19],vec![29,40,31],vec![30,29,10],vec![25,20,31],vec![38,28,18],vec![21,29,18],vec![18,46,19],vec![43,33,43],vec![22,15,19],vec![26,44,21],vec![9,13,13],vec![0,20,9],vec![11,9,12],vec![22,39,43],vec![43,47,29],vec![12,10,34],vec![49,36,41],vec![39,48,11],vec![9,27,13],vec![9,8,30],vec![18,49,39],vec![18,33,40],vec![35,22,28],vec![8,6,24],vec![14,41,10],vec![21,34,20],vec![37,6,2],vec![20,7,24],vec![11,10,29],vec![12,35,2],vec![22,41,9],vec![47,1,16],vec![29,2,38],vec![46,40,29],vec![32,47,10],vec![39,33,23],vec![24,17,3],vec![27,47,3],vec![28,10,37],vec![42,48,46],vec![48,24,20],vec![48,44,16],vec![34,47,28],vec![48,34,3],vec![12,23,39],vec![13,4,44],vec![0,33,39],vec![21,3,3],vec![45,14,38],vec![36,9,18],vec![19,3,37],vec![6,2,27],vec![29,40,37],vec![37,42,44],vec![10,14,10],vec![15,17,21],vec![35,12,14],vec![46,10,18],vec![41,0,47],vec![46,28,42],vec![13,19,25],vec![42,11,30],vec![27,14,47],vec![47,30,36],vec![13,43,4],vec![29,3,14],vec![36,16,40],vec![1,0,18],vec![18,6,1],vec![18,0,20],vec![24,38,37],vec![25,48,12],vec![34,12,27],vec![8,42,12],vec![40,4,5],vec![33,15,13],vec![40,14,43],vec![17,23,25],vec![7,3,12],vec![41,42,32],vec![7,11,4],vec![33,23,36],vec![3,25,7],vec![20,22,29],vec![19,18,21],vec![6,34,34],vec![21,31,9],vec![48,16,22],vec![14,0,7],vec![20,10,24],vec![5,6,44],vec![24,48,27],vec![4,39,1],vec![16,41,43],vec![2,27,1],vec![0,7,13],vec![6,2,30],vec![40,43,15],vec![35,39,44],vec![45,47,37],vec![29,28,40],vec![27,41,38],vec![43,48,49],vec![23,3,34],vec![48,43,10],vec![7,23,17],vec![4,9,44],vec![22,41,29],vec![42,13,33],vec![40,7,24],vec![23,21,8],vec![4,3,27],vec![7,22,42],vec![12,26,3],vec![38,23,3],vec![14,8,16],vec![35,26,31],vec![40,7,9],vec![4,13,4],vec![48,47,27],vec![18,27,2],vec![20,30,27],vec![7,32,32],vec![12,5,25],vec![47,41,25],vec![49,27,37],vec![9,43,4],vec![47,2,15],vec![14,47,24],vec![28,10,4],vec![36,2,11],vec![36,25,14],vec![17,5,38],vec![26,20,17],vec![25,40,5],vec![26,12,30],vec![29,19,24],vec![47,16,15],vec![4,19,27],vec![8,44,1],vec![13,41,44],vec![6,20,28],vec![44,13,35],vec![11,39,25],vec![6,8,19],vec![16,30,15],vec![36,43,25],vec![43,2,9],vec![34,42,46],vec![13,18,45],vec![48,27,36],vec![16,13,9],vec![48,27,9],vec![49,18,6],vec![41,5,50],vec![1,20,12],vec![27,13,40],vec![1,0,30],vec![48,28,14],vec![20,29,15],vec![14,23,27],vec![14,23,4],vec![3,48,18],vec![2,21,31],vec![18,43,31],vec![7,1,11],vec![25,23,24],vec![24,0,21],vec![2,1,38],vec![20,31,27],vec![8,38,50],vec![23,16,33],vec![22,28,19],vec![48,17,8],vec![22,6,22],vec![4,3,43],vec![35,4,40],vec![32,7,8],vec![46,37,49],vec![39,24,24],vec![36,9,25],vec![39,34,22],vec![10,28,24],vec![36,8,21],vec![23,30,36],vec![6,0,27],vec![35,39,47],vec![14,40,30],vec![16,24,32],vec![1,22,13],vec![0,40,32],vec![20,15,48],vec![28,16,2],vec![16,29,42],vec![24,19,1],vec![32,31,11],vec![4,29,4],vec![35,39,16],vec![46,12,38],vec![22,48,49],vec![28,12,47],vec![0,6,22],vec![39,44,14],vec![5,37,19],vec![43,33,33],vec![37,23,21],vec![13,8,50],vec![36,16,30],vec![9,24,30],vec![24,10,28],vec![12,42,11],vec![4,20,4],vec![6,44,31],vec![15,17,39],vec![14,30,36],vec![18,47,34],vec![18,30,28],vec![16,40,50],vec![30,3,24],vec![6,4,41],vec![7,11,6],vec![10,20,20],vec![16,43,18],vec![13,27,14],vec![18,1,33],vec![24,48,45],vec![2,48,21],vec![30,18,32],vec![18,42,17],vec![42,15,36],vec![36,7,6],vec![35,31,12],vec![13,31,45],vec![7,8,8],vec![39,29,12],vec![20,39,43],vec![14,42,5],vec![6,32,44],vec![11,4,21],vec![34,25,26],vec![28,29,28],vec![45,4,7],vec![12,2,5],vec![27,41,44],vec![44,34,11],vec![7,11,37],vec![31,16,13],vec![47,13,14],vec![5,34,6],vec![41,11,49],vec![48,11,20],vec![33,42,2],vec![18,5,21],vec![4,19,9],vec![38,46,26],vec![26,17,13],vec![19,41,49],vec![11,38,22],vec![2,21,11],vec![13,49,14],vec![21,9,36],vec![8,14,27],vec![45,9,14],vec![1,2,1],vec![38,4,35],vec![1,48,39],vec![1,18,50],vec![3,5,4],vec![47,3,37],vec![6,26,31],vec![49,22,46],vec![14,19,49],vec![11,33,34],vec![17,7,25],vec![30,14,31],vec![18,14,45],vec![29,2,45],vec![14,35,49],vec![10,37,28],vec![12,15,20],vec![34,0,45],vec![42,7,37],vec![41,15,16],vec![47,12,26],vec![0,30,11],vec![10,1,22],vec![16,36,16],vec![24,32,10],vec![24,22,50],vec![35,4,13],vec![45,10,41],vec![17,36,23],vec![2,48,14],vec![33,11,30],vec![6,22,27],vec![42,14,35],vec![22,4,17],vec![25,35,26],vec![49,18,13],vec![16,25,35],vec![41,20,12],vec![2,30,29],vec![12,11,12],vec![47,3,13],vec![2,10,34],vec![13,29,15],vec![37,34,44],vec![8,33,21],vec![42,37,49],vec![48,26,31],vec![18,44,23],vec![22,8,18],vec![34,37,30],vec![41,40,49],vec![17,41,11],vec![1,23,32],vec![5,1,48],vec![49,23,50],vec![40,49,32],vec![25,46,6],vec![43,30,37],vec![20,3,13],vec![5,46,49],vec![34,10,35],vec![42,48,38],vec![40,16,31],vec![49,43,16],vec![24,12,16],vec![2,0,36],vec![49,29,10],vec![16,37,37],vec![22,45,44],vec![42,21,35],vec![39,33,14],vec![9,3,2],vec![42,34,19],vec![35,46,24],vec![36,30,44],vec![17,2,34],vec![4,30,29],vec![28,15,28],vec![9,8,44],vec![36,42,46],vec![9,14,41],vec![40,23,3],vec![41,9,23],vec![42,47,29],vec![2,22,48],vec![22,44,32],vec![15,7,46],vec![11,28,4],vec![28,7,47],vec![14,39,21],vec![2,7,6],vec![1,9,12],vec![25,16,15],vec![44,10,48],vec![46,15,3],vec![7,3,32],vec![44,30,18],vec![27,10,46],vec![11,4,28],vec![49,15,15],vec![49,36,10],vec![36,15,39],vec![16,36,21],vec![11,21,29],vec![29,12,17],vec![29,31,24],vec![32,47,13],vec![3,4,17],vec![31,18,13],vec![11,33,6],vec![7,27,50],vec![7,3,40],vec![24,40,41],vec![47,25,42],vec![20,38,21],vec![42,25,10],vec![20,0,42],vec![31,19,6],vec![31,8,29],vec![3,19,10],vec![9,32,50],vec![15,17,40],vec![12,9,42],vec![16,28,25],vec![26,10,20],vec![19,0,42],vec![10,48,27],vec![47,1,33],vec![36,29,18],vec![38,36,38],vec![0,41,31],vec![17,27,23],vec![39,8,30],vec![47,37,5],vec![39,1,50],vec![39,25,21],vec![13,35,22],vec![0,22,8],vec![3,1,39],vec![11,7,3],vec![12,44,28],vec![33,13,27],vec![30,16,7],vec![36,45,31],vec![33,32,42],vec![33,1,15],vec![39,3,23],vec![48,6,12],vec![24,49,5],vec![13,46,22],vec![43,23,26],vec![24,15,46],vec![24,43,14],vec![0,14,31],vec![42,41,6],vec![14,47,6],vec![36,39,6],vec![24,18,45],vec![10,39,1],vec![17,25,22],vec![36,23,23],vec![10,23,42],vec![40,33,41],vec![41,28,13],vec![25,1,1],vec![10,45,19],vec![40,2,42],vec![14,42,40],vec![13,37,24],vec![29,38,32],vec![47,11,35],vec![24,4,45],vec![37,40,7],vec![29,45,37],vec![13,44,49]], 
            vec![190,843,824,838,336,528,395,301,902,169,729,254,2,463,15,649,865,840,198,789,232,516,699,157,608,893,40,87,615,294,214,66,313,103,847,326,501,1000,65,35,622,905,15,571,808,444,866,11,182,657]), 
        1158);
        assert_eq!(Solution::min_cost(30, vec![vec![0,1,10],vec![1,2,10],vec![2,5,10],vec![0,3,1],vec![3,4,10],vec![4,5,15]], vec![5,1,2,20,20,3]), 11);
        assert_eq!(Solution::min_cost(29, vec![vec![0,1,10],vec![1,2,10],vec![2,5,10],vec![0,3,1],vec![3,4,10],vec![4,5,15]], vec![5,1,2,20,20,3]), 48);
    }
}

```

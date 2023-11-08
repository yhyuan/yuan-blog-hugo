---
title: 787. cheapest flights within k stops
date: '2022-05-17'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0787 cheapest flights within k stops
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={787}/>
 

  There are n cities connected by some number of flights. You are given an array flights where flights[i] <TeX>=</TeX> [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

  You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

   

 >   Example 1:

 >   ![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/16/995.png)

 >   Input: n <TeX>=</TeX> 3, flights <TeX>=</TeX> [[0,1,100],[1,2,100],[0,2,500]], src <TeX>=</TeX> 0, dst <TeX>=</TeX> 2, k <TeX>=</TeX> 1

 >   Output: 200

 >   Explanation: The graph is shown.

 >   The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

  

 >   Example 2:

 >   ![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/16/995.png)

 >   Input: n <TeX>=</TeX> 3, flights <TeX>=</TeX> [[0,1,100],[1,2,100],[0,2,500]], src <TeX>=</TeX> 0, dst <TeX>=</TeX> 2, k <TeX>=</TeX> 0

 >   Output: 500

 >   Explanation: The graph is shown.

 >   The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 100

 >   	0 <TeX>\leq</TeX> flights.length <TeX>\leq</TeX> (n  (n - 1) / 2)

 >   	flights[i].length <TeX>=</TeX><TeX>=</TeX> 3

 >   	0 <TeX>\leq</TeX> fromi, toi < n

 >   	fromi !<TeX>=</TeX> toi

 >   	1 <TeX>\leq</TeX> pricei <TeX>\leq</TeX> 10^4

 >   	There will not be any multiple flights between two cities.

 >   	0 <TeX>\leq</TeX> src, dst, k < n

 >   	src !<TeX>=</TeX> dst


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::{HashSet, HashMap};
impl Solution {
    pub fn find_cheapest_price(n: i32, flights: Vec<Vec<i32>>, src: i32, dst: i32, k: i32) -> i32 {
        let n = n as usize;
        let mut graph: Vec<HashSet<usize>> = vec![HashSet::new(); n];
        let mut costs: HashMap<(usize, usize), i32> = HashMap::new();
        for i in 0..flights.len() {
            let start = flights[i][0] as usize;
            let end = flights[i][1] as usize;
            let cost = flights[i][2];
            graph[start].insert(end);     
            costs.insert((start, end), cost);
        }
        let k_max = k as usize;
        let mut dp: Vec<Vec<i32>> = vec![vec![i32::MAX; n]; k_max + 1];
        let src = src as usize;
        let dst = dst as usize;
        for &i in graph[src].iter() {
            dp[0][i] = costs[&(src, i)];
        }
        for k in 1..=k_max {
            for j in 0..n {
                if dp[k - 1][j] != i32::MAX {
                    for &m in graph[j].iter() {
                        dp[k][m] = i32::min(dp[k][m], dp[k - 1][j] + costs[&(j, m)]);
                    }
                }
            }
        }
        let res = dp.iter().map(|v| v[dst]).min().unwrap();
        if res == i32::MAX {-1} else {res}
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_787() {
    }
}

```

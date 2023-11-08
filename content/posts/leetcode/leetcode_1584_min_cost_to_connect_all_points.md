---
title: 1584. min cost to connect all points
date: '2022-08-16'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 1584 min cost to connect all points
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1584}/>
 

  You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] <TeX>=</TeX> [xi, yi].

  The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

  Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/08/26/d.png)

  

 >   Input: points <TeX>=</TeX> [[0,0],[2,2],[3,10],[5,2],[7,0]]

 >   Output: 20

 >   Explanation:

 >   ![](https://assets.leetcode.com/uploads/2020/08/26/c.png)

 >   We can connect the points as shown above to get the minimum cost of 20.

 >   Notice that there is a unique path between every pair of points.

  

 >   Example 2:

  

 >   Input: points <TeX>=</TeX> [[3,12],[-2,5],[-4,1]]

 >   Output: 18

  

 >   Example 3:

  

 >   Input: points <TeX>=</TeX> [[0,0],[1,1],[1,0],[-1,1]]

 >   Output: 4

  

 >   Example 4:

  

 >   Input: points <TeX>=</TeX> [[-1000000,-1000000],[1000000,1000000]]

 >   Output: 4000000

  

 >   Example 5:

  

 >   Input: points <TeX>=</TeX> [[0,0]]

 >   Output: 0

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> points.length <TeX>\leq</TeX> 1000

 >   	-10^6 <TeX>\leq</TeX> xi, yi <TeX>\leq</TeX> 10^6

 >   	All pairs (xi, yi) are distinct.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
pub struct UF {
    parents: Vec<usize>,
    ranks: Vec<usize>,
    count: usize,
}

impl UF {
    pub fn new(n: usize) -> UF {
        let parents = (0..n).into_iter().collect::<Vec<_>>();
        let ranks = vec![1; n];
        let count = n;
        UF {
            parents,
            ranks, 
            count
        }
    }

    pub fn find(&mut self, i: usize) -> usize {
        let mut root = self.parents[i];
        while root != self.parents[root] {
            root = self.parents[root];
        }
        let mut p = self.parents[i];
        while p != self.parents[p] {
            let tmp = self.parents[p];
            self.parents[p] = root;
            p = tmp;
        }
        root
    }

    pub fn union(&mut self, i: usize, j: usize) -> bool {
        let ip = self.find(i);
        let jp = self.find(j);
        if ip == jp {
            return false;
        }
        if self.ranks[ip] < self.ranks[jp] {
            self.parents[ip] = jp;
        } else {
            self.parents[jp] = ip;
            if self.ranks[ip] == self.ranks[jp] {
                self.ranks[ip] += 1;
            }
        }
        self.count -= 1;
        true
    }
}
impl Solution {
    pub fn min_cost_connect_points(points: Vec<Vec<i32>>) -> i32 {
        let n = points.len();
        let mut edges: Vec<(usize, usize, i32)> = vec![];
        for i in 0..n {
            let i_x = points[i][0];
            let i_y = points[i][1];
            for j in i + 1..n {
                let j_x = points[j][0];
                let j_y = points[j][1];
                let dist = (j_x - i_x).abs() + (j_y - i_y).abs();
                edges.push((i, j, dist));
            }
        }
        edges.sort_by(|a, b| a.2.partial_cmp(&b.2).unwrap());
        let mut uf = UF::new(n);
        let mut res = 0i32;
        for i in 0..edges.len() {
            let start = edges[i].0;
            let end = edges[i].1;
            let cost = edges[i].2;
            if uf.find(start) != uf.find(end) {
                uf.union(start, end);
                res += cost;
            }
        }
        res
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1584() {
        assert_eq!(Solution::min_cost_connect_points(vec![vec![0,0],vec![2,2],vec![3,10],vec![5,2],vec![7,0]]), 20);
        assert_eq!(Solution::min_cost_connect_points(vec![vec![3,12],vec![-2,5],vec![-4,1]]), 18);
    }
}

```

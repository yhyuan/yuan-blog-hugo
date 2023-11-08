---
title: 149. max points on a line
date: '2021-09-21'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0149 max points on a line
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={149}/>
 

  Given an array of points where points[i] <TeX>=</TeX> [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/02/25/plane1.jpg)

 >   Input: points <TeX>=</TeX> [[1,1],[2,2],[3,3]]

 >   Output: 3

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2021/02/25/plane2.jpg)

 >   Input: points <TeX>=</TeX> [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]

 >   Output: 4

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> points.length <TeX>\leq</TeX> 300

 >   	points[i].length <TeX>=</TeX><TeX>=</TeX> 2

 >   	-10^4 <TeX>\leq</TeX> xi, yi <TeX>\leq</TeX> 10^4

 >   	All the points are unique.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::cmp::Ordering;
impl Solution {
    pub fn max_points(points: Vec<Vec<i32>>) -> i32 {
        let mut max_count = 2i32;
        let n = points.len();
        if n == 1 {
            return 1;
        }
        for i in 0..n {
            let mut deltas: Vec<(i64, i64)> = (i + 1..n).into_iter()
                .map(|j| ((points[j][0] - points[i][0]) as i64, (points[j][1] - points[i][1]) as i64))
                .collect();
            deltas.sort_by(|&a, &b| {
                if a.0 == 0 && b.0 == 0 {
                    return Ordering::Equal;
                }
                if a.0 == 0 && b.0 != 0 {
                    return Ordering::Greater;
                }
                if a.0 != 0 && b.0 == 0 {
                    return Ordering::Less;
                }
                let a_slope = a.1 as f64 / a.0 as f64;
                let b_slope = b.1 as f64 / b.0 as f64;
                a_slope.partial_cmp(&b_slope).unwrap()
            });
            println!("{:?}", deltas);
            if deltas.len() == 0 {
                continue;
            }
            let mut pre_dx = deltas[0].0;
            let mut pre_dy = deltas[0].1;
            let mut count = 2;
            for j in 1..deltas.len() {
                let dx = deltas[j].0;
                let dy = deltas[j].1;
                if dx * pre_dy == pre_dx * dy {
                    count += 1;
                } else {
                    pre_dx = dx;
                    pre_dy = dy;
                    max_count = i32::max(max_count, count);
                    count = 2;
                }
            }
            max_count = i32::max(max_count, count);
        }
        max_count
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_149() {
        assert_eq!(
            Solution::max_points(vec![vec![1, 1], vec![2, 2], vec![3, 3]]),
            3
        );
        
        assert_eq!(
            Solution::max_points(vec![
                vec![1, 1],
                vec![3, 2],
                vec![5, 3],
                vec![4, 1],
                vec![2, 3],
                vec![1, 4]
            ]),
            4
        );
        assert_eq!(
            Solution::max_points(vec![vec![0, 0], vec![1, 65536], vec![65536, 0]]),
            2
        );
        assert_eq!(
            Solution::max_points(vec![vec![1, 1], vec![1, 1], vec![1, 1]]),
            3
        );
        assert_eq!(
            Solution::max_points(vec![
                vec![0, 9],
                vec![138, 429],
                vec![115, 359],
                vec![115, 359],
                vec![-30, -102],
                vec![230, 709],
                vec![-150, -686],
                vec![-135, -613],
                vec![-60, -248],
                vec![-161, -481],
                vec![207, 639],
                vec![23, 79],
                vec![-230, -691],
                vec![-115, -341],
                vec![92, 289],
                vec![60, 336],
                vec![-105, -467],
                vec![135, 701],
                vec![-90, -394],
                vec![-184, -551],
                vec![150, 774]
            ]),
            12
        );
        
    }
}

```

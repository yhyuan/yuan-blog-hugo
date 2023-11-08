---
title: 939. minimum area rectangle
date: '2022-06-17'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0939 minimum area rectangle
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={939}/>
 

  You are given an array of points in the X-Y plane points where points[i] <TeX>=</TeX> [xi, yi].

  Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/08/03/rec1.JPG)

 >   Input: points <TeX>=</TeX> [[1,1],[1,3],[3,1],[3,3],[2,2]]

 >   Output: 4

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2021/08/03/rec2.JPG)

 >   Input: points <TeX>=</TeX> [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]

 >   Output: 2

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> points.length <TeX>\leq</TeX> 500

 >   	points[i].length <TeX>=</TeX><TeX>=</TeX> 2

 >   	0 <TeX>\leq</TeX> xi, yi <TeX>\leq</TeX> 4  10^4

 >   	All the given points are unique.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
这道题给了我们一堆点的坐标，问能组成的最小的矩形面积是多少，题目中限定了矩形的边一定是平行于主轴的，不会出现旋转矩形的形状。
如果知道了矩形的两个对角顶点坐标，求面积就非常的简单了，但是随便取四个点并不能保证一定是矩形，不过这四个点坐标之间是有联系的，
相邻的两个顶点要么横坐标，要么纵坐标，一定有一个是相等的，这个特点先记下。策略是，先找出两个对角线的顶点，一但两个对角顶点确定了，
其实这个矩形的大小也就确定了，另外的两个点其实就是分别在跟这两个点具有相同的横坐标或纵坐标的点中寻找即可，为了优化查找的时间，
可以事先把所有具有相同横坐标的点的纵坐标放入到一个 HashSet 中，使用一个 HashMap，建立横坐标和所有具有该横坐标的点的纵坐标的集合
之间的映射。然后开始遍历任意两个点的组合，由于这两个点必须是对角顶点，所以其横纵坐标均不能相等，若有一个相等了，则跳过该组合。否则
看其中任意一个点的横坐标对应的集合中是否均包含另一个点的纵坐标，均包含的话，说明另两个顶点也是存在的，就可以计算矩形的面积了，
更新结果 res，若最终 res 还是初始值，说明并没有能组成矩形，返回0即可，参见代码如下：
*/
use std::collections::{HashSet, HashMap};

impl Solution {
    pub fn min_area_rect(points: Vec<Vec<i32>>) -> i32 {
        let mut x_hashmap: HashMap<i32, HashSet<(i32, i32)>> = HashMap::new();
        let n = points.len();
        for i in 0..n {
            let x = points[i][0];
            let y = points[i][1];
            if x_hashmap.contains_key(&x) {
                x_hashmap.get_mut(&x).unwrap().insert((x, y));
            } else {
                let mut hashset:HashSet<(i32, i32)> = HashSet::new();
                hashset.insert((x, y));
                x_hashmap.insert(x, hashset);
            }
        }
        //println!("x_hashmap: {:?}", x_hashmap);
        let mut res = i32::MAX;
        for i in 0..n {
            let (x1, y1) = (points[i][0], points[i][1]);
            for j in i + 1..n {
                let (x2, y2) = (points[j][0], points[j][1]);
                // (x1, y2) (x2, y1)
                if x_hashmap[&x1].contains(&(x1, y2)) && x_hashmap[&x2].contains(&(x2, y1)) {
                    let area = (x1 - x2).abs() * (y1 - y2).abs();
                    if area > 0 {
                        res = i32::min(res, area)
                    }
                }
            }
        }
        if res == i32::MAX {0} else {res}
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_939() {
        assert_eq!(Solution::min_area_rect(vec![vec![1,1],vec![1,3],vec![3,1],vec![3,3],vec![2,2]]), 4);
        assert_eq!(Solution::min_area_rect(vec![vec![1,1],vec![1,3],vec![3,1],vec![3,3],vec![4,1],vec![4,3]]), 2);
    }
}

```

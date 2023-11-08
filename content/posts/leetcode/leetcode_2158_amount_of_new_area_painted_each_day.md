---
title: 2158. amount of new area painted each day
date: '2022-09-14'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 2158 amount of new area painted each day
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={2158}/>

There is a long and thin painting that can be represented by a number line. You are given a 0-indexed 2D integer array paint of length n, where paint[i] <TeX>=</TeX> [starti, endi]. This means that on the ith day you need to paint the area between starti and endi.



Painting the same area multiple times will create an uneven painting so you only want to paint each area of the painting at most once.



Return an integer array worklog of length n, where worklog[i] is the amount of new area that you painted on the ith day.



 



 > Example 1:





 > Input: paint <TeX>=</TeX> [[1,4],[4,7],[5,8]]

 > Output: [3,3,1]

 > Explanation:

 > On day 0, paint everything between 1 and 4.

 > The amount of new area painted on day 0 is 4 - 1 <TeX>=</TeX> 3.

 > On day 1, paint everything between 4 and 7.

 > The amount of new area painted on day 1 is 7 - 4 <TeX>=</TeX> 3.

 > On day 2, paint everything between 7 and 8.

 > Everything between 5 and 7 was already painted on day 1.

 > The amount of new area painted on day 2 is 8 - 7 <TeX>=</TeX> 1. 

 > Example 2:





 > Input: paint <TeX>=</TeX> [[1,4],[5,8],[4,7]]

 > Output: [3,3,1]

 > Explanation:

 > On day 0, paint everything between 1 and 4.

 > The amount of new area painted on day 0 is 4 - 1 <TeX>=</TeX> 3.

 > On day 1, paint everything between 5 and 8.

 > The amount of new area painted on day 1 is 8 - 5 <TeX>=</TeX> 3.

 > On day 2, paint everything between 4 and 5.

 > Everything between 5 and 7 was already painted on day 1.

 > The amount of new area painted on day 2 is 5 - 4 <TeX>=</TeX> 1. 

 > Example 3:





 > Input: paint <TeX>=</TeX> [[1,5],[2,4]]

 > Output: [4,0]

 > Explanation:

 > On day 0, paint everything between 1 and 5.

 > The amount of new area painted on day 0 is 5 - 1 <TeX>=</TeX> 4.

 > On day 1, paint nothing because everything between 2 and 4 was already painted on day 0.

 > The amount of new area painted on day 1 is 0.

 



**Constraints:**



 > 1 <TeX>\leq</TeX> paint.length <TeX>\leq</TeX> 105

 > paint[i].length <TeX>=</TeX><TeX>=</TeX> 2

 > 0 <TeX>\leq</TeX> starti < endi <TeX>\leq</TeX> 5  104


## Solution
### Rust
```rust

pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn amount_painted(paint: Vec<Vec<i32>>) -> Vec<i32> {
        let min_day = paint.iter().map(|interval| interval[0]).min().unwrap();
        let max_day = paint.iter().map(|interval| interval[1]).max().unwrap();
        let n = paint.len();
        let mut ans: Vec<i32> = vec![0; n];
        let mut events: Vec<(i32, usize, i32)> = vec![];
        for i in 0..n {
            let start = paint[i][0];
            let end = paint[i][1];
            events.push((start, i, 1)); // entering
            events.push((end, i, -1)); // leaving
        }
        events.sort();
        let mut running_indices: Vec<usize> = vec![];
        let mut i = 0; // event index
        for day in min_day..max_day {
            while i < events.len() && events[i].0 == day {
                let (_, index, event_type) = events[i];
                if event_type == 1 {
                    match running_indices.binary_search(&index) {
                        Err(k) => {
                            running_indices.insert(k, index);
                        },
                        Ok(_) => unreachable!(),
                    }
                } else {
                    let k = running_indices.binary_search(&index).unwrap();
                    running_indices.remove(k);
                }
                i += 1;
            }
            if running_indices.len() > 0 {
                ans[running_indices[0]] += 1;
            }
        }
        ans
    }
}// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_2158() {
        assert_eq!(Solution::amount_painted(vec![vec![1,4],vec![4,7],vec![5,8]]), vec![3,3,1]);
        assert_eq!(Solution::amount_painted(vec![vec![1,4],vec![5,8],vec![4,7]]), vec![3,3,1]);
        assert_eq!(Solution::amount_painted(vec![vec![1,5],vec![2,4]]), vec![4,0]);
    }
}

```

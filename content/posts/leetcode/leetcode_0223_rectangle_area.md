---
title: 223. rectangle area
date: '2021-11-09'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0223 rectangle area
---



Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2021/05/08/rectangle-plane.png)
>   Input: ax1 <TeX>=</TeX> -3, ay1 <TeX>=</TeX> 0, ax2 <TeX>=</TeX> 3, ay2 <TeX>=</TeX> 4, bx1 <TeX>=</TeX> 0, by1 <TeX>=</TeX> -1, bx2 <TeX>=</TeX> 9, by2 <TeX>=</TeX> 2
>   Output: 45
>   Example 2:
>   Input: ax1 <TeX>=</TeX> -2, ay1 <TeX>=</TeX> -2, ax2 <TeX>=</TeX> 2, ay2 <TeX>=</TeX> 2, bx1 <TeX>=</TeX> -2, by1 <TeX>=</TeX> -2, bx2 <TeX>=</TeX> 2, by2 <TeX>=</TeX> 2
>   Output: 16
**Constraints:**
>   	-10^4 <TeX>\leq</TeX> ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 <TeX>\leq</TeX> 10^4


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn compute_area(ax1: i32, ay1: i32, ax2: i32, ay2: i32, bx1: i32, by1: i32, bx2: i32, by2: i32) -> i32 {
let total_area = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1);
if ax1 == ax2 || ay1 == ay2 || bx1 == bx2 || by1 == by2 {
return total_area;
}
if ax2 <= bx1 || bx2  <= ax1 {
return total_area;
}
if ay2 <= by1 || by2  <= ay1 {
return total_area;
}

let x_right = i32::min(ax2, bx2);
let x_left = i32::max(ax1, bx1);

let y_up = i32::min(ay2, by2);
let y_down = i32::max(ay1, by1);
total_area - (x_right - x_left) * (y_up - y_down)
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_223() {
assert_eq!(Solution::compute_area(0, 0, 0, 0, 0, 0, 0, 0), 0);
assert_eq!(Solution::compute_area(-3, 0, 3, 4, 0, -1, 9, 2), 45);
assert_eq!(Solution::compute_area(-2, -2, 2, 2, -2, -2, 2, 2), 16);
assert_eq!(Solution::compute_area(-2, -2, 2, 2, -1, 4, 1, 6), 20);
}
}

```

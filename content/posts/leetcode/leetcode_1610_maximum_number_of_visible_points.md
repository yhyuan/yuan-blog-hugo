---
title: 1610. maximum number of visible points
date: '2022-08-18'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 1610 maximum number of visible points
---

 

  You are given an array points, an integer angle, and your location, where location <TeX>=</TeX> [posx, posy] and points[i] <TeX>=</TeX> [xi, yi] both denote integral coordinates on the X-Y plane.

  Initially, you are facing directly east from your position. You cannot move from your position, but you can rotate. In other words, posx and posy cannot be changed. Your field of view in degrees is represented by angle, determining how wide you can see from any given view direction. Let d be the amount in degrees that you rotate counterclockwise. Then, your field of view is the inclusive range of angles [d - angle/2, d + angle/2].

  

  

  

  You can see some set of points if, for each point, the angle formed by the point, your position, and the immediate east direction from your position is in your field of view.

  There can be multiple points at one coordinate. There may be points at your location, and you can always see these points regardless of your rotation. Points do not obstruct your vision to other points.

  Return the maximum number of points you can see.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/09/30/89a07e9b-00ab-4967-976a-c723b2aa8656.png)

 >   Input: points <TeX>=</TeX> [[2,1],[2,2],[3,3]], angle <TeX>=</TeX> 90, location <TeX>=</TeX> [1,1]

 >   Output: 3

 >   Explanation: The shaded region represents your field of view. All points can be made visible in your field of view, including [3,3] even though [2,2] is in front and in the same line of sight.

  

 >   Example 2:

  

 >   Input: points <TeX>=</TeX> [[2,1],[2,2],[3,4],[1,1]], angle <TeX>=</TeX> 90, location <TeX>=</TeX> [1,1]

 >   Output: 4

 >   Explanation: All points can be made visible in your field of view, including the one at your location.

  

 >   Example 3:

 >   ![](https://assets.leetcode.com/uploads/2020/09/30/5010bfd3-86e6-465f-ac64-e9df941d2e49.png)

 >   Input: points <TeX>=</TeX> [[1,0],[2,1]], angle <TeX>=</TeX> 13, location <TeX>=</TeX> [1,1]

 >   Output: 1

 >   Explanation: You can only see one of the two points, as shown above.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> points.length <TeX>\leq</TeX> 10^5

 >   	points[i].length <TeX>=</TeX><TeX>=</TeX> 2

 >   	location.length <TeX>=</TeX><TeX>=</TeX> 2

 >   	0 <TeX>\leq</TeX> angle < 360

 >   	0 <TeX>\leq</TeX> posx, posy, xi, yi <TeX>\leq</TeX> 100


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::f32::consts::PI;
impl Solution {
    pub fn is_inside_vision(angles: &Vec<(f32, i32, i32)>, angle: i32, j: usize, i: usize, location: (i32, i32)) -> bool {
        let (x3, y3) = location;
        let (angle1, x1, y1) = angles[i];
        let (angle2, x2, y2) = angles[j];
        if angle == 0 {
            return (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2);
        }
        (angle2 - angle1) < angle as f32
    }
    pub fn visible_points(points: Vec<Vec<i32>>, angle: i32, location: Vec<i32>) -> i32 {
        let x0 = location[0];
        let y0 = location[1];
        let mut angles: Vec<(f32, i32, i32)> = vec![];
        let n = points.len();
        let mut ans = 0;
        for i in 0..n {
            let x = points[i][0];
            let y = points[i][1];
            if x == x0 && y == y0 { // same location as obsevation. 
                ans += 1;
            } else if x == x0 {
                if y > y0 {
                    angles.push((90f32, x, y));
                } else {
                    angles.push((270f32, x, y));
                }
                continue;
            } else if x > x0 {
                let mut angle = ((y - y0 ) as f32 / (x - x0) as f32).atan() * 180f32 / PI;
                if angle < 0.0f32 {
                    angle += 360f32;
                }
                angles.push((angle, x, y));    
            } else { // x < x0
                let angle = ((y - y0 ) as f32 / (x - x0) as f32).atan() * 180f32 / PI;
                angles.push((angle + 180f32, x, y));
            }
        }
        //angles.sort();
        angles.sort_by(|a, b| a.partial_cmp(b).unwrap());
        let n = angles.len();
        if n == 0 {
            return ans;
        }
        if n == 1 {
            return ans + 1i32;
        }
        for i in 0..n {
            let (ang, x, y) = angles[i];
            angles.push((ang + 360f32, x, y));
        }
        let mut i = 0; // back pointer
        let mut j = 1; // front pointer
        let mut max_result = i32::MIN;
        println!("angles: {:?}", angles);
        while i < 2 * n {
            //move j forward until the angle differnce > angle. 
            //is_inside_vision(angles: &Vec<(f32, i32, i32)>, angle: i32, j: usize, i: usize, location: (i32, i32))
            //move j forward until the angle differnce > angle. 
            while j < 2 * n && angles[j % (2 * n)].0 - angles[i % (2 * n)].0 <= angle as f32 {
                j += 1;
            }
            println!("i: {}, j: {}", i, j);
            max_result = i32::max((j - i) as i32, max_result);
            i += 1;
        }
        max_result + ans
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1610() {
        assert_eq!(Solution::visible_points(vec![vec![2,1],vec![2,2],vec![3,4],vec![1,1], vec![1, 3], vec![-1, -2]], 90, vec![1,1]), 5);
        assert_eq!(Solution::visible_points(vec![vec![2,1],vec![2,2],vec![3,4],vec![1,1], vec![3, 3]], 0, vec![1,1]), 3);
        assert_eq!(Solution::visible_points(vec![vec![1,0],vec![2,1]], 13, vec![1,1]), 1);
        assert_eq!(Solution::visible_points(vec![vec![2,1],vec![2,2],vec![3,4],vec![1,1]], 90, vec![1,1]), 4);
    }
}

```

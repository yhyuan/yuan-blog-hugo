---
title: 2013. detect squares
date: '2022-09-03'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 2013 detect squares
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={2013}/>

You are given a stream of points on the X-Y plane. Design an algorithm that:



Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.

Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.

An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.



Implement the DetectSquares class:



DetectSquares() Initializes the object with an empty data structure.

void add(int[] point) Adds a new point point <TeX>=</TeX> [x, y] to the data structure.

int count(int[] point) Counts the number of ways to form axis-aligned squares with point point <TeX>=</TeX> [x, y] as described above.

 



 > Example 1:





 > Input

 > ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]

 > [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]

 > Output

 > [null, null, null, null, 1, 0, null, 2]



 > Explanation

 > DetectSquares detectSquares <TeX>=</TeX> new DetectSquares();

 > detectSquares.add([3, 10]);

 > detectSquares.add([11, 2]);

 > detectSquares.add([3, 2]);

 > detectSquares.count([11, 10]); // return 1. You can choose:

 >                                //   - The first, second, and third points

 > detectSquares.count([14, 8]);  // return 0. The query point cannot form a square with any points in the data structure.

 > detectSquares.add([11, 2]);    // Adding duplicate points is allowed.

 > detectSquares.count([11, 10]); // return 2. You can choose:

 >                                //   - The first, second, and third points

 >                                //   - The first, third, and fourth points

 



**Constraints:**



 > point.length <TeX>=</TeX><TeX>=</TeX> 2

 > 0 <TeX>\leq</TeX> x, y <TeX>\leq</TeX> 1000

 > At most 3000 calls in total will be made to add and count.


## Solution
### Rust
```rust
pub struct Solution {}

use std::collections::HashMap;

struct DetectSquares {
    x_hashmap: HashMap<i32, Vec<(i32, i32)>>,
    y_hashmap: HashMap<i32, Vec<(i32, i32)>>,
    count_hashmap: HashMap<(i32, i32), i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl DetectSquares {

    fn new() -> Self {
        let x_hashmap: HashMap<i32, Vec<(i32, i32)>> = HashMap::new();
        let y_hashmap: HashMap<i32, Vec<(i32, i32)>> = HashMap::new();
        let count_hashmap: HashMap<(i32, i32), i32> = HashMap::new();
        Self { x_hashmap, y_hashmap, count_hashmap}
    }
    
    fn add(&mut self, point: Vec<i32>) {
        let x = point[0];
        let y = point[1];
        if self.count_hashmap.contains_key(&(x ,y)) {
            *self.count_hashmap.get_mut(&(x ,y)).unwrap() += 1;
        } else {
            self.count_hashmap.insert((x ,y), 1);
        }
        if self.x_hashmap.contains_key(&x) {
            self.x_hashmap.get_mut(&x).unwrap().push((x, y));
        } else {
            self.x_hashmap.insert(x, vec![(x, y)]);
        }
        if self.y_hashmap.contains_key(&y) {
            self.y_hashmap.get_mut(&y).unwrap().push((x, y));
        } else {
            self.y_hashmap.insert(y, vec![(x, y)]);
        }
    }
    
    fn count(&self, point: Vec<i32>) -> i32 {
        let x = point[0];
        let y = point[1];
        if !self.x_hashmap.contains_key(&x) || !self.y_hashmap.contains_key(&y) {
            return 0;
        }
        let x_hashset = &self.x_hashmap[&x];
        let y_hashset = &self.y_hashmap[&y];

        let mut count = 0;
        for &(_, y1) in x_hashset.iter() {
            // (x, y), (x, y1), ()
            if y != y1 {
                let len = (y - y1).abs();
                // (x + len, y), (x + len, y1)
                // (x - len, y), (x - len, y1)
                if self.count_hashmap.contains_key(&(x + len, y)) && self.count_hashmap.contains_key(&(x + len, y1)) {
                    count += self.count_hashmap[&(x + len, y)] * self.count_hashmap[&(x + len, y1)];
                }
                if self.count_hashmap.contains_key(&(x - len, y)) && self.count_hashmap.contains_key(&(x - len, y1)) {
                    count += self.count_hashmap[&(x - len, y)] * self.count_hashmap[&(x - len, y1)];
                }
            }
        }
        count
    }
}
/**
 * Your DetectSquares object will be instantiated and called as such:
 * let obj = DetectSquares::new();
 * obj.add(point);
 * let ret_2: i32 = obj.count(point);
 */

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_2013() {
        
        let mut obj = DetectSquares::new();
        obj.add(vec![3, 10]);
        obj.add(vec![11, 2]);
        obj.add(vec![3, 2]);
        assert_eq!(obj.count(vec![11, 10]), 1);
        assert_eq!(obj.count(vec![14, 8]), 0);
        obj.add(vec![11, 2]);
        assert_eq!(obj.count(vec![11, 10]), 2);
        
        /*
        let mut obj = DetectSquares::new();
        obj.add(vec![5, 10]);
        obj.add(vec![10, 5]);
        obj.add(vec![10, 10]);
        assert_eq!(obj.count(vec![5, 5]), 1);

        obj.add(vec![3, 0]);
        obj.add(vec![8, 0]);
        obj.add(vec![8, 5]);
        assert_eq!(obj.count(vec![3, 5]), 1);

        obj.add(vec![3, 0]);
        obj.add(vec![8, 0]);
        obj.add(vec![8, 5]);
        assert_eq!(obj.count(vec![3, 5]), 1);
        */
    }
}

```

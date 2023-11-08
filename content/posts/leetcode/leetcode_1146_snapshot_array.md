---
title: 1146. snapshot array
date: '2022-07-14'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 1146 snapshot array
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1146}/>
 

  Implement a SnapshotArray that supports the following interface:

  

  

  	SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.

  	void set(index, val) sets the element at the given index to be equal to val.

  	int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.

  	int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id

  

  

   

 >   Example 1:

  

  

 >   Input: ["SnapshotArray","set","snap","set","get"]

 >   [[3],[0,5],[],[0,6],[0,0]]

 >   Output: [null,null,0,null,5]

 >   Explanation: 

 >   SnapshotArray snapshotArr <TeX>=</TeX> new SnapshotArray(3); // set the length to be 3

 >   snapshotArr.set(0,5);  // Set array[0] <TeX>=</TeX> 5

 >   snapshotArr.snap();  // Take a snapshot, return snap_id <TeX>=</TeX> 0

 >   snapshotArr.set(0,6);

 >   snapshotArr.get(0,0);  // Get the value of array[0] with snap_id <TeX>=</TeX> 0, return 5

  

   

  **Constraints:**

  

  

 >   	1 <TeX>\leq</TeX> length <TeX>\leq</TeX> 50000

 >   	At most 50000 calls will be made to set, snap, and get.

 >   	0 <TeX>\leq</TeX> index < length

 >   	0 <TeX>\leq</TeX> snap_id < (the total number of times we call snap())

 >   	0 <TeX>\leq</TeX> val <TeX>\leq</TeX> 10^9


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;

struct SnapshotArray {
    // snaps: Vec<Vec<i32>>,
    changes: Vec<HashMap<usize, i32>>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SnapshotArray {

    fn new(length: i32) -> Self {
        /*
        let snaps = vec![vec![0; length as usize]];
        Self { snaps }
        */
        let changes: Vec<HashMap<usize, i32>> = vec![HashMap::new()];
        Self { changes }
    }
    
    fn set(&mut self, index: i32, val: i32) {
        /*
        let n = self.snaps.len();
        self.snaps[n - 1][index as usize] = val;
        */
        let n = self.changes.len();
        self.changes[n - 1].insert(index as usize, val);
    }
    
    fn snap(&mut self) -> i32 {
        /*
        let new_snap = self.snaps[self.snaps.len() - 1].clone();
        self.snaps.push(new_snap);
        return self.snaps.len() as i32 - 2;
        */
        let new_hashmap = self.changes[self.changes.len() - 1].clone();
        self.changes.push(new_hashmap);
        return self.changes.len() as i32 - 2;
    }
    
    fn get(&self, index: i32, snap_id: i32) -> i32 {
        //self.snaps[snap_id as usize][index as usize]   
        let index = index as usize;
        let hashmap = &self.changes[snap_id as usize];
        if hashmap.contains_key(&index) {
            return *hashmap.get(&index).unwrap();
        }
        0
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * let obj = SnapshotArray::new(length);
 * obj.set(index, val);
 * let ret_2: i32 = obj.snap();
 * let ret_3: i32 = obj.get(index, snap_id);
 */

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1146() {
        let mut obj = SnapshotArray::new(3);
        obj.set(0, 5);
        assert_eq!(obj.snap(), 0);
        obj.set(0, 6);
        assert_eq!(obj.get(0, 0), 5);
    }
}

```

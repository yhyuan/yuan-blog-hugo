---
title: 295. find median from data stream
date: '2021-12-23'
tags: ['leetcode', 'rust', 'python', 'hard']
draft: false
description: Solution for leetcode 0295 find median from data stream
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={295}/>
 

  The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

  

  	For example, for arr <TeX>=</TeX> [2,3,4], the median is 3.

  	For example, for arr <TeX>=</TeX> [2,3], the median is (2 + 3) / 2 <TeX>=</TeX> 2.5.

  

  Implement the MedianFinder class:

  

  	MedianFinder() initializes the MedianFinder object.

  	void addNum(int num) adds the integer num from the data stream to the data structure.

  	double findMedian() returns the median of all elements so far. Answers within 10^-5 of the actual answer will be accepted.

  

   

 >   Example 1:

  

 >   Input

 >   ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]

 >   [[], [1], [2], [], [3], []]

 >   Output

 >   [null, null, null, 1.5, null, 2.0]

 >   Explanation

 >   MedianFinder medianFinder <TeX>=</TeX> new MedianFinder();

 >   medianFinder.addNum(1);    // arr <TeX>=</TeX> [1]

 >   medianFinder.addNum(2);    // arr <TeX>=</TeX> [1, 2]

 >   medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)

 >   medianFinder.addNum(3);    // arr[1, 2, 3]

 >   medianFinder.findMedian(); // return 2.0

  

   

  **Constraints:**

  

 >   	-10^5 <TeX>\leq</TeX> num <TeX>\leq</TeX> 10^5

 >   	There will be at least one element in the data structure before calling findMedian.

 >   	At most 5  10^4 calls will be made to addNum and findMedian.

  

   

 >   Follow up:

  

 >   	If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

 >   	If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?


## Solution
We can use the max heap to store the smaller half of the numbers and use the min Heap to store the largest half of the numbers. If the total size is not even, the min Heap will have one more number. 

The calculation of median is easy. If the size is even, we can simply check the max value in the max heap and min value in min heap and calculate their average. If the size is odd, we can check the min value in min heap. The time complexity is O(1)

The add number is a little bit complicated. 

We firstly add the num to the heap according to its relationship between minHeap[0]. If it is larger than minHeap[0], put it in minHeap. Otherwise, put it in maxHeap. 

Rebalance the maxHeap and minHeap. If the counts are same or the minHeap has one more than the maxHeap, we will simply return because the two heaps are balanced. Otherwise, we can either pop one value out of max heap or min heap and put it in another heap to maintain the balance. 

Now we can maintain that the numbers in the min heap and max heap have same count or the count in min heap is only one more number than the max heap.

### Python
```python
class MedianFinder:
  def __init__(self):
    self.maxHeap = []
    self.minHeap = []
    self.count = 0
  
  def rebalance(self):
    minHeapLen = len(self.minHeap)
    maxHeapLen = len(self.maxHeap)
    if minHeapLen == maxHeapLen or minHeapLen == maxHeapLen + 1:
      return
    if minHeapLen < maxHeapLen:
      val = heappop(self.maxHeap)
      heappush(self.minHeap, -val)
    if minHeapLen > maxHeapLen + 1:
      val = heappop(self.minHeap)
      heappush(self.maxHeap, -val)        
    return      

  def addNum(self, num: int) -> None:
    if len(self.minHeap) == 0 or num > self.minHeap[0]: # larger value
      heappush(self.minHeap, num)
    else:
      heappush(self.maxHeap, -num)
    self.count += 1      
    self.rebalance()
        
  def findMedian(self) -> float:
    if self.count % 2 == 0:
      return (self.minHeap[0] + (-self.maxHeap[0])) * 0.5
    return self.minHeap[0]
```
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::BinaryHeap;
struct MedianFinder {
    large_heap: BinaryHeap<i32>,
    small_heap: BinaryHeap<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MedianFinder {

    /** initialize your data structure here. */
    fn new() -> Self {
        let large_heap: BinaryHeap<i32> = BinaryHeap::new();//reverse 
        let small_heap: BinaryHeap<i32> = BinaryHeap::new();
        Self{small_heap, large_heap}
    }
    
    fn add_num(&mut self, num: i32) {
        if self.large_heap.len() == self.small_heap.len() {
            //add to small
            if self.small_heap.len() == 0 {
                self.small_heap.push(num);
                return;
            }
            let small_heap_max_val = *self.small_heap.peek().unwrap();
            if num < small_heap_max_val {
                self.small_heap.push(num);
            } else {
                self.large_heap.push(-num);
                let large_heap_min_val = -self.large_heap.pop().unwrap();
                self.small_heap.push(large_heap_min_val);
            }
        } else {
            let small_heap_max_val = *self.small_heap.peek().unwrap();
            if num < small_heap_max_val {
                self.small_heap.push(num);
                let small_val = self.small_heap.pop().unwrap();
                self.large_heap.push(-small_val);
            } else {
                self.large_heap.push(-num);
            }
        }
    }
    
    fn find_median(&self) -> f64 {
        if self.large_heap.len() == self.small_heap.len() {
            let large_val = -(*self.large_heap.peek().unwrap());
            let small_val = *self.small_heap.peek().unwrap();
            (large_val as f64 + small_val as f64) * 0.5f64
        } else {
            let small_val = *self.small_heap.peek().unwrap();
            small_val as f64
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * let obj = MedianFinder::new();
 * obj.add_num(num);
 * let ret_2: f64 = obj.find_median();
 */

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_295() {
        let mut obj = MedianFinder::new();
        obj.add_num(1);
        obj.add_num(2);
        assert_eq!(obj.find_median(), 1.5);
        obj.add_num(3);
        assert_eq!(obj.find_median(), 2_f64);
    }
}

```

---
title: Pattern 2 Two Heaps
date: '2022-10-29'
tags: ['leetcode', 'pattern']
draft: false
description: Pattern 2 Two Heaps
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

# Introduction
This pattern aims to address quickly calculate the median value of a data stream. We will need to two heaps: Min Heap and MaxHeap. Min Heap is used to store the half of larger values, while max heap is ued to store the half of the smaller values. If the total number of elements is odd, the min Heap will have one more value than the max Heap. 

If these two heaps are maintained successfully, the calucation of the median value becomes very simple. If the count is even, we will be the min value of the min Heap and the max value of the max and calculate the mean as the median value. If the count is odd, we can simple extract the heap of the min Heap. 

Now we are going to discuss how to maintain these two heaps. 
1) compare the num with the heap top of min Heap. If it is larger or currently there is no number in these two heaps, push it to minHeap. Otherwise, push the number to the maxHeap. 
2) Now we will use a function called balance to rebalance the elements in the two heaps. 
3) If the difference is 0 or 1, we can simply ignore it. If the number in the min Heap is smaller than the number in the max Heap, we should pop value in the max Heap and push it back to the min Heap. Otherwise, we should pop the value in the min Heap and push it back the max Heap. 

## Problem solving boilerplate code
````python
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        self.count = 0
  
    def balance(self):
        if len(self.minHeap) == len(self.maxHeap) or len(self.minHeap) == len(self.maxHeap) + 1:
            return
        if len(self.minHeap) < len(self.maxHeap):
            val = heappop(self.maxHeap)
            heappush(self.minHeap, -val)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = heappop(self.minHeap)
            heappush(self.maxHeap, -val)        
        return      

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == 0 or num > self.minHeap[0]: # larger value
            heappush(self.minHeap, num)
        else:
            heappush(self.maxHeap, -num)
        self.count += 1      
        self.balance()      
        
    def findMedian(self) -> float:
        if self.count % 2 == 0:
            return (self.minHeap[0] + (-self.maxHeap[0])) * 0.5
        return self.minHeap[0]
````


## Problems
<LeetCode.ProblemCard id={295}/>
<LeetCode.ProblemCard id={480}/>
<LeetCode.ProblemCard id={502}/>
<LeetCode.ProblemCard id={436}/>
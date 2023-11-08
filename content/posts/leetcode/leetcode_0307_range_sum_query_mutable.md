---
title: 307. range sum query mutable
date: '2022-01-01'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0307 range sum query mutable
---



Given an integer array nums, handle multiple queries of the following types:

<ol>

Update the value of an element in nums.

Calculate the sum of the elements of nums between indices left and right inclusive where left <TeX>\leq</TeX> right.

</ol>

Implement the NumArray class:



NumArray(int[] nums) Initializes the object with the integer array nums.

void update(int index, int val) Updates the value of nums[index] to be val.

int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).





>   Example 1:
>   Input
>   ["NumArray", "sumRange", "update", "sumRange"]
>   [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
>   Output
>   [null, 9, null, 8]
>   Explanation
>   NumArray numArray <TeX>=</TeX> new NumArray([1, 3, 5]);
>   numArray.sumRange(0, 2); // return 1 + 3 + 5 <TeX>=</TeX> 9
>   numArray.update(1, 2);   // nums <TeX>=</TeX> [1, 2, 5]
>   numArray.sumRange(0, 2); // return 1 + 2 + 5 <TeX>=</TeX> 8
**Constraints:**
>   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 3  10^4
>   	-100 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 100
>   	0 <TeX>\leq</TeX> index < nums.length
>   	-100 <TeX>\leq</TeX> val <TeX>\leq</TeX> 100
>   	0 <TeX>\leq</TeX> left <TeX>\leq</TeX> right < nums.length
>   	At most 3  10^4 calls will be made to update and sumRange.


## Solution
Build Segment Tree:

lo == hi: self.tree[treeIndex] = nums[lo];

otherwise, mid = (lo + hi) // 2. [lo, mid], [mid + 1, hi] for left (2 * index + 1) and right (2 * index + 2) branch.

Update Segment Tree:

lo == hi: self.tree[treeIndex] = newVal

otherwise mid = (lo + hi) // 2. ArrIndex > mid, then, update the right, otherwise, update left.



### Python
```rust


#https://leetcode.com/tag/segment-tree/
import math
class NumArray:
def __init__(self, nums: List[int]):
n = len(nums)
self.n = n
k = math.ceil(math.log2(n))
self.tree=[0] * (int(math.pow(2, k + 1)) - 1)
def buildSegTree(arr, treeIndex, lo, hi):
if (lo == hi):
self.tree[treeIndex] = arr[lo]
return;
mid = (hi + lo) // 2
left = 2 * treeIndex + 1
right = 2 * treeIndex + 2
buildSegTree(arr, left, lo, mid)
buildSegTree(arr, right, mid + 1, hi)
def merge(left, right):
return left + right
self.tree[treeIndex] = merge(self.tree[left], self.tree[right]);
return
buildSegTree(nums, 0, 0, n - 1)


def update(self, index: int, val: int) -> None:
def updateTree(treeIndex, lo, hi, arrIndex, val):
if (lo == hi):
self.tree[treeIndex] = val
return
mid = (lo + hi) // 2
left = 2 * treeIndex + 1
right = 2 * treeIndex + 2
if (arrIndex > mid):
updateTree(right, mid + 1, hi, arrIndex, val)
if (arrIndex <= mid):
updateTree(left, lo, mid, arrIndex, val)
def merge(left, right):
return left + right
self.tree[treeIndex] = merge(self.tree[left], self.tree[right])
updateTree(0, 0, self.n - 1, index, val)

def sumRange(self, left: int, right: int) -> int:
def queryTree(treeIndex, lo, hi, i, j):
if lo > j or hi < i: # No intersection
return 0
if i <= lo and j >= hi: # [i, j] is inside [lo, hi]
return self.tree[treeIndex]
mid = (lo + hi) // 2
left = 2 * treeIndex + 1
right = 2 * treeIndex + 2
if i > mid: # on the right of the mid
return queryTree(right, mid + 1, hi, i, j)
if j <= mid:


# on the left of the mid
return queryTree(left, lo, mid, i, j)

leftQuery = queryTree(left, lo, mid, i, mid);
rightQuery = queryTree(right, mid + 1, hi, mid + 1, j);
def merge(left, right):
return left + right
return merge(leftQuery, rightQuery);

return queryTree(0, 0, self.n - 1, left, right)
```


### Rust
```rust
pub struct Solution {}


// submission codes start here

struct NumArray {
totals: Vec<i32>
}


/**
* `&self` means the method takes an immutable reference.
* If you need a mutable reference, change it to `&mut self` instead.
*/
impl NumArray {

fn new(nums: Vec<i32>) -> Self {
let mut totals: Vec<i32> = vec![];
let mut total = 0i32;
for &num in nums.iter() {
total += num;
totals.push(total);
}
NumArray{totals: totals}
}

fn update(&mut self, index: i32, val: i32) {
let index = index as usize;
let previous_val = if index == 0 {self.totals[0]} else {self.totals[index] - self.totals[index - 1]};
let diff = val - previous_val;
for i in index..self.totals.len() {
self.totals[i] = self.totals[i] + diff;
}
}

fn sum_range(&self, left: i32, right: i32) -> i32 {
let left = left as usize;
let right = right as usize;
if left == 0 {
self.totals[right]
} else {
self.totals[right] - self.totals[left - 1]
}
}
}

/**
* Your NumArray object will be instantiated and called as such:
* let obj = NumArray::new(nums);
* obj.update(index, val);
* let ret_2: i32 = obj.sum_range(left, right);
*/

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_307() {
let _empty = NumArray::new(vec![]);
let mut tree = NumArray::new(vec![1, 1, 1, 1, 1, 1, 1, 1, 1, 1]);
assert_eq!(tree.sum_range(0, 6), 7);
tree.update(0, 2);
assert_eq!(tree.sum_range(0, 6), 8);
tree.update(1, 2);
assert_eq!(tree.sum_range(0, 2), 5);
tree.update(6, 10);
assert_eq!(tree.sum_range(6, 6), 10);
}
}

```

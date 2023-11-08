---
title: 852. peak index in a mountain array
date: '2022-05-31'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0852 peak index in a mountain array
---

 

  Let's call an array arr a mountain if the following properties hold:

  

  	arr.length ><TeX>=</TeX> 3

  	There exists some i with 0 < i < arr.length - 1 such that:

  	

  		arr[0] < arr[1] < ... arr[i-1] < arr[i] 

  		arr[i] > arr[i+1] > ... > arr[arr.length - 1]

  	

  	

  

  Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

   

 >   Example 1:

 >   Input: arr <TeX>=</TeX> [0,1,0]

 >   Output: 1

 >   Example 2:

 >   Input: arr <TeX>=</TeX> [0,2,1,0]

 >   Output: 1

 >   Example 3:

 >   Input: arr <TeX>=</TeX> [0,10,5,2]

 >   Output: 1

 >   Example 4:

 >   Input: arr <TeX>=</TeX> [3,4,5,1]

 >   Output: 2

 >   Example 5:

 >   Input: arr <TeX>=</TeX> [24,69,100,99,79,78,67,36,26,19]

 >   Output: 2

   

  **Constraints:**

  

 >   	3 <TeX>\leq</TeX> arr.length <TeX>\leq</TeX> 10^4

 >   	0 <TeX>\leq</TeX> arr[i] <TeX>\leq</TeX> 10^6

 >   	arr is guaranteed to be a mountain array.

  

   

 >   Follow up: Finding the O(n) is straightforward, could you find an O(log(n)) solution?


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn peak_index_in_mountain_array(arr: Vec<i32>) -> i32 {
        let mut low = 0;
        let mut high = arr.len();
        while low + 1 < high {
            let mid= low + (high - low) / 2;
            if arr[mid] > arr[mid - 1] && arr[mid] > arr[mid + 1]{
                return mid as i32;
            }
            if arr[mid] > arr[mid - 1] {
                low = mid;
            } else {
                high = mid;
            }
        }
        if arr[low] > arr[low - 1] && arr[low] > arr[low + 1]{
            return low as i32;
        }
        if arr[high] > arr[high - 1] && arr[high] > arr[high + 1]{
            return high as i32;
        }

        -1
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_852() {
        assert_eq!(Solution::peak_index_in_mountain_array(vec![0,1,0]), 1);
        assert_eq!(Solution::peak_index_in_mountain_array(vec![0,2,1,0]), 1);
        assert_eq!(Solution::peak_index_in_mountain_array(vec![0,10,5,2]), 1);
    }
}

```

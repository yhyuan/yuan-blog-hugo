---
title: 4. median of two sorted arrays
date: '2021-05-05'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0004 median of two sorted arrays
---

 

  Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

  The overall run time complexity should be O(log (m+n)).

   

 >   Example 1:

  

 >   Input: nums1 <TeX>=</TeX> [1,3], nums2 <TeX>=</TeX> [2]

 >   Output: 2.00000

 >   Explanation: merged array <TeX>=</TeX> [1,2,3] and median is 2.

  

 >   Example 2:

  

 >   Input: nums1 <TeX>=</TeX> [1,2], nums2 <TeX>=</TeX> [3,4]

 >   Output: 2.50000

 >   Explanation: merged array <TeX>=</TeX> [1,2,3,4] and median is (2 + 3) / 2 <TeX>=</TeX> 2.5.

  

 >   Example 3:

  

 >   Input: nums1 <TeX>=</TeX> [0,0], nums2 <TeX>=</TeX> [0,0]

 >   Output: 0.00000

  

 >   Example 4:

  

 >   Input: nums1 <TeX>=</TeX> [], nums2 <TeX>=</TeX> [1]

 >   Output: 1.00000

  

 >   Example 5:

  

 >   Input: nums1 <TeX>=</TeX> [2], nums2 <TeX>=</TeX> []

 >   Output: 2.00000

  

   

  **Constraints:**

  

 >   	nums1.length <TeX>=</TeX><TeX>=</TeX> m

 >   	nums2.length <TeX>=</TeX><TeX>=</TeX> n

 >   	0 <TeX>\leq</TeX> m <TeX>\leq</TeX> 1000

 >   	0 <TeX>\leq</TeX> n <TeX>\leq</TeX> 1000

 >   	1 <TeX>\leq</TeX> m + n <TeX>\leq</TeX> 2000

 >   	-10^6 <TeX>\leq</TeX> nums1[i], nums2[i] <TeX>\leq</TeX> 10^6


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
    pub fn find_median_one_sorted_array(nums: &Vec<i32>) -> f64 {
        let n = nums.len();
        let n_2 = n / 2;
        if n % 2 == 1 {
            nums[n_2] as f64
        } else {
            0.5f64 * ((nums[n_2] + nums[n_2 - 1]) as f64)
        }
    }
    pub fn find_median_two_separated_sorted_array(nums1: &Vec<i32>, nums2: &Vec<i32>) -> f64 {
        let m = nums1.len();
        let n = nums2.len();
        let middle = (m + n) / 2;
        let median = if middle < m {
            nums1[middle] as f64
        } else {
            nums2[middle - m]  as f64
        };
        if (m + n) % 2 == 1 {
            return median;
        } 
        let median_1 = if middle - 1 < m {
            nums1[middle - 1] as f64
        } else {
            nums2[middle - 1 - m]  as f64
        };
        return 0.5f64 * (median + median_1);
    }
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        if nums1.len() == 0 {
            return Solution::find_median_one_sorted_array(&nums2);
        }
        if nums2.len() == 0 {
            return Solution::find_median_one_sorted_array(&nums1);
        }
        if nums1[nums1.len() - 1] <= nums2[0] {
            return Solution::find_median_two_separated_sorted_array(&nums1, &nums2);
        }
        if nums2[nums2.len() - 1] <= nums1[0] {
            return Solution::find_median_two_separated_sorted_array(&nums2, &nums1);
        }
        let m = nums1.len();
        let n = nums2.len();
        let middle = (m + n) / 2;
        let mut i = 0usize;
        let mut j = 0usize;
        let mut pre_median = i32::MIN;
        let mut median = i32::MIN;
        while i + j <= middle {
            if i < nums1.len() && j < nums2.len() {
                if nums1[i] <= nums2[j] {
                    pre_median = median;
                    median = nums1[i];
                    i = i + 1;
                } else {
                    pre_median = median;
                    median = nums2[j];
                    j = j + 1;
                }    
            } else if i == nums1.len() {
                pre_median = median;
                median = nums2[j];
                j = j + 1;
            } else if j == nums2.len() {
                pre_median = median;
                median = nums1[i];
                i = i + 1;
            } else {
                panic!("Wrong data!");
            }
        }
        //println!("pre_median: {}", pre_median);
        //println!("median: {}", median);
        if (m + n) % 2 == 1 {
            median as f64
        } else {
            0.5f64 * (median as f64 + pre_median as f64)
        }
    }
}
*/
impl Solution {
    pub fn find_median_one_sorted_array(nums: &Vec<i32>) -> f64 {
        let n = nums.len();
        let n_2 = n / 2;
        if n % 2 == 1 {
            nums[n_2] as f64
        } else {
            0.5f64 * ((nums[n_2] + nums[n_2 - 1]) as f64)
        }
    }
    pub fn find_kth_number(nums1: &Vec<i32>, start_1: usize, end_1: usize, nums2: &Vec<i32>, start_2: usize, end_2: usize, k: usize) -> i32 {
        //println!("nums1: {:?}, nums2: {:?}, k: {}", &nums1[start_1..=end_1], &nums2[start_2..=end_2], k);
        if end_1 < start_1 {
            return nums2[start_2 + k - 1];
        }
        if end_2 < start_2 {
            return nums1[start_1 + k - 1];
        }
        if k == 1 { //end1 > start1, end2 > start2
            return i32::min(nums1[start_1], nums2[start_2]);
        }
        //start1 + k/2 - 1
        let index_1 = usize::min(start_1 + k/2 - 1, end_1);
        let index_2 = usize::min(start_2 + k/2 - 1, end_2);
        if nums1[index_1] > nums2[index_2] {
            if index_2 == end_2 {
                Solution::find_kth_number(nums1, start_1, end_1, nums2, start_2 + k/2, end_2, k - (end_2 - start_2 + 1))
            } else {
                Solution::find_kth_number(nums1, start_1, end_1, nums2, start_2 + k/2, end_2, k - k/2)
            }
        } else {
            if index_1 == end_1 {
                Solution::find_kth_number(nums1, start_1 + k/2, end_1, nums2, start_2, end_2, k - (end_1 - start_1 + 1))
            } else {
                Solution::find_kth_number(nums1, start_1 + k/2, end_1, nums2, start_2, end_2, k - k/2)
            }
        }
    }
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let m = nums1.len();
        let n = nums2.len();
        if m == 0 {
            return Solution::find_median_one_sorted_array(&nums2);
        }
        if n == 0 {
            return Solution::find_median_one_sorted_array(&nums1);
        }

        let val = Solution::find_kth_number(&nums1, 0, m - 1, &nums2, 0, n - 1, (m + n)/2 + 1);
        //println!("The {} th number is {}", (m + n) / 2, val);

        if  (m + n) % 2 == 1 {
            val as f64
        } else {
            let val2 = Solution::find_kth_number(&nums1, 0, m - 1, &nums2, 0, n - 1, (m + n)/2);
            0.5f64 * ((val + val2) as f64)
        }
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_4() {
        assert_eq!(
            Solution::find_median_sorted_arrays(
                vec![1, 3, 4, 9], 
                vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            4.5
        );
        assert_eq!(
            Solution::find_median_sorted_arrays(vec![1, 3], vec![2, 4]),
            2.5
        );
        assert_eq!(
            Solution::find_kth_number(&vec![1, 3], 0, 1, &vec![2], 0, 0, 2),
            2
        );
        assert_eq!(
            Solution::find_median_sorted_arrays(vec![1, 3], vec![2]),
            2.0
        );
        assert_eq!(
            Solution::find_median_sorted_arrays(vec![1, 2], vec![3, 4]),
            2.5
        );
        assert_eq!(
            Solution::find_median_sorted_arrays(vec![1], vec![2, 3, 4, 5, 6]),
            3.5
        );
    }
}

```

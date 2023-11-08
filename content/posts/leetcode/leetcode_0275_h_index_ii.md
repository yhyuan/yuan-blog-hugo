---
title: 275. h index ii
date: '2021-12-12'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0275 h index ii
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={275}/>
 

  Given an array of integers citations where citations[i] is the number of citations a researcher received for their i^th paper and citations is sorted in an ascending order, return compute the researcher's h-index.

  According to the [definition of h-index on Wikipedia](https://en.wikipedia.org/wiki/H-index): A scientist has an index h if h of their n papers have at least h citations each, and the other n - h papers have no more than h citations each.

  If there are several possible values for h, the maximum one is taken as the h-index.

  You must write an algorithm that runs in logarithmic time.

   

 >   Example 1:

  

 >   Input: citations <TeX>=</TeX> [0,1,3,5,6]

 >   Output: 3

 >   Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had received 0, 1, 3, 5, 6 citations respectively.

 >   Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

  

 >   Example 2:

  

 >   Input: citations <TeX>=</TeX> [1,2,100]

 >   Output: 2

  

   

  **Constraints:**

  

 >   	n <TeX>=</TeX><TeX>=</TeX> citations.length

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 10^5

 >   	0 <TeX>\leq</TeX> citations[i] <TeX>\leq</TeX> 1000

 >   	citations is sorted in ascending order.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn is_h_index(citations: &Vec<i32>, index: usize) -> bool {
        let n = citations.len();
        if (n - index) >= citations[index] as usize {
            true
        } else {
            false
        }
    }

    pub fn h_index(citations: Vec<i32>) -> i32 {
        /*
        let n = citations.len();
        if Solution::is_h_index(&citations, begin) {
            return (n - begin) as i32;
        }
        */
        /*
        if Solution::is_h_index(&citations, end) {
            return (n - end) as i32;
        }
        */
        //let size = (citations.len() - begin) as i32;
        /*
        println!("begin: {}, end: {}", begin, end);
        begin as i32
        */
        /*
        let n = citations.len();
        if citations[0] >= citations.len() as i32 {
            return citations.len() as i32;
        }
        for i in (0..n).rev() {
            let val = i32::min((n - i) as i32, citations[i]);
            if val >= (n - i) as i32 {
                return val;
            }
        }
        return 0i32;
        */
        let n = citations.len();
        let mut begin = 0usize;
        let mut end = n;
        while begin + 1 < end {
            let mid = begin + (end - begin) / 2;
            let size = (n - mid) as i32;
            if size >= citations[mid] {
                begin = mid;
            } else {
                end = mid;
            }
        }
        println!("begin: {}, end: {}", begin, end);
        let v1 = i32::min(citations[begin] as i32, (n - begin) as i32);
        let v2 = i32::min(citations[end] as i32, (n - end) as i32);
        //i32::max(v1, v2)
        //i32::min(citations[begin] as i32, (n - begin) as i32)
        v1
        /*
        for i in 0..n {
            let count = n - i; // >= citations[i] 's count
            let citation = citations[i] as usize;
            if citation >= count {
                return  i32::min(citation as i32, count as i32);
            }
        }
        0i32
        */
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_275() {
        
        assert_eq!(Solution::h_index(vec![0,1,3,5,6]), 3);
        assert_eq!(Solution::h_index(vec![1,2,100]), 2);
        assert_eq!(Solution::h_index(vec![100]), 1);
        assert_eq!(Solution::h_index(vec![0]), 0);
        assert_eq!(Solution::h_index(vec![0, 1]), 1);
        assert_eq!(Solution::h_index(vec![0, 0, 1]), 1);
        
        assert_eq!(Solution::h_index(vec![0, 0, 4, 4]), 2);
    }
}

```

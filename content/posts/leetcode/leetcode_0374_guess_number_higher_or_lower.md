---
title: 374. guess number higher or lower
date: '2022-02-02'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0374 guess number higher or lower
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={374}/>
 

  We are playing the Guess Game. The game is as follows:

  I pick a number from 1 to n. You have to guess which number I picked.

  Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

  You call a pre-defined API int guess(int num), which returns 3 possible results:

  

  	-1: The number I picked is lower than your guess (i.e. pick < num).

  	1: The number I picked is higher than your guess (i.e. pick > num).

  	0: The number I picked is equal to your guess (i.e. pick <TeX>=</TeX><TeX>=</TeX> num).

  

  Return the number that I picked.

   

 >   Example 1:

 >   Input: n <TeX>=</TeX> 10, pick <TeX>=</TeX> 6

 >   Output: 6

 >   Example 2:

 >   Input: n <TeX>=</TeX> 1, pick <TeX>=</TeX> 1

 >   Output: 1

 >   Example 3:

 >   Input: n <TeX>=</TeX> 2, pick <TeX>=</TeX> 1

 >   Output: 1

 >   Example 4:

 >   Input: n <TeX>=</TeX> 2, pick <TeX>=</TeX> 2

 >   Output: 2

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 2^31 - 1

 >   	1 <TeX>\leq</TeX> pick <TeX>\leq</TeX> n


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * unsafe fn guess(num: i32) -> i32 {}
 */
/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * unsafe fn guess(num: i32) -> i32 {}
 */
unsafe fn guess(num: i32) -> i32 {
    0i32
}
impl Solution {
    unsafe fn guessNumber(n: i32) -> i32 {
        let mut low = 1;
        let mut high = n;
        while low + 1 < high {
            let mid = low + (high - low) / 2;
            let r = guess(mid);
            if r == 0 {
                return mid;
            }
            if r == -1 {
                high = mid - 1;
            }
            if r == 1 {
                low = mid + 1
            }
        }
        if guess(low) == 0 {
            return low;
        }
        if guess(high) == 0 {
            return high;
        }
        
        -1
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_374() {
    }
}

```

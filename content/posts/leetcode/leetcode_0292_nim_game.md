---
title: 292. nim game
date: '2021-12-21'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0292 nim game
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={292}/>
 

  You are playing the following Nim Game with your friend:

  

  	Initially, there is a heap of stones on the table.

  	You and your friend will alternate taking turns, and you go first.

  	On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.

  	The one who removes the last stone is the winner.

  

  Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.

   

 >   Example 1:

  

 >   Input: n <TeX>=</TeX> 4

 >   Output: false

 >   Explanation: These are the possible outcomes:

 >   1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins.

 >   2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins.

 >   3. You remove 3 stones. Your friend removes the last stone. Your friend wins.

 >   In all outcomes, your friend wins.

  

 >   Example 2:

  

 >   Input: n <TeX>=</TeX> 1

 >   Output: true

  

 >   Example 3:

  

 >   Input: n <TeX>=</TeX> 2

 >   Output: true

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 2^31 - 1


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn can_win_nim(n: i32) -> bool {
        n % 4 != 0
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_292() {
        assert_eq!(Solution::can_win_nim(4), false);
    }
}

```

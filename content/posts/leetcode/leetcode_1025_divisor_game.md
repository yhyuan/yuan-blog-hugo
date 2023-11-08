---
title: 1025. divisor game
date: '2022-07-01'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1025 divisor game
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1025}/>
 

  Alice and Bob take turns playing a game, with Alice starting first.

  Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

  

  	Choosing any x with 0 < x < n and n % x <TeX>=</TeX><TeX>=</TeX> 0.

  	Replacing the number n on the chalkboard with n - x.

  

  Also, if a player cannot make a move, they lose the game.

  Return true if and only if Alice wins the game, assuming both players play optimally.

   

 >   Example 1:

  

 >   Input: n <TeX>=</TeX> 2

 >   Output: true

 >   Explanation: Alice chooses 1, and Bob has no more moves.

  

 >   Example 2:

  

 >   Input: n <TeX>=</TeX> 3

 >   Output: false

 >   Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 1000


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

use std::collections::HashMap;
impl Solution {
    pub fn divisor_game_helper(n: i32, is_alice_playing: bool, memo: &mut HashMap<(bool, i32), bool>) -> bool {
        //println!("n: {}, is_alice: {}", n, is_alice_playing);
        if memo.contains_key(&(is_alice_playing, n)) {
            return memo[&(is_alice_playing, n)];
        }
        if is_alice_playing {
            for x in 1..n { // 0 < x < n 
                if n % x == 0 {
                    let res = Self::divisor_game_helper(n - x, !is_alice_playing, memo);
                    if res {
                        memo.insert((is_alice_playing, n), true);
                        return true;
                    }
                }
            }
            memo.insert((is_alice_playing, n), false);
            return false;            
        }

        for x in 1..n { // 0 < x < n 
            if n % x == 0 {
                let res = Self::divisor_game_helper(n - x, !is_alice_playing, memo);
                if !res {
                    memo.insert((is_alice_playing, n), false);
                    return false;
                }
            }
        }
        memo.insert((is_alice_playing, n), true);
        return true;            
    }
    pub fn divisor_game(n: i32) -> bool {
        let mut memo: HashMap<(bool, i32), bool> = HashMap::new();
        memo.insert((false, 1), true);
        memo.insert((true, 1), false);
        let res = Self::divisor_game_helper(n, true, &mut memo);
        //println!("memo: {:?}", memo);
        res
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1025() {
    }
}

```

---
title: 486. predict the winner
date: '2022-03-14'
tags: ['leetcode', 'rust', 'python', 'medium']
draft: false
description: Solution for leetcode 0486 predict the winner
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={486}/>
 

  You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

  Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.

  Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume that both players are playing optimally.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [1,5,2]

 >   Output: false

 >   Explanation: Initially, player 1 can choose between 1 and 2. 

 >   If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 

 >   So, final score of player 1 is 1 + 2 <TeX>=</TeX> 3, and player 2 is 5. 

 >   Hence, player 1 will never be the winner and you need to return false.

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [1,5,233,7]

 >   Output: true

 >   Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.

 >   Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 20

 >   	0 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^7


## Solution
Solution: let's define dp[i, j, isPlayer1] as the scores for player 1 and player 2 for subarray [i, j] if is Player 1 is playing or not. So the final result dp[0, n - 1, True] will be the scores for player 1 and player 2. If we compare them, we will get the final answer. 

if i == j. If player 1 is playing, we will return (nums[i], 0). Otherwise, we will return (0, nums[i]). 

If player 1 is playing, we are at [i, j]. We can two choices:

Pick the beginning. The problem is reduced to [i + 1, j, False]

Pick the ending. The problem is reduced to [i, j - 1, False]

If player 2 is playing, we are at [i, j]. We also have two choices. 

Pick the beginning. The problem is reduced to [i + 1, j, True]

Pick the ending. The problem is reduced to [i, j - 1, True]

### Python
```python
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        def helper(i, j, isPlayer1Playing):
            if (i, j, isPlayer1Playing) in memo:
                return memo[(i, j, isPlayer1Playing)]
            if i == j:
                return (nums[i], 0) if isPlayer1Playing else (0, nums[i])
            if isPlayer1Playing:
                res1 = helper(i + 1, j, not isPlayer1Playing)
                res1 = (res1[0] + nums[i], res1[1]) 
                res2 = helper(i, j - 1, not isPlayer1Playing)
                res2 = (res2[0] + nums[j], res2[1]) 
                if res1[0] >= res2[0]:
                    ans = res1
                else:
                    ans = res2
                memo[(i, j, isPlayer1Playing)] = ans
                return ans
            res1 = helper(i + 1, j, not isPlayer1Playing)
            res1 = (res1[0], res1[1] + nums[i]) 
            res2 = helper(i, j - 1, not isPlayer1Playing)
            res2 = (res2[0], res2[1] + nums[j]) 
            if res1[1] > res2[1]:
                ans = res1
            else:
                ans = res2
            memo[(i, j, isPlayer1Playing)] = ans
            return ans
            
        n = len(nums)
        ans = helper(0, n - 1, True)
        return ans[0] >= ans[1]
```
### Rust
```rust
pub struct Solution {}


// submission codes start here

use std::collections::HashMap;
impl Solution {
    pub fn helper(nums: &Vec<i32>, start: usize, end: usize, is_player_one_pick: bool, memo: &mut HashMap<(usize, usize, bool), (i32, i32)>) -> (i32, i32) {
        if memo.contains_key(&(start, end, is_player_one_pick)) {
            return *memo.get(&(start, end, is_player_one_pick)).unwrap();
        }
        if start == end {
            let res = if is_player_one_pick {(nums[start], 0)} else {(0, nums[start])};
            memo.insert((start, end, is_player_one_pick), res);
            return res;
        }
        let mut pick_left = Self::helper(nums, start + 1, end, !is_player_one_pick, memo);
        let mut pick_right = Self::helper(nums, start, end - 1, !is_player_one_pick, memo);
        let res = if is_player_one_pick {
            if pick_left.0 + nums[start] >= pick_right.0 + nums[end] {
                (pick_left.0 + nums[start], pick_left.1)
            } else {
                (pick_right.0 + nums[end], pick_right.1)
            }
        } else {
            if pick_left.1 + nums[start] >= pick_right.1 + nums[end] {
                (pick_left.0, pick_left.1 + nums[start])
            } else {
                (pick_right.0, pick_right.1 + nums[end])
            }            
        };
        memo.insert((start, end, is_player_one_pick), res);
        res
    }
    pub fn predict_the_winner(nums: Vec<i32>) -> bool {
        let n = nums.len();
        //key: start index, end index, is player pick 
        //value: player 1 score, player 2 score
        let mut memo: HashMap<(usize, usize, bool), (i32, i32)> = HashMap::new();
        let (score1, score2) = Self::helper(&nums, 0, n - 1, true, &mut memo);
        score1 >= score2
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_486() {
        assert_eq!(Solution::predict_the_winner(vec![1,5,2]), false);
        assert_eq!(Solution::predict_the_winner(vec![1,5,233,7]), true);
    }
}

```

---
title: 1823. find the winner of the circular game
date: '2022-08-26'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 1823 find the winner of the circular game
---



There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the i^th friend brings you to the (i+1)^th friend for 1 <TeX>\leq</TeX> i < n, and moving clockwise from the n^th friend brings you to the 1^st friend.



The rules of the game are as follows:



<ol>

Start at the 1^st friend.

Count the next k friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some friends more than once.

The last friend you counted leaves the circle and loses the game.

If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.

Else, the last friend in the circle wins the game.

</ol>



Given the number of friends, n, and an integer k, return the winner of the game.





>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2021/03/25/ic234-q2-ex11.png)
>   Input: n <TeX>=</TeX> 5, k <TeX>=</TeX> 2
>   Output: 3
>   Explanation: Here are the steps of the game:
>   1) Start at friend 1.
>   2) Count 2 friends clockwise, which are friends 1 and 2.
>   3) Friend 2 leaves the circle. Next start is friend 3.
>   4) Count 2 friends clockwise, which are friends 3 and 4.
>   5) Friend 4 leaves the circle. Next start is friend 5.
>   6) Count 2 friends clockwise, which are friends 5 and 1.
>   7) Friend 1 leaves the circle. Next start is friend 3.
>   8) Count 2 friends clockwise, which are friends 3 and 5.
>   9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.
>   Example 2:
>   Input: n <TeX>=</TeX> 6, k <TeX>=</TeX> 5
>   Output: 1
>   Explanation: The friends leave in this order: 5, 4, 6, 2, 3. The winner is friend 1.
**Constraints:**
>   	1 <TeX>\leq</TeX> k <TeX>\leq</TeX> n <TeX>\leq</TeX> 500


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn find_the_winner(n: i32, k: i32) -> i32 {
let mut vals = (1..=n).into_iter().collect::<Vec<_>>();
let k = k as usize;
let mut index = k - 1;
while vals.len() > 1 {
vals.remove(index);
index = (index + k - 1 ) % vals.len();
}
vals[0]
}
}
// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_1823() {
assert_eq!(Solution::find_the_winner(5, 2), 3);
assert_eq!(Solution::find_the_winner(6, 5), 1);
}
}

```

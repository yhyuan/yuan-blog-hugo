---
title: 997. find the town judge
date: '2022-06-27'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0997 find the town judge
---



In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

<ol>

The town judge trusts nobody.

Everybody (except for the town judge) trusts the town judge.

There is exactly one person that satisfies properties 1 and 2.

</ol>

You are given an array trust where trust[i] <TeX>=</TeX> [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.



>   Example 1:
>   Input: n <TeX>=</TeX> 2, trust <TeX>=</TeX> [[1,2]]
>   Output: 2
>   Example 2:
>   Input: n <TeX>=</TeX> 3, trust <TeX>=</TeX> [[1,3],[2,3]]
>   Output: 3
>   Example 3:
>   Input: n <TeX>=</TeX> 3, trust <TeX>=</TeX> [[1,3],[2,3],[3,1]]
>   Output: -1
>   Example 4:
>   Input: n <TeX>=</TeX> 3, trust <TeX>=</TeX> [[1,2],[2,3]]
>   Output: -1
>   Example 5:
>   Input: n <TeX>=</TeX> 4, trust <TeX>=</TeX> [[1,3],[1,4],[2,3],[2,4],[4,3]]
>   Output: 3
**Constraints:**
>   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 1000
>   	0 <TeX>\leq</TeX> trust.length <TeX>\leq</TeX> 10^4
>   	trust[i].length <TeX>=</TeX><TeX>=</TeX> 2
>   	All the pairs of trust are unique.
>   	ai !<TeX>=</TeX> bi
>   	1 <TeX>\leq</TeX> ai, bi <TeX>\leq</TeX> n


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashSet;
impl Solution {
pub fn find_judge(n: i32, trust: Vec<Vec<i32>>) -> i32 {
let trust = trust.into_iter().map(|v| (v[0], v[1])).collect::<HashSet<_>>();
for i in 1..=n {
let mut is_judge = true;
for j in 1..=n {
if i == j {
continue;
}
if trust.contains(&(i, j)) {
is_judge = false;
break;
}
}
//println!("2 i: {}, judge: {}", i, is_judge);
if is_judge {
for j in 1..=n {
if i == j {
continue;
}
if !trust.contains(&(j, i)) {
is_judge = false;
break;
}
}
}
//println!("3 i: {}, judge: {}", i, is_judge);
if is_judge {
return i;
}
}
-1
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_997() {
assert_eq!(Solution::find_judge(2, vec![vec![1, 2]]), 2);
assert_eq!(Solution::find_judge(3, vec![vec![1,3],vec![2,3]]), 3);
assert_eq!(Solution::find_judge(3, vec![vec![1,3],vec![2,3],vec![3,1]]), -1);
}
}

```

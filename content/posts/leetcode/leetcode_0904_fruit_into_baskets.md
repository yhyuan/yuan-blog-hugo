---
title: 904. fruit into baskets
date: '2022-06-06'
tags: ['leetcode', 'rust', 'python', 'easy']
draft: false
description: Solution for leetcode 0904 fruit into baskets
---

 

  You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the i^th tree produces.

  You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

  

  	You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.

  	Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.

  	Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

  

  Given the integer array fruits, return the maximum number of fruits you can pick.

   

 >   Example 1:

  

 >   Input: fruits <TeX>=</TeX> [<u>1,2,1</u>]

 >   Output: 3

 >   Explanation: We can pick from all 3 trees.

  

 >   Example 2:

  

 >   Input: fruits <TeX>=</TeX> [0,<u>1,2,2</u>]

 >   Output: 3

 >   Explanation: We can pick from trees [1,2,2].

 >   If we had started at the first tree, we would only pick from trees [0,1].

  

 >   Example 3:

  

 >   Input: fruits <TeX>=</TeX> [1,<u>2,3,2,2</u>]

 >   Output: 4

 >   Explanation: We can pick from trees [2,3,2,2].

 >   If we had started at the first tree, we would only pick from trees [1,2].

  

 >   Example 4:

  

 >   Input: fruits <TeX>=</TeX> [3,3,3,<u>1,2,1,1,2</u>,3,3,4]

 >   Output: 5

 >   Explanation: We can pick from trees [1,2,1,1,2].

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> fruits.length <TeX>\leq</TeX> 10^5

 >   	0 <TeX>\leq</TeX> fruits[i] < fruits.length


## Solution
This question can be summarized as: We have a sliding window over an array. If we limit the count of unique elements to 2, what is the max length of this sliding window.  Here are steps.
we define i, j and the front and back point. Both of them are initialized as 0. We also create ans, count, and size to track the final result, the frequency dictionary, and the length of sliding window. 

The outer loop is defined as i < n to keep the front back valid.

The first loop is to move the front pointer until the sliding window just break the condition (it means contains more than 2 unique numbers) or we reach the end of array.  We need to keep track of the window size and frequency dictionary. 

Because we may break the first loop because the front index reach the end or the condition is break. If it is that the index reaches the end, it means current sliding window meet the  condition. We will update the final result ans with this size. If the condition is break, it mean one more character is added to the sliding window. We will need to minus 1 from the current size and update the final result. 

The second loop will allow us to move the back point forward until we meet the condition again or we meet the front pointer. We will need to update the frequency dictionary and size.

### Python
```python
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        i = 0
        j = 0
        ans = 0
        count = {}
        size = 0
        while i < n:
            while i < n and len(count) <= 2:
                count[fruits[i]] = count.get(fruits[i], 0) + 1
                i += 1
                size += 1
            if len(count) == 3:
                ans = max(ans, size - 1) # we add one more
            else:
                ans = max(ans, size) # we reach the end. 
            while j < i and len(count) > 2:
                if count[fruits[j]] == 1:
                    del count[fruits[j]]
                else:
                   count[fruits[j]] -= 1 
                j += 1
                size -= 1
        return ans
```
### Rust
```rust
pub struct Solution {}


// submission codes start here

use std::collections::HashMap;
impl Solution {
    pub fn total_fruit(fruits: Vec<i32>) -> i32 {
        let n = fruits.len();
        let mut hashmap: HashMap<i32, i32> = HashMap::new();
        let mut i = 0usize; //left
        let mut j = 0usize; // right
        let mut ans = i32::MIN;
        while j < n {
            //println!("0: i: {}, j: {}", i, j);
            while j < n && hashmap.len() < 3 {
                if hashmap.contains_key(&fruits[j]) {
                    *hashmap.get_mut(&fruits[j]).unwrap() += 1;
                } else {
                    hashmap.insert(fruits[j], 1);
                }
                j += 1;
            }
            let mut res = 0;
            for (key, val) in hashmap.iter() {
                res += *val;
            }
            if hashmap.len() == 3 {
                res -= 1;
            }
            //println!("1: i: {}, j: {}, res: {}", i, j, j - i);
            //println!("hashmap: {:?}", hashmap);
            ans = i32::max(ans, res);
            while i < j && hashmap.len() == 3 {
                let count = hashmap[&fruits[i]];
                if count == 1 {
                    hashmap.remove(&fruits[i]);
                } else {
                    *hashmap.get_mut(&fruits[i]).unwrap() -= 1;
                }
                i += 1;
            }
            //println!("hashmap: {:?}", hashmap);
            //println!("2: i: {}, j: {}", i, j);
        }
        ans
    }

}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_904() {
        assert_eq!(Solution::total_fruit(vec![1, 2, 1]), 3);
        assert_eq!(Solution::total_fruit(vec![0, 1, 2, 2]), 3);
        assert_eq!(Solution::total_fruit(vec![1, 2, 3, 2, 2]), 4);
    }
}

```

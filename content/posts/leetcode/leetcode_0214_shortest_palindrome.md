---
title: 214. shortest palindrome
date: '2021-10-31'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0214 shortest palindrome
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={214}/>
 

  You are given a string s. You can convert s to a palindrome by adding characters in front of it.

  Return the shortest palindrome you can find by performing this transformation.

   

 >   Example 1:

 >   Input: s <TeX>=</TeX> "aacecaaa"

 >   Output: "aaacecaaa"

 >   Example 2:

 >   Input: s <TeX>=</TeX> "abcd"

 >   Output: "dcbabcd"

   

  **Constraints:**

  

 >   	0 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 5  10^4

 >   	s consists of lowercase English letters only.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
这个解法的前提是你熟悉另一种字符串匹配算法，即 KMP 算法。推荐两个链接，大家可以先学习一下，我就不多说了。KMP 算法代码简单，但理解求 next 数组的话，确实有些麻烦。

http://jakeboxer.com/blog/2009/12/13/the-knuth-morris-pratt-algorithm-in-my-own-words/

https://learnku.com/articles/10622/introduction-of-kmp-algorithm-and-derivation-of-next-array

如果熟悉了 KMP 算法，下边就简单了。

再回想一下解法三，倒置字符串的思路，依次比较对应子串。

abbacd

原s: abbacd, 长度记为 n
逆r: dcabba, 长度记为 n

我们把两个字符串写在一起
abbacd dcabba

判断 abbacd 和 dcabba 是否相等
判断 abbac 和 cabba 是否相等
判断 abba 和 abba 是否相等
Copy
如果我们把 abbacd dcabba看成一个字符串，中间加上一个分隔符 #，abbacd#dcabba。

回味一下上边的三条判断，判断 XXX 和 XXX 是否相等，按列看一下。

左半部分 abbacd，abbac , abba 其实就是 abbacd#dcabba 的一些前缀。

右半部分dcabba，cabba，abba 其实就是 abbacd#dcabba 的一些后缀。

寻找前缀和后缀相等。

想一想 KMP 算法，这不就是 next 数组做的事情吗。

而我们中间加了分隔符，也就保证了前缀和后缀相等时，前缀一定在 abbacd 中。

换句话说，我们如果求出了 abbacd#dcabba 的 next 数组，因为我们构造的字符串后缀就是原字符串的倒置，前缀后缀相等时，也就意味着当前前缀是一个回文串，而 next 数组是寻求最长的前缀，我们也就找到了开头开始的最长回文串。

因为 next 数组的含义并不统一，但 KMP 算法本质上都是一样的，所以下边的代码仅供参考。

我的 next 数组 next[i] 所考虑的对应字符串不包含 s[i]
*/
impl Solution {
    /*
    pub fn shortest_palindrome(s: String) -> String {
        let n = s.len();
        let s_new: Vec<char> = s.chars().chain(std::iter::once('#')).chain(s.chars().rev()).collect();
        let n_new = s_new.len();
        let mut f = vec![0; n_new];
        for i in 1..n_new {
            let mut t = f[i - 1];
            while t > 0 && s_new[i] != s_new[t] {
                t = f[t - 1];
            }
            if s_new[i] == s_new[t] {
                t += 1;
            }
            f[i] = t;
        }
        s.chars()
            .rev()
            .take(n - f.last().unwrap())
            .chain(s.chars())
            .collect()
    }
    */
    pub fn shortest_palindrome(s: String) -> String {
        let n = s.len();
        if n == 1 || n == 0 {
            return s;
        }
        let chars: Vec<char> = s.chars().collect();
        let mut dp_row = vec![false; n];
        dp_row[n - 1] = true;
        for i in (0..n - 1).rev() {
            dp_row[i] = true;
            // dp_row[i + 1] = chars[i] == chars[i + 1];
            for j in (i + 1..n).rev() {
                dp_row[j] = dp_row[j - 1] && chars[i] == chars[j];
            }
        }
        let mut index = usize::MAX;
        for i in (0..n).rev() {
            if dp_row[i] {
                index = i;
                break;
            }
        }
        //println!("dp_row: {:?}", dp_row);
        //println!("index: {}", index);
        let mut new_chars: Vec<char> = chars.clone();        
        for i in index + 1..n {
            new_chars.insert(0, chars[i]);
        }

        /*
        let mut dp: Vec<Vec<bool>> = vec![vec![false; n]; n];
        for i in 0..n {
            dp[i][i] = true;
        }
        for i in 1..n {
            dp[i - 1][i] = chars[i - 1] == chars[i];
        }
        for i in (0..n - 1).rev() {
            for j in i + 2..n {
                dp[i][j] = dp[i + 1][j - 1] && chars[i] == chars[j];
            }
        }
        let mut index = usize::MAX;
        for i in (0..n).rev() {
            if dp[0][i] {
                index = i;
                break;
            }
        }
        
        // println!("dp: {:?}", dp);
        // println!("index: {:?}", index);
        let mut new_chars: Vec<char> = chars.clone();
        for i in index + 1..n {
            new_chars.insert(0, chars[i]);
        }
        */
        // println!("new_chars: {:?}", new_chars);
        let str: String = new_chars.iter().collect();
        str
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_214() {
        assert_eq!(Solution::shortest_palindrome("aacecaaa".to_string()), "aaacecaaa".to_string());
        assert_eq!(Solution::shortest_palindrome("abcd".to_string()), "dcbabcd".to_string());
    }
}

```

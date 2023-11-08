---
title: 299. bulls and cows
date: '2021-12-25'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0299 bulls and cows
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={299}/>
 

  You are playing the [Bulls and Cows](https://en.wikipedia.org/wiki/Bulls_and_Cows) game with your friend.

  You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

  

  	The number of "bulls", which are digits in the guess that are in the correct position.

  	The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.

  

  Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

  The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

   

 >   Example 1:

  

 >   Input: secret <TeX>=</TeX> "1807", guess <TeX>=</TeX> "7810"

 >   Output: "1A3B"

 >   Explanation: Bulls are connected with a '|' and cows are underlined:

 >   "1807"

 >     |

 >   "<u>7</u>8<u>10</u>"

 >   Example 2:

  

 >   Input: secret <TeX>=</TeX> "1123", guess <TeX>=</TeX> "0111"

 >   Output: "1A1B"

 >   Explanation: Bulls are connected with a '|' and cows are underlined:

 >   "1123"        "1123"

 >     |      or     |

 >   "01<u>1</u>1"        "011<u>1</u>"

 >   Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.

  

 >   Example 3:

  

 >   Input: secret <TeX>=</TeX> "1", guess <TeX>=</TeX> "0"

 >   Output: "0A0B"

  

 >   Example 4:

  

 >   Input: secret <TeX>=</TeX> "1", guess <TeX>=</TeX> "1"

 >   Output: "1A0B"

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> secret.length, guess.length <TeX>\leq</TeX> 1000

 >   	secret.length <TeX>=</TeX><TeX>=</TeX> guess.length

 >   	secret and guess consist of digits only.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn get_hint(secret: String, guess: String) -> String {
        if secret.len() != guess.len() {
            panic!("Secret and guess must have the same lengths!");
        }
        let string_length = secret.len();
        let secret_chars: Vec<char> = secret.chars().collect();
        let guess_chars: Vec<char> = guess.chars().collect();
        let indices: Vec<usize> = (0..string_length).filter(|&i| secret_chars[i] != guess_chars[i]).collect();
        let secret_chars: Vec<char> = indices.iter().map(|&i| secret_chars[i]).collect();
        let mut guess_chars: Vec<char> = indices.iter().map(|&i| guess_chars[i]).collect();
        let bull = string_length - secret_chars.len();
        let mut cow = 0usize;
        for ch in secret_chars {
            if let Some(index) = guess_chars.iter().position(|x| *x == ch) {
                guess_chars.remove(index);
                cow += 1;
            }
        }
        format!("{}A{}B", bull, cow)
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_299() {
        assert_eq!(
            Solution::get_hint("1807".to_owned(), "7810".to_owned()),
            "1A3B".to_owned()
        );
        assert_eq!(
            Solution::get_hint("1123".to_owned(), "0111".to_owned()),
            "1A1B".to_owned()
        );
    }
}

```

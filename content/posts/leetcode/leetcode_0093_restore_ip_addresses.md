---
title: 93. restore ip addresses
date: '2021-08-02'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0093 restore ip addresses
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={93}/>
 

  Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.

  A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

   

 >   Example 1:

 >   Input: s <TeX>=</TeX> "25525511135"

 >   Output: ["255.255.11.135","255.255.111.35"]

 >   Example 2:

 >   Input: s <TeX>=</TeX> "0000"

 >   Output: ["0.0.0.0"]

 >   Example 3:

 >   Input: s <TeX>=</TeX> "1111"

 >   Output: ["1.1.1.1"]

 >   Example 4:

 >   Input: s <TeX>=</TeX> "010010"

 >   Output: ["0.10.0.10","0.100.1.0"]

 >   Example 5:

 >   Input: s <TeX>=</TeX> "101023"

 >   Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

   

  **Constraints:**

  

 >   	0 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 3000

 >   	s consists of digits only.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn restore_ip_addresses_helper(chars: &Vec<char>, index: usize, dot_positions: &mut Vec<usize>) -> Vec<String> {
        if dot_positions.len() == 3 {
            if chars.len() <= dot_positions[2] || chars.len() - dot_positions[2] > 3 {
                return vec![];
            }
            if chars[0] == '0' && dot_positions[0] > 1 {
                return vec![];
            }
            if chars[dot_positions[0]] == '0' && dot_positions[1] - dot_positions[0] > 1 {
                return vec![];
            }
            if chars[dot_positions[1]] == '0' && dot_positions[2] - dot_positions[1] > 1 {
                return vec![];
            }
            if chars[dot_positions[2]] == '0' && chars.len() - dot_positions[2] > 1 {
                return vec![];
            }
            let num_1 = (&chars[..dot_positions[0]]).iter().collect::<String>().parse::<i32>().unwrap();
            let num_2 = (&chars[dot_positions[0]..dot_positions[1]]).iter().collect::<String>().parse::<i32>().unwrap();
            let num_3 = (&chars[dot_positions[1]..dot_positions[2]]).iter().collect::<String>().parse::<i32>().unwrap();
            let num_4 = (&chars[dot_positions[2]..]).iter().collect::<String>().parse::<i32>().unwrap();

            if num_1 <= 255 && num_2 <= 255 && num_3 <= 255 && num_4 <= 255 {
                let mut result_chars = chars.clone();
                result_chars.insert(dot_positions[2], '.');
                result_chars.insert(dot_positions[1], '.');
                result_chars.insert(dot_positions[0], '.');
                return vec![result_chars.iter().collect::<String>()];
            } else {
                return vec![];
            }
        }
        if index == chars.len() {
            return vec![];
        }
        //index, index + 1, index + 2
        let mut results: Vec<String> = vec![];
        for i in 1..=3 {
            dot_positions.push(index + i);
            let results_single = Solution::restore_ip_addresses_helper(chars, index + i, dot_positions);    
            dot_positions.pop();
            for result in results_single {
                results.push(result);
            }
        }
        results
    }

    pub fn restore_ip_addresses(s: String) -> Vec<String> {
        if s.len() < 4 {
            return vec![];
        }
        let chars: Vec<char> = s.chars().collect();
        let mut dot_positions = vec![];
        Solution::restore_ip_addresses_helper(&chars, 0, &mut dot_positions)
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_93() {
        assert_eq!(Solution::restore_ip_addresses("25525511135".to_string()), vec!["255.255.11.135".to_string(),"255.255.111.35".to_string()]);
        assert_eq!(Solution::restore_ip_addresses("0000".to_string()), vec!["0.0.0.0".to_string()]);
        assert_eq!(Solution::restore_ip_addresses("1111".to_string()), vec!["1.1.1.1".to_string()]);
        assert_eq!(Solution::restore_ip_addresses("010010".to_string()), vec!["0.10.0.10".to_string(),"0.100.1.0".to_string()]);
        assert_eq!(Solution::restore_ip_addresses("101023".to_string()), vec!["1.0.10.23".to_string(),"1.0.102.3".to_string(),"10.1.0.23".to_string(),"10.10.2.3".to_string(),"101.0.2.3".to_string()]);
    }
}

```

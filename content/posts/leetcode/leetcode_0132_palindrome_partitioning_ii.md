---
title: 132. palindrome partitioning ii
date: '2021-09-08'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0132 palindrome partitioning ii
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={132}/>
 

  Given a string s, partition s such that every substring of the partition is a palindrome.

  Return the minimum cuts needed for a palindrome partitioning of s.

   

 >   Example 1:

  

 >   Input: s <TeX>=</TeX> "aab"

 >   Output: 1

 >   Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

  

 >   Example 2:

  

 >   Input: s <TeX>=</TeX> "a"

 >   Output: 0

  

 >   Example 3:

  

 >   Input: s <TeX>=</TeX> "ab"

 >   Output: 1

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 2000

 >   	s consists of lower-case English letters only.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
//use std::collections::HashSet;
/*
impl Solution {
    pub fn is_palindrome(chars: &Vec<char>, start: usize, end: usize) -> bool {
        for i in 0..(end - start + 1) / 2 {
            if chars[start + i] != chars[end - i] {
                return false;
            }
        }
        return true;
    }
    pub fn min_cut(s: String) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        //let palindrome_set = Self::find_palindrome(&chars);
        let n = s.len();
        let mut dp: Vec<Vec<i32>> = vec![vec![0; n]; n];
        for k in 1..n {
            for i in 0..n - k { //k = 1
                if Self::is_palindrome(&chars, i, i + k) {
                    dp[i][i + k] = 0;    
                } else {
                    dp[i][i + k] = dp[i][i] + dp[i + 1][i + k];
                    for j in 1..k {
                        let value = dp[i][i + j] + dp[i + j + 1][i + k];
                        if dp[i][i + k] > value {
                            dp[i][i + k] = value;
                        }
                    }
                    dp[i][i + k] = dp[i][i + k] + 1;
                }
            }    
        }
        dp[0][n - 1]
    }
}
*/
impl Solution {
    pub fn build_is_palindrome_dp(chars: &Vec<char>) -> Vec<Vec<bool>> {
        let n = chars.len();
        let mut is_palindrome_dp: Vec<Vec<bool>> = vec![vec![false; n]; n];
        for i in 0..n {
            is_palindrome_dp[i][i] = true;
        }
        for i in 0..n - 1 {
            is_palindrome_dp[i][i + 1] = chars[i] == chars[i + 1];
        }
        for k in 3..=n { // len 
            for i in 0..n - k + 1 {
                is_palindrome_dp[i][i + k - 1] = chars[i] == chars[i + k - 1] && is_palindrome_dp[i + 1][i + k - 1 - 1];
            }
        }
        is_palindrome_dp    
    }
    pub fn min_cut(s: String) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        let n = chars.len();
        let is_palindrome_dp = Self::build_is_palindrome_dp(&chars);
        //dp[i]: min cut for chars[0..i]
        let mut min_cut_dp: Vec<i32> = vec![0; n];
        for end in 0..n {
            let mut min_cut = i32::MAX;
            for start in 0..=end {
                if is_palindrome_dp[start][end] {
                    if start == 0 {
                        min_cut = 0;
                        break;
                    }
                    min_cut = i32::min(min_cut, min_cut_dp[start - 1] + 1);
                }
            }
            min_cut_dp[end] = min_cut;
        }
        min_cut_dp[n - 1]
        /*
        // dp[i][j] is the min cut for s[i..=j]
        let mut is_palindrome_dp: Vec<Vec<bool>> = vec![vec![false; n]; n];
        let mut min_cut_dp: Vec<Vec<i32>> = vec![vec![0; n]; n];
        for i in 0..n {
            is_palindrome_dp[i][i] = true;
            min_cut_dp[i][i] = 0;
        }
        for i in 0..n - 1 {
            is_palindrome_dp[i][i + 1] = chars[i] == chars[i + 1];
            min_cut_dp[i][i + 1] = if chars[i] == chars[i + 1] {0} else {1};
        }
        for k in 3..=n { // len 
            for i in 0..n - k + 1 {
                is_palindrome_dp[i][i + k - 1] = chars[i] == chars[i + k - 1] && is_palindrome_dp[i + 1][i + k - 1 - 1];
                min_cut_dp[i][i + k - 1] = if is_palindrome_dp[i][i + k - 1] {
                    0
                } else {
                    let mut res = i32::MAX;
                    for j in i..i + k - 1 {
                        res = i32::min(res, min_cut_dp[i][j] + min_cut_dp[j + 1][i + k - 1]);
                    }
                    res + 1
                };
            }
        }
        min_cut_dp[0][n - 1]
        */
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_132() {
        assert_eq!(Solution::min_cut("leet".to_string()), 2);
        assert_eq!(Solution::min_cut("aab".to_string()), 1);
        assert_eq!(Solution::min_cut("a".to_string()), 0);
        assert_eq!(Solution::min_cut("ab".to_string()), 1);
        assert_eq!(Solution::min_cut("coder".to_string()), 4);
        assert_eq!(Solution::min_cut("apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp".to_string()), 452);
        assert_eq!(Solution::min_cut("fiefhgdcdcgfeibggchibffahiededbbegegdfibdbfdadfbdbceaadeceeefiheibahgececggaehbdcgebaigfacifhdbecbebfhiefchaaheiichgdbheacfbhfiaffaecicbegdgeiaiccghggdfggbebdaefcagihbdhhigdgbghbahhhdagbdaefeccfiaifffcfehfcdiiieibadcedibbedgfegibefagfccahfcbegdfdhhdgfhgbchiaieehdgdabhidhfeecgfiibediiafacagigbhchcdhbaigdcedggehhgdhedaebchcafcdehcffdiagcafcgiidhdhedgaaegdchibhdaegdfdaiiidcihifbfidechicighbcbgibadbabieaafgeagfhebfaheaeeibagdfhadifafghbfihehgcgggffgbfccgafigieadfehieafaehaggeeaaaehggffccddchibegfhdfafhadgeieggiigacbfgcagigbhbhefcadafhafdiegahbhccidbeeagcgebehheebfaechceefdiafgeddhdfcadfdafbhiifigcbddahbabbeedidhaieagheihhgffbfbiacgdaifbedaegbhigghfeiahcdieghhdabdggfcgbafgibiifdeefcbegcfcdihaeacihgdchihdadifeifdgecbchgdgdcifedacfddhhbcagaicbebbiadgbddcbagbafeadhddaeebdgdebafabghcabdhdgieiahggddigefddccfccibifgbfcdccghgceigdfdbghdihechfabhbacifgbiiiihcgifhdbhfcaiefhccibebcahidachfabicbdabibiachahggffiibbgchbidfbbhfcicfafgcagaaadbacddfiigdiiffhbbehaaacidggfbhgeaghigihggfcdcidbfccahhgaffiibbhidhdacacdfebedbiacaidaachegffaiiegeabfdgdcgdacfcfhdcbfiaaifgfaciacfghagceaaebhhibbieehhcbiggabefbeigcbhbcidbfhfcgdddgdffghidbbbfbdhcgabaagddcebaechbbiegeiggbabdhgghciheabdibefdfghbfbfebidhicdhbeghebeddgfdfhefebiiebdchifbcbahaddhbfafbbcebiigadhgcfbebgbebhfddgdeehhgdegaeedfadegfeihcgeefbbagbbacbgggciehdhiggcgaaicceeaefgcehfhfdciaghcbbgdihbhecfbgffefhgiefgeiggcebgaacefidghdfdhiabgibchdicdehahbibeddegfciaeaffgbefbbeihbafbagagedgbdadfdggfeaebaidchgdbcifhahgfdcehbahhdggcdggceiabhhafghegfdiegbcadgaecdcdddfhicabdfhbdiiceiegiedecdifhbhhfhgdbhibbdgafhgdcheefdhifgddchadbdggiidhbhegbdfdidhhfbehibiaacdfbiagcbheabaaebfeaeafbgigiefeaeheabifgcfibiddadicheahgbfhbhddaheghddceedigddhchecaghdegigbegcbfgbggdgbbigegffhcfcbbebdchffhddbfhhfgegggibhafiebcfgeaeehgdgbccbfghagfdbdfcbcigbigaccecfehcffahiafgabfcaefbghccieehhhiighcfeabffggfchfdgcfhadgidabdceediefdccceidcfbfiiaidechhbhdccccaigeegcaicabbifigcghcefaafaefd".to_string()), 1345);
    }
}

```

---
title: 418. sentence screen fitting
date: '2022-03-07'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0418 sentence screen fitting
---


Given a rows x cols screen and a sentence represented as a list of strings, return the number of times the given sentence can be fitted on the screen.



The order of words in the sentence must remain unchanged, and a word cannot be split into two lines. A single space must separate two consecutive words in a line.



 



 > Example 1:



 > Input: sentence <TeX>=</TeX> ["hello","world"], rows <TeX>=</TeX> 2, cols <TeX>=</TeX> 8

 > Output: 1

 > Explanation:

 > hello---

 > world---

 > The character '-' signifies an empty space on the screen.

 > Example 2:



 > Input: sentence <TeX>=</TeX> ["a", "bcd", "e"], rows <TeX>=</TeX> 3, cols <TeX>=</TeX> 6

 > Output: 2

 > Explanation:

 > a-bcd- 

 > e-a---

 > bcd-e-

 > The character '-' signifies an empty space on the screen.

 > Example 3:



 > Input: sentence <TeX>=</TeX> ["i","had","apple","pie"], rows <TeX>=</TeX> 4, cols <TeX>=</TeX> 5

 > Output: 1

 > Explanation:

 > i-had

 > apple

 > pie-i

 > had--

 > The character '-' signifies an empty space on the screen.

 



**Constraints:**



 > 1 <TeX>\leq</TeX> sentence.length <TeX>\leq</TeX> 100

 > 1 <TeX>\leq</TeX> sentence[i].length <TeX>\leq</TeX> 10

 > sentence[i] consists of lowercase English letters.

 > 1 <TeX>\leq</TeX> rows, cols <TeX>\leq</TeX> 2  104

 > Accepted

 > 85,596

 > Submissions

 > 241,053


## Solution

Let's deal with the following corn cases firstly.

The cols is smaller than the max word length. Obviously, the word can not be filled. So we should return 0. 

The cols can be divided by the sentence length + 1 or the remain is sentence length. It means one row can be used to fill one or many sentences without empty spaces. 

Let's use ans and index to mark the number of filled sentences and current index. Then, we will calculate row by row. Firstly, we calculate how many sentence can be filled. Then, we calculate that if we fill one sentence in the ending, what value will index become.

### Python
```python
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        wordLens = list(map(lambda word: len(word), sentence))
        maxLength = max(wordLens)
        if cols < maxLength:
            return 0
        sentenceLength = len(" ".join(sentence))
        if cols % (sentenceLength + 1) == 0:
            return rows * cols // (sentenceLength + 1)
        if cols % (sentenceLength + 1) == sentenceLength:
            return rows * (cols + 1) // (sentenceLength + 1)

        def findNextPositionWord(index, wordLen, cols):            
            remained = cols - index % cols
            if (remained > wordLen):
                index += wordLen
                index += 1
            elif (remained == wordLen):
                index += wordLen
            else:
                index = (index // cols + 1) * cols + wordLen
                index += 1
            return index
        def fillOneRow(index, wordLens, cols, sentenceLength):
            col_index = index % cols
            n = (cols - col_index) // (sentenceLength + 1)
            res = n
            index = index + n * (sentenceLength + 1)
            for j in range(len(wordLens)):
                index = findNextPositionWord(index, wordLens[j], cols)
            if index <= rows * cols:
                res += 1
            return (index, res)

        ans = 0
        index = 0
        for i in range(rows):
            (index, res) = fillOneRow(index, wordLens, cols, sentenceLength)
            ans += res
            if (index >= rows * cols):
                break
        return ans
```

### Rust
```rust
 pub struct Solution {}

 // problem: https://leetcode.com/problems/sentence-screen-fitting/
 // discuss: https://leetcode.com/problems/sentence-screen-fitting/discuss/?currentPage=1&orderBy=most_votes&query=
 
 // submission codes start here
 impl Solution {
    pub fn words_typing(sentence: Vec<String>, rows: i32, cols: i32) -> i32 {
        let word_lens: Vec<usize> = sentence.iter().map(|s| s.len()).collect::<Vec<_>>();
        if word_lens.iter().filter(|&size| size > &(cols as usize)).count() > 0 { // exist a word which is longer than cols. It is not possible to fit. 
            return 0;
        }
        let sentence_len = word_lens.iter().sum::<usize>() + word_lens.len() - 1;
        let rows = rows as usize;
        let cols = cols as usize;
        //special case: the length + one space can fill each row.
        if cols % (sentence_len + 1) == 0 {
            let result = rows  * cols / (sentence_len + 1);
            return result as i32;
        }
        //special case: the length + one space can fill each row.
        if cols % (sentence_len + 1) == sentence_len {
            let result = rows * (cols + 1) / (sentence_len + 1);
            return result as i32;
        }
        let mut ans = 0i32;
        let mut index = 0usize;
        for i in 0..rows {
            // if cols is very long, the following lines allow us to quick jump.
            let col_index = index % cols;
            let n = (cols - col_index) / (sentence_len + 1); // with a space ending.
            ans += n as i32;
            index = index + n * (sentence_len + 1);
            // deal with remaining spaces or the column is short. 
            for j in 0..word_lens.len() {
                let remained = cols - index % cols;
                // remained space is long
                if remained > word_lens[j] {
                    index += word_lens[j];
                    index += 1;
                } else if remained == word_lens[j] { // remained space just fill the word
                    index += word_lens[j];
                } else { // remaining space is too short and we have to jump to the enxt row
                    index = (index / cols + 1) * cols + word_lens[j];
                    index += 1;
                }
            }
            if index > rows * cols {
                break;
            }
            ans += 1;
            if index == rows * cols {
                break;
            }
        }
        return ans;
    }
}
 
 // submission codes end
 
 #[cfg(test)]
 mod tests {
     use super::*;
 
     #[test]
     fn test_418() {
        assert_eq!(Solution::words_typing(vec_string!["a", "bc"], 20000, 20000), 80000000);
        assert_eq!(Solution::words_typing(vec_string!["a", "bcd", "e"], 3, 6), 2);
        assert_eq!(Solution::words_typing(vec_string!["hello","world"], 16, 8), 8);
        assert_eq!(Solution::words_typing(vec_string!["a", "b", "c"], 3, 1), 1);
        assert_eq!(Solution::words_typing(vec_string!["a", "bcd", "e"], 3, 6), 2);
        assert_eq!(Solution::words_typing(vec_string!["hello","world"], 2, 8), 1);
        assert_eq!(Solution::words_typing(vec_string!["i","had","apple","pie"], 4, 5), 1);
    }
 }
 
```

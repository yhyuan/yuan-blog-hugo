---
title: 68. text justification
date: '2021-07-08'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0068 text justification
---



Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified and no extra space is inserted between words.

Note:



A word is defined as a character sequence consisting of non-space characters only.

Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.

The input array words contains at least one word.





>   Example 1:
>   Input: words <TeX>=</TeX> ["This", "is", "an", "example", "of", "text", "justification."], maxWidth <TeX>=</TeX> 16
>   Output:
>   [
>      "This    is    an",
>      "example  of text",
>      "justification.  "
>   ]
>   Example 2:
>   Input: words <TeX>=</TeX> ["What","must","be","acknowledgment","shall","be"], maxWidth <TeX>=</TeX> 16
>   Output:
>   [
>     "What   must   be",
>     "acknowledgment  ",
>     "shall be        "
>   ]
>   Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
>   Note that the second line is also left-justified becase it contains only one word.
>   Example 3:
>   Input: words <TeX>=</TeX> ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth <TeX>=</TeX> 20
>   Output:
>   [
>     "Science  is  what we",
>     "understand      well",
>     "enough to explain to",
>     "a  computer.  Art is",
>     "everything  else  we",
>     "do                  "
>   ]
**Constraints:**
>   	1 <TeX>\leq</TeX> words.length <TeX>\leq</TeX> 300
>   	1 <TeX>\leq</TeX> words[i].length <TeX>\leq</TeX> 20
>   	words[i] consists of only English letters and symbols.
>   	1 <TeX>\leq</TeX> maxWidth <TeX>\leq</TeX> 100
>   	words[i].length <TeX>\leq</TeX> maxWidth


## Solution
The key to solve this problem is to solve how can we arrange one row with maxWidth. If we can arrange the words between [index, nextIndex] in one row, we can use recursive function to repeatedly fill the words row by row.

First let's define a function to find nextIndex with index and maxWidth.
```python
def findNextIndex(words, index, maxWidth):
nextIndex = -1 # if we reach the end of words,
textLength = 0
for i in range(index, len(words)):
textLength += words[i] + 1 # we need to add a space.


# we do not need the last space when compare with maxWidth
if textLength - 1 > maxWidth:
nextIndex = i
break
return nextIndex
```
Second we can define a helper function. It means we can going to arrange the words from index to a screen with maxWidth and will return a list with arranged text.
```python
def helper(words, index, maxWidth)
```
If this function is implemented, the problem can solve by calling this helper function.
```python
helper(words, 0, maxWidth)
```
Now the key to solve this problem is to implement this helper function. We have to deal with the following cases.

1. index >= len(words). It means we have reach the end of words. We will return [].

2. we can findNextIndex(words, index, maxWidth) to find the nextIndex. If nextIndex is -1, it means we have reach the end of the text. We can simple concatenate the words together and more spaces to make sure the final length will reach maxWidth.

3. nextIndex is as same as index. It means the length of word at index has exceed the maxWidth. We will have to cut the word to fill the row. The remaining part of the word will be saved back the words list and recursively call the function forward. We will need to make sure we change the words back since we do not want to modify the words list.

4. nextIndex is index + 1. It means the current row can only fill the current word. We will have to fill the row with this word and add more spaces behind this word.

5. Now we have to deal with the cases more than one words are filled in the row. We firstly calculate how many spaces we need to fill in this row and how many spaces between words are needed. Let's deal with a simple case if these spaces can be evenly distributed in these spaces between words. We can simple divide the number of spaces and the number of spaces between words. And join the words with the number of spaces.

6. If these spaces can not be evenly distributed, we firstly calculate the minimal spaces can be used between words. Then, we find the remain of the division and add the extra one space for the beginning part until we use all the remain spaces.

```python
class Solution(object):
def fullJustify(self, words, maxWidth):
def findNextIndex(words, maxWidth, index):
nextIndex = -1
textLength = 0
n = len(words)
for i in range(index, n):
textLength += len(words[i]) + 1
if textLength - 1 > maxWidth:
nextIndex = i
break
return nextIndex

def helper(words, maxWidth, index):
n = len(words)


# index exceed.
if index >= len(words):
return []
nextIndex = findNextIndex(words, maxWidth, index)


# last line
if nextIndex == -1:
line = " ".join(list(map(lambda i: words[i], range(index, n))))
line = line + " " * (maxWidth - len(line))
return [line]


# current word is longer than maxWidth
if nextIndex == index:
currentWord = words[index]
currentLine = words[index][ :maxWidth]
words[index] = words[index][maxWidth:]
results = helper(words, maxWidth, index)
results.insert(0, currentLine)
words[index] = currentWord
return results


# current word can be filled in row, but only current word can be filled.
if nextIndex == index + 1: # one line contains a word
wordLength = len(words[index])
currentLine = words[index] + " " * (maxWidth - len(words[index]))
results = helper(words, maxWidth, nextIndex)
results.insert(0, currentLine)
return results


# more than one words can be filled and the spaces can be evenly distributed.
numberOfLetter = sum(list(map(lambda i: len(words[i]), range(index, nextIndex))))
numberOfSpaces = maxWidth - numberOfLetter
if numberOfSpaces % (nextIndex - index - 1) == 0:
spaces = " " * (numberOfSpaces // (nextIndex - index - 1))
currentLine = spaces.join(list(map(lambda i: words[i], range(index, nextIndex))))
results = helper(words, maxWidth, nextIndex)
results.insert(0, currentLine)
return results


# spaces can not be evenly distributed.
currentWords = list(map(lambda i: words[i], range(index, nextIndex)))
numberOfWordSpaces = nextIndex - index - 1
remainedSpaces = maxWidth - sum(list(map(lambda word: len(word), currentWords)))
averageSpaces = remainedSpaces // numberOfWordSpaces
remainedSpaces = remainedSpaces % numberOfWordSpaces
currentLine = ""
for i in range(len(currentWords)):
currentLine += currentWords[i]
if i == len(currentWords) - 1:
break
if i < remainedSpaces % numberOfWordSpaces:
currentLine += " " * (averageSpaces + 1)
else:
currentLine += " " * (averageSpaces)
results = helper(words, maxWidth, nextIndex)
results.insert(0, currentLine)
return results

return helper(words, maxWidth, 0)
```


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn full_justify_helper(words: &Vec<String>, index: usize, max_width: usize) -> Vec<String> {
if index >= words.len() {
return vec![];
}
let max_width = max_width as usize;
let mut min_total_length = 0;
let mut k = usize::MAX;
for i in index..words.len() {
min_total_length += words[i].len() + 1;
//println!("min_total_length: {}, words[index]: {}, max_width + 1: {}", min_total_length, words[index], max_width + 1);
if min_total_length > max_width + 1 {
k = i;
break;
}
}
if k == usize::MAX {
let words: Vec<String> = (index..words.len()).into_iter().map(|i| words[i].clone()).collect();
let mut result = words.join(" ");
while result.len() < max_width {
result.push(' ');
}
return vec![result];
}
let line_words: Vec<String> = (index..k).into_iter().map(|i| words[i].clone()).collect();
let number_of_letters: usize = line_words.iter().map(|word| word.len()).sum();
if line_words.len() == 1 {
let mut result = line_words.join(" ");
while result.len() < max_width {
result.push(' ');
}
let mut results = Solution::full_justify_helper(words, index + 1, max_width);
results.insert(0, result);
return results;
}
//println!("line_words: {:?}, number_of_letters: {}, spaces: {}", line_words, number_of_letters, max_width - number_of_letters);

let space_postions = line_words.len() - 1;
let spaces = max_width - number_of_letters;
//println!("spaces / space_postions: {}, spaces % space_postions: {}", spaces / space_postions, spaces % space_postions);
// spaces / space_postions, spaces % space_postions
let mut new_line_words: Vec<String> = vec![];
for i in 0..line_words.len()-1 {
new_line_words.push(line_words[i].clone());
let min_number_of_spaces = spaces / space_postions;
let num_of_spaces = if i < spaces % space_postions {
min_number_of_spaces + 1
} else {
min_number_of_spaces
};
//println!("i: {} num_of_spaces: {}", i, num_of_spaces);
let space_string: String = (0..num_of_spaces).into_iter().map(|_| ' ').collect();
new_line_words.push(space_string);
}

new_line_words.push(line_words[line_words.len() - 1].clone());
let result = new_line_words.join("");
let mut results = Solution::full_justify_helper(words, k, max_width);
results.insert(0, result);
results
}
pub fn full_justify(words: Vec<String>, max_width: i32) -> Vec<String> {
Solution::full_justify_helper(&words, 0, max_width as usize)
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_68() {
assert_eq!(
Solution::full_justify(
vec_string![
"This",
"is",
"an",
"example",
"of",
"text",
"justification."
],
16
),
vec_string!["This    is    an", "example  of text", "justification.  "]
);
assert_eq!(
Solution::full_justify(
vec_string!["What", "must", "be", "acknowledgment", "shall", "be"],
16
),
vec_string!["What   must   be", "acknowledgment  ", "shall be        "]
);
assert_eq!(
Solution::full_justify(
vec_string![
"Science",
"is",
"what",
"we",
"understand",
"well",
"enough",
"to",
"explain",
"to",
"a",
"computer.",
"Art",
"is",
"everything",
"else",
"we",
"do"
],
20
),
vec_string![
"Science  is  what we",
"understand      well",
"enough to explain to",
"a  computer.  Art is",
"everything  else  we",
"do                  ",
]
);
}
}

```



### Python
```

```
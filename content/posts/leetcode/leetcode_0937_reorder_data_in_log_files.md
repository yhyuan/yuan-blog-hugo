---
title: 937. reorder data in log files
date: '2022-06-16'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0937 reorder data in log files
---



You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:



Letter-logs: All words (except the identifier) consist of lowercase English letters.

Digit-logs: All words (except the identifier) consist of digits.



Reorder these logs so that:

<ol>

The letter-logs come before all digit-logs.

The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.

The digit-logs maintain their relative ordering.

</ol>

Return the final order of the logs.



>   Example 1:
>   Input: logs <TeX>=</TeX> ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
>   Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
>   Explanation:
>   The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
>   The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
>   Example 2:
>   Input: logs <TeX>=</TeX> ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
>   Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
**Constraints:**
>   	1 <TeX>\leq</TeX> logs.length <TeX>\leq</TeX> 100
>   	3 <TeX>\leq</TeX> logs[i].length <TeX>\leq</TeX> 100
>   	All the tokens of logs[i] are separated by a single space.
>   	logs[i] is guaranteed to have an identifier and at least one word after the identifier.


## Solution
We try to use tuple to solve this problem. Since the letters-log should be sorted before digits-log, we assign 0 as the type value for letters-log and 1 as the type for the digits-log.

Since digits-log should keep its original order, we assign an order number as the second value. For letters-log, there is no requirement. We will simple give them 0.

Since the letters-log need to sort with its content, we put its content as the third value in the tuple.

Finally, we put the identifier as the fourth value in the tuple.

We sorted this tuple list and extract its content out and generate the results



### Python
```python
class Solution:
def reorderLogFiles(self, logs: List[str]) -> List[str]:
def checkInt(str):
try:
int(str)
return True
except ValueError:
return False
results = []
n = len(logs)
digitlogsCount = 0
for i in range(n):
words = logs[i].split(" ")
identifer = words[0]
logType = 1
for j in range(1, len(words)):
if not checkInt(words[j]):
logType = 0
break
logContent = " ".join(list(map(lambda i: words[i], range(1, len(words)))))
if logType == 1: #Digit
results.append((logType, digitlogsCount, logContent, identifer))
digitlogsCount += 1
else:
results.append((logType, 0, logContent, identifer))
results.sort()
results = list(map(lambda record: record[3] + " " + record[2], results))
return results
```


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::cmp::Ordering;
impl Solution {
pub fn is_digital_log(log: &String) -> bool {
let items = log.split_ascii_whitespace().collect::<Vec<&str>>();
if items.len() <= 1 {
return false;
}
let digits = vec!['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
for i in 1..items.len() {
let item = items[i];
for ch in item.chars() {
if !digits.contains(&ch) {
return false;
}
}
}
true
}
pub fn compare_letter_log(log1: &String, log2: &String) -> Option<Ordering> {
let index1 = log1.chars().position(|c| c == ' ').unwrap();
let index2 = log2.chars().position(|c| c == ' ').unwrap();
let substring1 = &log1[index1..];
let substring2 = &log2[index2..];
if substring1 == substring2 {
let id1 = &log1[..index1];
let id2 = &log2[..index2];
id1.partial_cmp(id2)
} else {
substring1.partial_cmp(substring2)
}
}
pub fn reorder_log_files(logs: Vec<String>) -> Vec<String> {
let digital_logs: Vec<&String> = logs.iter().filter(|&log| Solution::is_digital_log(log)).collect();
let mut letter_logs: Vec<&String> = logs.iter().filter(|&log| !Solution::is_digital_log(log)).collect();
letter_logs.sort_by(|&a, &b| Solution::compare_letter_log(a, b).unwrap());
for &log in digital_logs.iter() {
letter_logs.push(log);
}
let results: Vec<String> = letter_logs.iter().map(|&log| log.to_string()).collect();
results
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_937() {
assert_eq!(Solution::reorder_log_files(vec!["dig1 8 1 5 1".to_string(),"let1 art can".to_string(),"dig2 3 6".to_string(),"let2 own kit dig".to_string(),"let3 art zero".to_string()]), vec!["let1 art can".to_string(),"let3 art zero".to_string(),"let2 own kit dig".to_string(),"dig1 8 1 5 1".to_string(),"dig2 3 6".to_string()])
}
}

```

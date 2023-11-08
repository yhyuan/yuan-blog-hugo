---
title: 127. word ladder
date: '2021-09-03'
tags: ['leetcode', 'rust', 'python', 'hard']
draft: false
description: Solution for leetcode 0127 word ladder
---



A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:



Every adjacent pair of words differs by a single letter.

Every si for 1 <TeX>\leq</TeX> i <TeX>\leq</TeX> k is in wordList. Note that beginWord does not need to be in wordList.

sk <TeX>=</TeX><TeX>=</TeX> endWord



Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.



>   Example 1:
>   Input: beginWord <TeX>=</TeX> "hit", endWord <TeX>=</TeX> "cog", wordList <TeX>=</TeX> ["hot","dot","dog","lot","log","cog"]
>   Output: 5
>   Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
>   Example 2:
>   Input: beginWord <TeX>=</TeX> "hit", endWord <TeX>=</TeX> "cog", wordList <TeX>=</TeX> ["hot","dot","dog","lot","log"]
>   Output: 0
>   Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
**Constraints:**
>   	1 <TeX>\leq</TeX> beginWord.length <TeX>\leq</TeX> 10
>   	endWord.length <TeX>=</TeX><TeX>=</TeX> beginWord.length
>   	1 <TeX>\leq</TeX> wordList.length <TeX>\leq</TeX> 5000
>   	wordList[i].length <TeX>=</TeX><TeX>=</TeX> beginWord.length
>   	beginWord, endWord, and wordList[i] consist of lowercase English letters.
>   	beginWord !<TeX>=</TeX> endWord
>   	All the words in wordList are unique.


## Solution
The key to solve this problem is use BFS to search the graph. For each word, we will need to find its neighbour words. It is too time consuming to search the words list again and again. The best approach is to use "_" to replace one letter in the word and create a new string. It means this position can be any letters. Then, we can find all the words in the word list which match this pattern. For example, we want to search "hit"'s neighbours. We will need to search patterns: "_it", "h_t", "hi_". We can use a memo to store the results to avoid repeated calculation.


### Python
```python
from collections import deque
class Solution:
def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
wordDict = {}
n = len(wordList)
m = len(beginWord)
for i in range(n):
wordDict[wordList[i]] = i
memo = {}
def findNextWords(_word, index):
result = []
for ch in ['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','z','y']:
word = _word[:i] + ch + _word[i + 1: ]
if word in wordDict:
result.append(word)
memo[_word] = result
return result

q = deque()
q.append((0, beginWord))
visited = set([beginWord])
while len(q) > 0:
(step, word) = q.popleft()
if word == endWord:
return step + 1
for i in range(m):
ch = word[i]
_word = word[:i] + "_" + word[i + 1: ]
candidates = []
if _word in memo:
candidates = memo[_word]
else:
candidates = findNextWords(_word, i)
memo[_word] = candidates
for j in range(len(candidates)):
if candidates[j] in visited:
continue
q.append((step + 1, candidates[j]))
visited.add(candidates[j])
return 0
```


### Rust
```rust
pub struct Solution {}
use std::collections::VecDeque;
use std::collections::HashSet;
use std::collections::HashMap;

// submission codes start here
//use std::collections::HashMap;
/*
impl Solution {
pub fn calculate_distance(s1: &String, s2: &String) -> usize {
let n = s1.len();
let chars1: Vec<char> = s1.chars().collect();
let chars2: Vec<char> = s2.chars().collect();
(0..n).into_iter().filter(|&i| chars1[i] != chars2[i]).count()
}
pub fn ladder_length_helper(begin_word: &String, end_word: &String, word_list: &Vec<String>, removed_indices: &mut HashSet<usize>) -> Option<i32> {
if Solution::calculate_distance(begin_word, end_word) == 0 {
return Some(1i32);
}
let mut res: Option<i32> = None;
for (i, word) in word_list.iter().enumerate() {
if removed_indices.contains(&i) {
continue;
}
if Solution::calculate_distance(begin_word, word) == 1 {
//let mut new_word_list: Vec<String> = word_list.clone();
//new_word_list.remove(i);
removed_indices.insert(i);
let dist = Solution::ladder_length_helper(word, end_word, word_list, removed_indices);
removed_indices.remove(&i);
res = match (res, dist) {
(None, None) => None,
(Some(res_val), None) => Some(res_val),
(None, Some(dist_val)) => Some(dist_val + 1),
(Some(res_val), Some(dist_val)) => Some(i32::min(res_val, dist_val + 1))
};
}
}
res
}
}
*/
/*
impl Solution {
pub fn is_distance_zero(s1: &Vec<char>, s2: &Vec<char>) -> bool {
let n = s1.len();
for i in 0..n {
if s1[i] != s2[i] {
return false;
}
}
true
}
pub fn is_distance_one(s1: &Vec<char>, s2: &Vec<char>) -> bool {
let n = s1.len();
let mut result = 0;
for i in 0..n {
if s1[i] != s2[i] {
result += 1;
}
if result == 2 {
return false;
}
}
result == 1
}
pub fn calculate_neighbors(word_chars_list: &Vec<Vec<char>>) -> Vec<Vec<usize>> {
let n = word_chars_list.len();
let mut isNeighborMatrix: Vec<Vec<bool>> = vec![vec![false; n]; n];
for i in 0..n {
for j in i + 1..n {
let is_dist_one = Solution::is_distance_one(&word_chars_list[i], &word_chars_list[j]);
if is_dist_one {
isNeighborMatrix[i][j] = true;
isNeighborMatrix[j][i] = true;
}
}
}
let mut neighbors: Vec<Vec<usize>> = vec![vec![]; n];
for i in 0..n {
neighbors[i] = (0..n).into_iter().filter(|&k| isNeighborMatrix[i][k]).collect();
}
neighbors
}
pub fn ladder_length_helper(begin_index: usize, end_index: usize, neighbors: &Vec<Vec<usize>>, path: &mut HashMap<usize, usize>, layer_dict: &mut HashMap<usize, usize>, layer: usize) -> i32 {
if begin_index == end_index {
return path.len() as i32;
}
let neighbor_vector = &neighbors[begin_index];
let mut res  = i32::MAX;
for &neighbor_index in neighbor_vector.iter() {
if path.contains_key(&neighbor_index) {
continue;
}
if layer_dict.contains_key(&neighbor_index) && layer_dict[&neighbor_index] <= layer {
continue;
}
layer_dict.insert(neighbor_index, layer);
path.insert(neighbor_index, path.len());
let dist = Solution::ladder_length_helper(neighbor_index, end_index, neighbors, path, layer_dict, layer + 1);
if dist != i32::MAX {
res = i32::min(res, dist);
}
path.remove(&neighbor_index);
}
res
}
pub fn ladder_length(begin_word: String, end_word: String, word_list: Vec<String>) -> i32 {
let n = word_list.len();
let word_chars_list: Vec<Vec<char>> = word_list.iter().map(|word| word.chars().collect::<Vec<char>>()).collect();
let mut neighbors: Vec<Vec<usize>> = Solution::calculate_neighbors(&word_chars_list);
let end_word_chars: Vec<char> = end_word.chars().collect();
let end_index = word_chars_list.iter().position(|word| Solution::is_distance_zero(word, &end_word_chars));
if end_index.is_none() {
return 0;
}
let end_index = end_index.unwrap();
//println!("end_index: {}", end_index);
let begin_word_chars: Vec<char> = begin_word.chars().collect();
let begin_indices: Vec<usize> = (0..n).into_iter().filter(|&i| Solution::is_distance_one(&word_chars_list[i], &begin_word_chars)).collect();
//println!("begin_indices: {:?}", begin_indices);
//1i32
let mut layer_dict: HashMap<usize, usize> = HashMap::new();
let mut res  = i32::MAX;
for &begin_index in begin_indices.iter() {
let mut path: HashMap<usize, usize> = HashMap::new();
path.insert(begin_index, 0);
layer_dict.insert(begin_index, 0);
let dist = Solution::ladder_length_helper(begin_index, end_index, &neighbors, &mut path, &mut layer_dict, 1);
path.remove(&begin_index);
if dist != i32::MAX {
res = i32::min(res, dist);
}
}
//let mut removed_indices: HashSet<usize> = HashSet::new();
//let result = Solution::ladder_length_helper(&begin_word, &end_word, &word_list, &mut removed_indices);
if res == i32::MAX {0} else {res + 1}
}
}
*/
//use std::collections::VecDeque;
// use std::collections::{HashSet, HashMap};

//impl Solution {
/*
pub fn is_distance_zero(s1: &Vec<char>, s2: &Vec<char>) -> bool {
let n = s1.len();
for i in 0..n {
if s1[i] != s2[i] {
return false;
}
}
true
}
pub fn is_distance_one(s1: &Vec<char>, s2: &Vec<char>) -> bool {
let n = s1.len();
let mut result = 0;
for i in 0..n {
if s1[i] != s2[i] {
result += 1;
}
if result == 2 {
return false;
}
}
result == 1
}
pub fn calculate_neighbors(word_chars_list: &Vec<Vec<char>>) -> Vec<Vec<usize>> {
let n = word_chars_list.len();
let mut isNeighborMatrix: Vec<Vec<bool>> = vec![vec![false; n]; n];
for i in 0..n {
for j in i + 1..n {
let is_dist_one = Solution::is_distance_one(&word_chars_list[i], &word_chars_list[j]);
if is_dist_one {
isNeighborMatrix[i][j] = true;
isNeighborMatrix[j][i] = true;
}
}
}
let mut neighbors: Vec<Vec<usize>> = vec![vec![]; n];
for i in 0..n {
neighbors[i] = (0..n).into_iter().filter(|&k| isNeighborMatrix[i][k]).collect();
}
neighbors
}
*/
/*
pub fn create_graph(word_list: &Vec<String>) -> Vec<HashSet<usize>> {
fn is_neighbor(s1: &String, s2: &String) -> bool {
let chars1: Vec<char> = s1.chars().collect();
let chars2: Vec<char> = s2.chars().collect();
let mut result = 0 ;
for i in 0..chars1.len() {
if chars1[i] != chars2[i] {
result += 1;
}
if result >= 2 {
return false;
}
}
result == 1
}
let n = word_list.len();
let mut result: Vec<HashSet<usize>> = vec![HashSet::new(); n];
for i in 0..n {
let s1 = &word_list[i];
for j in i + 1..n {
let s2 = &word_list[j];
if is_neighbor(s1, s2) {
result[i].insert(j);
result[j].insert(i);
}
}
}
result
}
pub fn bfs(hashset: &HashSet<usize>, graph: &Vec<HashSet<usize>>, marked: &mut Vec<bool>) -> HashSet<usize> {
let mut result: HashSet<usize> = HashSet::new();
for &u in hashset.iter() {
marked[u] = true;
for &v in graph[u].iter() {
if !marked[v] {
result.insert(v);
}
}
}
result
}
pub fn has_common(hashset1: &HashSet<usize>, hashset2: &HashSet<usize>) -> bool {
let len1 = hashset1.len();
let len2 = hashset2.len();
if len1 <= len2 {
for u in hashset1.iter() {
if hashset2.contains(u) {
return true;
}
}
return false
}
for u in hashset2.iter() {
if hashset1.contains(u) {
return true;
}
}
return false
}
pub fn ladder_length(begin_word: String, end_word: String, word_list: Vec<String>) -> i32 {
let end_index = word_list.iter().position(|word| word == &end_word);
if end_index.is_none() {
return 0;
}
let end_index = end_index.unwrap();
let begin_index = word_list.iter().position(|word| word == &begin_word);
let mut word_list = word_list;
if begin_index.is_none() {
word_list.push(begin_word);
}
let n = word_list.len();
let begin_index = if begin_index.is_none() {n - 1} else {begin_index.unwrap()};

let graph = Self::create_graph(&word_list);
//println!("graph: {:?}", graph);
let mut marked: Vec<bool> = vec![false; n];
let mut begin_hashset: HashSet<usize> = HashSet::new();
begin_hashset.insert(begin_index);
let mut end_hashset: HashSet<usize> = HashSet::new();
end_hashset.insert(end_index);
let mut k = 1;
//begin_hashset.intersection(&end_hashset).count() == 0
while !Self::has_common(&begin_hashset, &end_hashset) {
let begin_len = begin_hashset.len();
let end_len = end_hashset.len();
if begin_len < end_len {
begin_hashset = Solution::bfs(&begin_hashset, &graph, &mut marked);
} else {
end_hashset = Solution::bfs(&end_hashset, &graph, &mut marked);
}
if begin_hashset.len() == 0 || end_hashset.len() == 0 {
return 0;
}
k = k + 1;
}
k
}
*/
/*
pub fn is_word_same(str1: &str, str2: &str) -> bool {
if str1.len() == 0 && str2.len() == 0 {
return true;
}
for i in 0..str1.len() {
let char1 = str1.chars().nth(i).unwrap();
let char2 = str2.chars().nth(i).unwrap();
if char1 != char2 {
return false;
}
}
return true;
}
pub fn is_word_distance_one(str1: &str, str2: &str) -> bool {
if str1.len() == 0 && str2.len() == 0 {
return false;
}
let char1 = str1.chars().nth(0).unwrap();
let char2 = str2.chars().nth(0).unwrap();
let sub_str1 = &str1[1..];
let sub_str2 = &str2[1..];
if char1 == char2 {
Self::is_word_distance_one(sub_str1, sub_str2)
} else {
Self::is_word_same(sub_str1, sub_str2)
}
}
pub fn build_graph(word_list: &Vec<String>) -> HashMap<usize, Vec<usize>> {
let mut graph: HashMap<usize, Vec<usize>> = HashMap::new();
for i in 0..word_list.len() {
let str1 = &word_list[i];
for j in i + 1..word_list.len() {
let str2 = &word_list[j];
if Self::is_word_distance_one(str1, str2) {
if graph.contains_key(&i) {
let mut vec = graph.get(&i).unwrap().to_vec();
vec.push(j);
graph.insert(i, vec);
} else {
graph.insert(i, vec![j]);
}
if graph.contains_key(&j) {
let mut vec = graph.get(&j).unwrap().to_vec();
vec.push(i);
graph.insert(j, vec);
} else {
graph.insert(j, vec![i]);
}
}
}
}
graph
}
pub fn ladder_length(begin_word: String, end_word: String, word_list: Vec<String>) -> i32 {
let mut graph: HashMap<usize, Vec<usize>> = Self::build_graph(&word_list);
let n = word_list.len();
let end: Option<usize> = (0..n).into_iter().find(|&i| Self::is_word_same(&end_word, &word_list[i]));
if end.is_none() {
return 0;
}
let end = end.unwrap();
let begins: Vec<usize> = (0..n).into_iter()
.filter(|&i| Self::is_word_distance_one(&begin_word, &word_list[i])).collect();
if begins.len() == 0 {
return 0;
}
// println!("graph: {:?}", graph);
// println!("begins: {:?}", begins);
// println!("end: {}", end);

let mut begin_visited: Vec<i32> = vec![-1; n];
let mut begin_queue:VecDeque<(usize, usize)> = VecDeque::new();
for i in 0..begins.len() {
begin_queue.push_back((begins[i], 1));
begin_visited[begins[i]] = 1;
if begins[i] == end {
return 2;
}
}
let mut end_visited: Vec<i32> = vec![-1; n];
let mut end_queue:VecDeque<(usize, usize)> = VecDeque::new();
end_queue.push_back((end, 0));
end_visited[end] = 0;
let mut result = i32::MAX;
while !begin_queue.is_empty() || !end_queue.is_empty() {
if !begin_queue.is_empty() {
let (begin_v, begin_steps) = begin_queue.pop_front().unwrap();
begin_visited[begin_v] = begin_steps as i32;
if end_visited[begin_v] >= 0 {
let dist = end_visited[begin_v] + begin_visited[begin_v] + 1;
result = i32::min(dist, result);
// return end_visited[begin_v] + begin_visited[begin_v] + 1;
}
// println!("begin_v: {}, begin_steps: {}", begin_v, begin_steps);
let neighbors = graph.get(&begin_v).unwrap();
for  i in 0..neighbors.len() {
let neighbor = neighbors[i];
if begin_visited[neighbor] >= 0 {
continue;
}
// begin_visited[neighbor] = begin_steps as i32 + 1;
begin_queue.push_back((neighbor, begin_steps + 1));
}
}
if !end_queue.is_empty() {
let (end_v, end_steps) = end_queue.pop_front().unwrap();
end_visited[end_v] = end_steps as i32;
if begin_visited[end_v] >= 0 {
result = i32::min(end_visited[end_v] + begin_visited[end_v] + 1, result);
// return end_visited[end_v] + begin_visited[end_v] + 1;
}
// println!("end_v: {}, end_steps: {}", end_v, end_steps);
let neighbors = graph.get(&end_v).unwrap();
for  i in 0..neighbors.len() {
let neighbor = neighbors[i];
if end_visited[neighbor] >= 0 {
continue;
}
// end_visited[neighbor] = end_steps as i32 + 1;
end_queue.push_back((neighbor, end_steps + 1));
}
}
}
if result == i32::MAX {0} else {result}
// 0
}
*/
//}
impl Solution {
pub fn calculate_neighbors(word: &String, visited: &HashSet<String>, word_list: &HashSet<String>, memo: &mut HashMap<String, Vec<String>>) -> Vec<String> {
let mut result: Vec<String> = vec![];
let chars = word.chars().collect::<Vec<_>>();
for i in 0..chars.len() {
let mut new_chars = chars.clone();
new_chars[i] = '*';
let star_s = new_chars.iter().collect::<String>();
let mut words = vec![];
if memo.contains_key(&star_s) {
words = memo.get(&star_s).unwrap().clone();
} else {
for j in 0..26u8 {
new_chars[i] = ('a' as u8 + j) as char;
let s = new_chars.iter().collect::<String>();
if word_list.contains(&s) {
words.push(s);
}
}
memo.insert(star_s.clone(), words.clone());
}
for i in 0..words.len() {
if &words[i] == word {
continue;
}
if visited.contains(&words[i]) {
continue;
}
result.push(words[i].clone());
}
}
result
}
pub fn ladder_length(begin_word: String, end_word: String, word_list: Vec<String>) -> i32 {
let word_list = word_list.into_iter().collect::<HashSet<_>>();
let mut q: VecDeque<String> = VecDeque::new();
q.push_back(begin_word);
let mut visited: HashSet<String> = HashSet::new();
let mut step = 1;
let mut memo: HashMap<String, Vec<String>> = HashMap::new();
while !q.is_empty() {
let mut next_q: VecDeque<String> = VecDeque::new();
while !q.is_empty() {
let word = q.pop_front().unwrap();
if &word == &end_word {
return step;
}
let neighbors = Self::calculate_neighbors(&word, &visited, &word_list, &mut memo);
for i in 0..neighbors.len() {
visited.insert(neighbors[i].clone());
next_q.push_back(neighbors[i].clone());
}
}
q = next_q;
step += 1;
}
0
}
}
// submission codes end



#[cfg(test)]
mod tests {
use super::*;


#[test]
fn test_127() {
assert_eq!(
Solution::ladder_length("hbo".to_string(), "qbx".to_string(),
vec!["abo".to_string(),"hco".to_string(),"hbw".to_string(),"ado".to_string(),"abq".to_string(),"hcd".to_string(),"hcj".to_string(),"hww".to_string(),"qbq".to_string(),"qby".to_string(),"qbz".to_string(),"qbx".to_string(),"qbw".to_string()]),
4);

assert_eq!(
Solution::ladder_length("a".to_string(), "c".to_string(),
vec!["a".to_string(),"b".to_string(),"c".to_string()]),
2);
assert_eq!(
Solution::ladder_length("hit".to_string(), "cog".to_string(),
vec!["hot".to_string(),"dot".to_string(),"dog".to_string(),"lot".to_string(),"log".to_string(),"cog".to_string()]),
5);

assert_eq!(
Solution::ladder_length("hit".to_string(), "cog".to_string(),
vec!["hot".to_string(),"dot".to_string(),"dog".to_string(),"lot".to_string(),"log".to_string()]),
0);
assert_eq!(
Solution::ladder_length("qa".to_string(), "sq".to_string(),
vec!["si".to_string(),"go".to_string(),"se".to_string(),"cm".to_string(),"so".to_string(),"ph".to_string(),"mt".to_string(),"db".to_string(),"mb".to_string(),"sb".to_string(),"kr".to_string(),"ln".to_string(),"tm".to_string(),"le".to_string(),"av".to_string(),"sm".to_string(),"ar".to_string(),"ci".to_string(),"ca".to_string(),"br".to_string(),"ti".to_string(),"ba".to_string(),"to".to_string(),"ra".to_string(),"fa".to_string(),"yo".to_string(),"ow".to_string(),"sn".to_string(),"ya".to_string(),"cr".to_string(),"po".to_string(),"fe".to_string(),"ho".to_string(),"ma".to_string(),"re".to_string(),"or".to_string(),"rn".to_string(),"au".to_string(),"ur".to_string(),"rh".to_string(),"sr".to_string(),"tc".to_string(),"lt".to_string(),"lo".to_string(),"as".to_string(),"fr".to_string(),"nb".to_string(),"yb".to_string(),"if".to_string(),"pb".to_string(),"ge".to_string(),"th".to_string(),"pm".to_string(),"rb".to_string(),"sh".to_string(),"co".to_string(),"ga".to_string(),"li".to_string(),"ha".to_string(),"hz".to_string(),"no".to_string(),"bi".to_string(),"di".to_string(),"hi".to_string(),"qa".to_string(),"pi".to_string(),"os".to_string(),"uh".to_string(),"wm".to_string(),"an".to_string(),"me".to_string(),"mo".to_string(),"na".to_string(),"la".to_string(),"st".to_string(),"er".to_string(),"sc".to_string(),"ne".to_string(),"mn".to_string(),"mi".to_string(),"am".to_string(),"ex".to_string(),"pt".to_string(),"io".to_string(),"be".to_string(),"fm".to_string(),"ta".to_string(),"tb".to_string(),"ni".to_string(),"mr".to_string(),"pa".to_string(),"he".to_string(),"lr".to_string(),"sq".to_string(),"ye".to_string()]),
5);
assert_eq!(
Solution::ladder_length("hot".to_string(), "dog".to_string(),
vec!["hot".to_string(),"dog".to_string()]),
0);

assert_eq!(
Solution::ladder_length("charge".to_string(), "comedo".to_string(),
vec!["shanny".to_string(),"shinny".to_string(),"whinny".to_string(),"whiney".to_string(),"shiver".to_string(),"sharer".to_string(),"scarer".to_string(),"scaler".to_string(),"render".to_string(),"fluxes".to_string(),"teases".to_string(),"starks".to_string(),"clinks".to_string(),"messrs".to_string(),"crewed".to_string(),"donner".to_string(),"blurts".to_string(),"bettye".to_string(),"powell".to_string(),"castes".to_string(),"hackee".to_string(),"hackle".to_string(),"heckle".to_string(),"deckle".to_string(),"decile".to_string(),"defile".to_string(),"define".to_string(),"refine".to_string(),"repine".to_string(),"rapine".to_string(),"ravine".to_string(),"raving".to_string(),"roving".to_string(),"chased".to_string(),"roping".to_string(),"coping".to_string(),"coming".to_string(),"homing".to_string(),"pointy".to_string(),"hominy".to_string(),"homily".to_string(),"homely".to_string(),"comely".to_string(),"comedy".to_string(),"comedo".to_string(),"vagues".to_string(),"crocus".to_string(),"spiked".to_string(),"bobbed".to_string(),"dourer".to_string(),"smells".to_string(),"feared".to_string(),"wooden".to_string(),"stings".to_string(),"loafer".to_string(),"pleads".to_string(),"gaiter".to_string(),"meeter".to_string(),"denser".to_string(),"bather".to_string(),"deaves".to_string(),"wetted".to_string(),"pleats".to_string(),"cadger".to_string(),"curbed".to_string(),"grover".to_string(),"hinged".to_string(),"budget".to_string(),"gables".to_string(),"larked".to_string(),"flunks".to_string(),"fibbed".to_string(),"bricks".to_string(),"bowell".to_string(),"yonder".to_string(),"grimes".to_string(),"clewed".to_string(),"triads".to_string(),"legion".to_string(),"lacier".to_string(),"ridden".to_string(),"bogied".to_string(),"camper".to_string(),"damien".to_string(),"spokes".to_string(),"flecks".to_string(),"goosed".to_string(),"snorer".to_string(),"choked".to_string(),"choler".to_string(),"leakey".to_string(),"vagued".to_string(),"flumes".to_string(),"scanty".to_string(),"bugger".to_string(),"tablet".to_string(),"nilled".to_string(),"julies".to_string(),"roomed".to_string(),"ridges".to_string(),"snared".to_string(),"singes".to_string(),"slicks".to_string(),"toiled".to_string(),"verged".to_string(),"shitty".to_string(),"clicks".to_string(),"farmed".to_string(),"stunts".to_string(),"dowsed".to_string(),"brisks".to_string(),"skunks".to_string(),"linens".to_string(),"hammer".to_string(),"naiver".to_string(),"duster".to_string(),"elates".to_string(),"kooked".to_string(),"whacky".to_string(),"mather".to_string(),"loomed".to_string(),"soured".to_string(),"mosses".to_string(),"keeled".to_string(),"drains".to_string(),"drafty".to_string(),"cricks".to_string(),"glower".to_string(),"brayed".to_string(),"jester".to_string(),"mender".to_string(),"burros".to_string(),"arises".to_string(),"barker".to_string(),"father".to_string(),"creaks".to_string(),"prayed".to_string(),"bulges".to_string(),"heaped".to_string(),"called".to_string(),"volley".to_string(),"girted".to_string(),"forded".to_string(),"huffed".to_string(),"bergen".to_string(),"grated".to_string(),"douses".to_string(),"jagger".to_string(),"grovel".to_string(),"lashes".to_string(),"creeds".to_string(),"bonier".to_string(),"snacks".to_string(),"powder".to_string(),"curled".to_string(),"milker".to_string(),"posers".to_string(),"ribbed".to_string(),"tracts".to_string(),"stoked".to_string(),"russel".to_string(),"bummer".to_string(),"cusses".to_string(),"gouged".to_string(),"nailed".to_string(),"lobbed".to_string(),"novels".to_string(),"stands".to_string(),"caches".to_string(),"swanks".to_string(),"jutted".to_string(),"zinged".to_string(),"wigged".to_string(),"lunges".to_string(),"divers".to_string(),"cranny".to_string(),"pinter".to_string(),"guides".to_string(),"tigers".to_string(),"traces".to_string(),"berber".to_string(),"purges".to_string(),"hoaxer".to_string(),"either".to_string(),"bribed".to_string(),"camped".to_string(),"funked".to_string(),"creaky".to_string(),"noises".to_string(),"paused".to_string(),"splits".to_string(),"morrow".to_string(),"faults".to_string(),"ladies".to_string(),"dinged".to_string(),"smoker".to_string(),"calved".to_string(),"deters".to_string(),"kicker".to_string(),"wisher".to_string(),"ballad".to_string(),"filled".to_string(),"fobbed".to_string(),"tucker".to_string(),"steams".to_string(),"rubber".to_string(),"staled".to_string(),"chived".to_string(),"warred".to_string(),"draped".to_string(),"curfew".to_string(),"chafed".to_string(),"washer".to_string(),"tombed".to_string(),"basket".to_string(),"limned".to_string(),"rapped".to_string(),"swills".to_string(),"gashed".to_string(),"loaner".to_string(),"settee".to_string(),"layers".to_string(),"bootee".to_string(),"rioted".to_string(),"prance".to_string(),"sharps".to_string(),"wigner".to_string(),"ranted".to_string(),"hanker".to_string(),"leaden".to_string(),"groped".to_string(),"dalian".to_string(),"robbed".to_string(),"peeled".to_string(),"larder".to_string(),"spoofs".to_string(),"pushed".to_string(),"hallie".to_string(),"maiden".to_string(),"waller".to_string(),"pashas".to_string(),"grains".to_string(),"pinked".to_string(),"lodged".to_string(),"zipper".to_string(),"sneers".to_string(),"bootie".to_string(),"drives".to_string(),"former".to_string(),"deepen".to_string(),"carboy".to_string(),"snouts".to_string(),"fained".to_string(),"wilmer".to_string(),"trance".to_string(),"bugles".to_string(),"chimps".to_string(),"deeper".to_string(),"bolder".to_string(),"cupped".to_string(),"mauser".to_string(),"pagers".to_string(),"proven".to_string(),"teaser".to_string(),"plucky".to_string(),"curved".to_string(),"shoots".to_string(),"barged".to_string(),"mantes".to_string(),"reefer".to_string(),"coater".to_string(),"clotho".to_string(),"wanner".to_string(),"likens".to_string(),"swamis".to_string(),"troyes".to_string(),"breton".to_string(),"fences".to_string(),"pastas".to_string(),"quirky".to_string(),"boiler".to_string(),"canoes".to_string(),"looted".to_string(),"caries".to_string(),"stride".to_string(),"adorns".to_string(),"dwells".to_string(),"hatred".to_string(),"cloths".to_string(),"rotted".to_string(),"spooks".to_string(),"canyon".to_string(),"lances".to_string(),"denied".to_string(),"beefed".to_string(),"diaper".to_string(),"wiener".to_string(),"rifled".to_string(),"leader".to_string(),"ousted".to_string(),"sprays".to_string(),"ridged".to_string(),"mousey".to_string(),"darken".to_string(),"guiled".to_string(),"gasses".to_string(),"suited".to_string(),"drools".to_string(),"bloody".to_string(),"murals".to_string(),"lassie".to_string(),"babied".to_string(),"fitter".to_string(),"lessee".to_string(),"chiles".to_string(),"wrongs".to_string(),"malian".to_string(),"leaves".to_string(),"redder".to_string(),"funnel".to_string(),"broths".to_string(),"gushes".to_string(),"grants".to_string(),"doyens".to_string(),"simmer".to_string(),"locked".to_string(),"spoors".to_string(),"berger".to_string(),"landed".to_string(),"mosley".to_string(),"scorns".to_string(),"whiten".to_string(),"hurled".to_string(),"routed".to_string(),"careen".to_string(),"chorus".to_string(),"chasms".to_string(),"hopped".to_string(),"cadged".to_string(),"kicked".to_string(),"slewed".to_string(),"shrewd".to_string(),"mauled".to_string(),"saucer".to_string(),"jested".to_string(),"shriek".to_string(),"giblet".to_string(),"gnarls".to_string(),"foaled".to_string(),"roughs".to_string(),"copses".to_string(),"sacked".to_string(),"blends".to_string(),"slurps".to_string(),"cashew".to_string(),"grades".to_string(),"cramps".to_string(),"radius".to_string(),"tamped".to_string(),"truths".to_string(),"cleans".to_string(),"creams".to_string(),"manner".to_string(),"crimps".to_string(),"hauled".to_string(),"cheery".to_string(),"shells".to_string(),"asters".to_string(),"scalps".to_string(),"quotas".to_string(),"clears".to_string(),"clover".to_string(),"weeder".to_string(),"homers".to_string(),"pelted".to_string(),"hugged".to_string(),"marked".to_string(),"moaned".to_string(),"steely".to_string(),"jagged".to_string(),"glades".to_string(),"goshes".to_string(),"masked".to_string(),"ringer".to_string(),"eloped".to_string(),"vortex".to_string(),"gender".to_string(),"spotty".to_string(),"harken".to_string(),"hasten".to_string(),"smiths".to_string(),"mulled".to_string(),"specks".to_string(),"smiles".to_string(),"vainer".to_string(),"patted".to_string(),"harden".to_string(),"nicked".to_string(),"dooley".to_string(),"begged".to_string(),"belief".to_string(),"bushel".to_string(),"rivers".to_string(),"sealed".to_string(),"neuter".to_string(),"legged".to_string(),"garter".to_string(),"freaks".to_string(),"server".to_string(),"crimea".to_string(),"tossed".to_string(),"wilted".to_string(),"cheers".to_string(),"slides".to_string(),"cowley".to_string(),"snotty".to_string(),"willed".to_string(),"bowled".to_string(),"tortes".to_string(),"pranks".to_string(),"yelped".to_string(),"slaved".to_string(),"silver".to_string(),"swords".to_string(),"miners".to_string(),"fairer".to_string(),"trills".to_string(),"salted".to_string(),"copsed".to_string(),"crusts".to_string(),"hogged".to_string(),"seemed".to_string(),"revert".to_string(),"gusted".to_string(),"pixies".to_string(),"tamika".to_string(),"franks".to_string(),"crowed".to_string(),"rocked".to_string(),"fisher".to_string(),"sheers".to_string(),"pushes".to_string(),"drifts".to_string(),"scouts".to_string(),"sables".to_string(),"sallie".to_string(),"shiner".to_string(),"coupes".to_string(),"napped".to_string(),"drowse".to_string(),"traced".to_string(),"scenes".to_string(),"brakes".to_string(),"steele".to_string(),"beater".to_string(),"buries".to_string(),"turned".to_string(),"luther".to_string(),"bowers".to_string(),"lofted".to_string(),"blazer".to_string(),"serves".to_string(),"cagney".to_string(),"hansel".to_string(),"talker".to_string(),"warmed".to_string(),"flirts".to_string(),"braced".to_string(),"yukked".to_string(),"milken".to_string(),"forged".to_string(),"dodder".to_string(),"strafe".to_string(),"blurbs".to_string(),"snorts".to_string(),"jetted".to_string(),"picket".to_string(),"pistil".to_string(),"valved".to_string(),"pewter".to_string(),"crawls".to_string(),"strews".to_string(),"railed".to_string(),"clunks".to_string(),"smiled".to_string(),"dealer".to_string(),"cussed".to_string(),"hocked".to_string(),"spited".to_string(),"cowers".to_string(),"strobe".to_string(),"donned".to_string(),"brawls".to_string(),"minxes".to_string(),"philby".to_string(),"gavels".to_string(),"renter".to_string(),"losses".to_string(),"packet".to_string(),"defied".to_string(),"hazier".to_string(),"twines".to_string(),"balled".to_string(),"gaoled".to_string(),"esther".to_string(),"narrow".to_string(),"soused".to_string(),"crispy".to_string(),"souped".to_string(),"corned".to_string(),"cooley".to_string(),"rioter".to_string(),"talley".to_string(),"keaton".to_string(),"rocker".to_string(),"spades".to_string(),"billie".to_string(),"mattel".to_string(),"billet".to_string(),"horton".to_string(),"navels".to_string(),"sander".to_string(),"stoker".to_string(),"winded".to_string(),"wilder".to_string(),"cloyed".to_string(),"blazed".to_string(),"itched".to_string(),"docked".to_string(),"greene".to_string(),"boozed".to_string(),"ticket".to_string(),"temped".to_string(),"capons".to_string(),"bravos".to_string(),"rinded".to_string(),"brandi".to_string(),"massed".to_string(),"sobbed".to_string(),"shapes".to_string(),"yippee".to_string(),"script".to_string(),"lesion".to_string(),"mallet".to_string(),"seabed".to_string(),"medals".to_string(),"series".to_string(),"phases".to_string(),"grower".to_string(),"vertex".to_string(),"dented".to_string(),"tushed".to_string(),"barron".to_string(),"toffee".to_string(),"bushes".to_string(),"mouser".to_string(),"zenger".to_string(),"quaked".to_string(),"marley".to_string(),"surfed".to_string(),"harmed".to_string(),"mormon".to_string(),"flints".to_string(),"shamed".to_string(),"forgot".to_string(),"jailor".to_string(),"boater".to_string(),"sparer".to_string(),"shards".to_string(),"master".to_string(),"pistol".to_string(),"tooted".to_string(),"banned".to_string(),"drover".to_string(),"spices".to_string(),"gobbed".to_string(),"corals".to_string(),"chucks".to_string(),"kitten".to_string(),"whales".to_string(),"nickel".to_string(),"scrape".to_string(),"hosted".to_string(),"hences".to_string(),"morays".to_string(),"stomps".to_string(),"marcel".to_string(),"hummed".to_string(),"wonder".to_string(),"stoves".to_string(),"distil".to_string(),"coffer".to_string(),"quaker".to_string(),"curler".to_string(),"nurses".to_string(),"cabbed".to_string(),"jigger".to_string(),"grails".to_string(),"manges".to_string(),"larger".to_string(),"zipped".to_string(),"rovers".to_string(),"stints".to_string(),"nudges".to_string(),"marlin".to_string(),"exuded".to_string(),"storey".to_string(),"pester".to_string(),"longer".to_string(),"creeps".to_string(),"meaner".to_string(),"wallop".to_string(),"dewier".to_string(),"rivera".to_string(),"drones".to_string(),"valued".to_string(),"bugled".to_string(),"swards".to_string(),"cortes".to_string(),"charts".to_string(),"benson".to_string(),"wreaks".to_string(),"glares".to_string(),"levels".to_string(),"smithy".to_string(),"slater".to_string(),"suites".to_string(),"paired".to_string(),"fetter".to_string(),"rutted".to_string(),"levied".to_string(),"menses".to_string(),"wither".to_string(),"woolly".to_string(),"weeded".to_string(),"planed".to_string(),"censer".to_string(),"tested".to_string(),"pulled".to_string(),"hitter".to_string(),"slicer".to_string(),"tartar".to_string(),"chunky".to_string(),"whirrs".to_string(),"mewled".to_string(),"astern".to_string(),"walden".to_string(),"hilton".to_string(),"cached".to_string(),"geller".to_string(),"dolled".to_string(),"chores".to_string(),"sorter".to_string(),"soothe".to_string(),"reused".to_string(),"clumps".to_string(),"fueled".to_string(),"hurler".to_string(),"helled".to_string(),"packed".to_string(),"ripped".to_string(),"tanned".to_string(),"binder".to_string(),"flames".to_string(),"teased".to_string(),"punker".to_string(),"jerked".to_string(),"cannon".to_string(),"joists".to_string(),"whited".to_string(),"sagged".to_string(),"heaven".to_string(),"hansen".to_string(),"grayer".to_string(),"turfed".to_string(),"cranks".to_string(),"stater".to_string(),"bunted".to_string(),"horsey".to_string(),"shakes".to_string(),"brands".to_string(),"faints".to_string(),"barber".to_string(),"gorged".to_string(),"creamy".to_string(),"mowers".to_string(),"scrams".to_string(),"gashes".to_string(),"knacks".to_string(),"aeries".to_string(),"sticks".to_string(),"altars".to_string(),"hostel".to_string(),"pumped".to_string(),"reeves".to_string(),"litter".to_string(),"hoaxed".to_string(),"mushed".to_string(),"guided".to_string(),"ripper".to_string(),"bought".to_string(),"gelled".to_string(),"ranker".to_string(),"jennie".to_string(),"blares".to_string(),"saloon".to_string(),"bomber".to_string(),"mollie".to_string(),"scoops".to_string(),"coolie".to_string(),"hollis".to_string(),"shrunk".to_string(),"tattle".to_string(),"sensed".to_string(),"gasket".to_string(),"dodoes".to_string(),"mapped".to_string(),"strips".to_string(),"dodges".to_string(),"sailed".to_string(),"talked".to_string(),"sorted".to_string(),"lodges".to_string(),"livest".to_string(),"pastel".to_string(),"ladles".to_string(),"graded".to_string(),"thrice".to_string(),"thales".to_string(),"sagger".to_string(),"mellon".to_string(),"ganged".to_string(),"maroon".to_string(),"fluked".to_string(),"raised".to_string(),"nannie".to_string(),"dearer".to_string(),"lither".to_string(),"triked".to_string(),"dorset".to_string(),"clamps".to_string(),"lonnie".to_string(),"spates".to_string(),"larded".to_string(),"condor".to_string(),"sinker".to_string(),"narced".to_string(),"quaver".to_string(),"atones".to_string(),"farted".to_string(),"elopes".to_string(),"winger".to_string(),"mottle".to_string(),"loaned".to_string(),"smears".to_string(),"joanne".to_string(),"boozes".to_string(),"waster".to_string(),"digger".to_string(),"swoops".to_string(),"smokey".to_string(),"nation".to_string(),"drivel".to_string(),"ceased".to_string(),"miffed".to_string(),"faiths".to_string(),"pisses".to_string(),"frames".to_string(),"fooled".to_string(),"milled".to_string(),"dither".to_string(),"crazed".to_string(),"darryl".to_string(),"mulder".to_string(),"posses".to_string(),"sumter".to_string(),"weasel".to_string(),"pedals".to_string(),"brawny".to_string(),"charge".to_string(),"welted".to_string(),"spanks".to_string(),"sallow".to_string(),"joined".to_string(),"shaker".to_string(),"blocks".to_string(),"mattie".to_string(),"swirls".to_string(),"driver".to_string(),"belles".to_string(),"chomps".to_string(),"blower".to_string(),"roared".to_string(),"ratted".to_string(),"hailed".to_string(),"taunts".to_string(),"steamy".to_string(),"parrot".to_string(),"deafer".to_string(),"chewed".to_string(),"spaces".to_string(),"cuffed".to_string(),"molded".to_string(),"winked".to_string(),"runnel".to_string(),"hollow".to_string(),"fluted".to_string(),"bedded".to_string(),"crepes".to_string(),"stakes".to_string(),"vested".to_string(),"parley".to_string(),"burton".to_string(),"loiter".to_string(),"massey".to_string(),"carnap".to_string(),"closed".to_string(),"bailed".to_string(),"milder".to_string(),"heists".to_string(),"morale".to_string(),"putter".to_string(),"snyder".to_string(),"damion".to_string(),"conned".to_string(),"little".to_string(),"pooped".to_string(),"ticced".to_string(),"cocked".to_string(),"halves".to_string(),"wishes".to_string(),"francs".to_string(),"goblet".to_string(),"carlin".to_string(),"pecked".to_string(),"julius".to_string(),"raster".to_string(),"shocks".to_string(),"dawned".to_string(),"loosen".to_string(),"swears".to_string(),"buried".to_string(),"peters".to_string(),"treats".to_string(),"noshed".to_string(),"hedges".to_string(),"trumps".to_string(),"rabies".to_string(),"ronnie".to_string(),"forces".to_string(),"ticked".to_string(),"bodies".to_string(),"proved".to_string(),"dadoes".to_string(),"halved".to_string(),"warner".to_string(),"divest".to_string(),"thumbs".to_string(),"fettle".to_string(),"ponies".to_string(),"testis".to_string(),"ranked".to_string(),"clouts".to_string(),"slates".to_string(),"tauted".to_string(),"stools".to_string(),"dodged".to_string(),"chancy".to_string(),"trawls".to_string(),"things".to_string(),"sorrow".to_string(),"levies".to_string(),"glides".to_string(),"battle".to_string(),"sauced".to_string(),"doomed".to_string(),"seller".to_string(),"strove".to_string(),"ballet".to_string(),"bumper".to_string(),"gooses".to_string(),"foiled".to_string(),"plowed".to_string(),"glints".to_string(),"chanel".to_string(),"petals".to_string(),"darted".to_string(),"seared".to_string(),"trunks".to_string(),"hatter".to_string(),"yokels".to_string(),"vanned".to_string(),"tweedy".to_string(),"rubles".to_string(),"crones".to_string(),"nettie".to_string(),"roofed".to_string(),"dusted".to_string(),"dicker".to_string(),"fakers".to_string(),"rusted".to_string(),"bedder".to_string(),"darrin".to_string(),"bigger".to_string(),"baylor".to_string(),"crocks".to_string(),"niches".to_string(),"tented".to_string(),"cashed".to_string(),"splats".to_string(),"quoted".to_string(),"soloed".to_string(),"tessie".to_string(),"stiles".to_string(),"bearer".to_string(),"hissed".to_string(),"soiled".to_string(),"adored".to_string(),"bowery".to_string(),"snakes".to_string(),"wagers".to_string(),"rafter".to_string(),"crests".to_string(),"plaids".to_string(),"cordon".to_string(),"listed".to_string(),"lawson".to_string(),"scared".to_string(),"brazos".to_string(),"horded".to_string(),"greens".to_string(),"marred".to_string(),"mushes".to_string(),"hooper".to_string(),"halter".to_string(),"ration".to_string(),"calked".to_string(),"erodes".to_string(),"plumed".to_string(),"mummer".to_string(),"pinged".to_string(),"curios".to_string(),"slated".to_string(),"ranter".to_string(),"pillow".to_string(),"frills".to_string(),"whaled".to_string(),"bathos".to_string(),"madden".to_string(),"totted".to_string(),"reamed".to_string(),"bellow".to_string(),"golfer".to_string(),"seaman".to_string(),"barred".to_string(),"merger".to_string(),"hipped".to_string(),"silken".to_string(),"hastes".to_string(),"strays".to_string(),"slinks".to_string(),"hooted".to_string(),"convex".to_string(),"singed".to_string(),"leased".to_string(),"bummed".to_string(),"leaner".to_string(),"molted".to_string(),"naught".to_string(),"caters".to_string(),"tidied".to_string(),"forges".to_string(),"sealer".to_string(),"gulled".to_string(),"plumps".to_string(),"racket".to_string(),"fitted".to_string(),"rafted".to_string(),"drapes".to_string(),"nasser".to_string(),"tamara".to_string(),"winced".to_string(),"juliet".to_string(),"ledger".to_string(),"bettie".to_string(),"howell".to_string(),"reeved".to_string(),"spiced".to_string(),"thebes".to_string(),"apices".to_string(),"dorsey".to_string(),"welled".to_string(),"feeler".to_string(),"warded".to_string(),"reader".to_string(),"folded".to_string(),"lepers".to_string(),"cranky".to_string(),"bosses".to_string(),"ledges".to_string(),"player".to_string(),"yellow".to_string(),"lunged".to_string(),"mattes".to_string(),"confer".to_string(),"malign".to_string(),"shared".to_string(),"brandy".to_string(),"filmed".to_string(),"rhinos".to_string(),"pulsed".to_string(),"rouses".to_string(),"stones".to_string(),"mixers".to_string(),"cooped".to_string(),"joiner".to_string(),"papped".to_string(),"liston".to_string(),"capote".to_string(),"salvos".to_string(),"wicker".to_string(),"ciders".to_string(),"hoofed".to_string(),"wefted".to_string(),"locket".to_string(),"picker".to_string(),"nougat".to_string(),"limpid".to_string(),"hooter".to_string(),"jailer".to_string(),"peaces".to_string(),"mashes".to_string(),"custer".to_string(),"wallis".to_string(),"purees".to_string(),"trends".to_string(),"irater".to_string(),"honied".to_string(),"wavers".to_string(),"tanner".to_string(),"change".to_string(),"hinges".to_string(),"tatted".to_string(),"cookie".to_string(),"catnap".to_string(),"carton".to_string(),"crimed".to_string(),"betted".to_string(),"veined".to_string(),"surges".to_string(),"rumped".to_string(),"merlin".to_string(),"convey".to_string(),"placid".to_string(),"harped".to_string(),"dianna".to_string(),"hookey".to_string(),"nobles".to_string(),"carted".to_string(),"elided".to_string(),"whined".to_string(),"glover".to_string(),"bleats".to_string(),"stales".to_string(),"husker".to_string(),"hearer".to_string(),"tartan".to_string(),"weaker".to_string(),"skewer".to_string(),"lumbar".to_string(),"temper".to_string(),"gigged".to_string(),"gawked".to_string(),"mayors".to_string(),"pigged".to_string(),"gather".to_string(),"valves".to_string(),"mitten".to_string(),"largos".to_string(),"boreas".to_string(),"judges".to_string(),"cozens".to_string(),"censor".to_string(),"frilly".to_string(),"dumbed".to_string(),"downer".to_string(),"jogger".to_string(),"scolds".to_string(),"danced".to_string(),"floras".to_string(),"funded".to_string(),"lumped".to_string(),"dashes".to_string(),"azores".to_string(),"quites".to_string(),"chunks".to_string(),"washed".to_string(),"duller".to_string(),"bilges".to_string(),"cruels".to_string(),"brooks".to_string(),"fishes".to_string(),"smoked".to_string(),"leaped".to_string(),"hotter".to_string(),"trials".to_string(),"heaves".to_string(),"rouges".to_string(),"kissed".to_string(),"sleety".to_string(),"manses".to_string(),"spites".to_string(),"starts".to_string(),"banded".to_string(),"clings".to_string(),"titted".to_string(),"vetoed".to_string(),"mister".to_string(),"mildew".to_string(),"wailed".to_string(),"sheets".to_string(),"peeked".to_string(),"passer".to_string(),"felted".to_string(),"broken".to_string(),"lieges".to_string(),"ruffed".to_string(),"bracts".to_string(),"buster".to_string(),"muffed".to_string(),"lanker".to_string(),"breaks".to_string(),"coffey".to_string(),"sighed".to_string(),"charms".to_string(),"balded".to_string(),"kisser".to_string(),"booths".to_string(),"leaven".to_string(),"cheeps".to_string(),"billed".to_string(),"lauder".to_string(),"bumped".to_string(),"career".to_string(),"stocks".to_string(),"airier".to_string(),"limped".to_string(),"jeanie".to_string(),"roamed".to_string(),"carves".to_string(),"lilted".to_string(),"router".to_string(),"bonnie".to_string(),"denver".to_string(),"briggs".to_string(),"steeps".to_string(),"nerves".to_string(),"oinked".to_string(),"bucked".to_string(),"hooves".to_string(),"dancer".to_string(),"burris".to_string(),"parked".to_string(),"swells".to_string(),"collie".to_string(),"perked".to_string(),"cooler".to_string(),"fopped".to_string(),"wedder".to_string(),"malted".to_string(),"sabers".to_string(),"lidded".to_string(),"conner".to_string(),"rogues".to_string(),"fought".to_string(),"dapper".to_string(),"purled".to_string(),"crowds".to_string(),"barnes".to_string(),"bonner".to_string(),"globed".to_string(),"goners".to_string(),"yankee".to_string(),"probes".to_string(),"trains".to_string(),"sayers".to_string(),"jersey".to_string(),"valley".to_string(),"vatted".to_string(),"tauter".to_string(),"dulled".to_string(),"mucked".to_string(),"jotted".to_string(),"border".to_string(),"genres".to_string(),"banked".to_string(),"filter".to_string(),"hitler".to_string(),"dipper".to_string(),"dollie".to_string(),"sieves".to_string(),"joliet".to_string(),"tilted".to_string(),"checks".to_string(),"sports".to_string(),"soughs".to_string(),"ported".to_string(),"causes".to_string(),"gelded".to_string(),"mooter".to_string(),"grills".to_string(),"parred".to_string(),"tipped".to_string(),"placer".to_string(),"slayer".to_string(),"glided".to_string(),"basked".to_string(),"rinses".to_string(),"tamper".to_string(),"bunged".to_string(),"nabbed".to_string(),"climbs".to_string(),"faeces".to_string(),"hanson".to_string(),"brainy".to_string(),"wicket".to_string(),"crowns".to_string(),"calmed".to_string(),"tarred".to_string(),"spires".to_string(),"deanne".to_string(),"gravel".to_string(),"messes".to_string(),"snides".to_string(),"tugged".to_string(),"denier".to_string(),"moslem".to_string(),"erased".to_string(),"mutter".to_string(),"blahed".to_string(),"hunker".to_string(),"fasten".to_string(),"garbed".to_string(),"cracks".to_string(),"braked".to_string(),"rasped".to_string(),"ravens".to_string(),"mutton".to_string(),"tester".to_string(),"tories".to_string(),"pinker".to_string(),"titled".to_string(),"arisen".to_string(),"softer".to_string(),"woolen".to_string(),"disses".to_string(),"likest".to_string(),"dicier".to_string(),"nagged".to_string(),"lipton".to_string(),"plumbs".to_string(),"manged".to_string(),"faulty".to_string(),"sacred".to_string(),"whiter".to_string(),"erases".to_string(),"padres".to_string(),"haired".to_string(),"captor".to_string(),"metals".to_string(),"cardin".to_string(),"yowled".to_string(),"trusts".to_string(),"revels".to_string(),"boxers".to_string(),"toured".to_string(),"spouts".to_string(),"sodded".to_string(),"judged".to_string(),"holley".to_string(),"figged".to_string(),"pricey".to_string(),"lapses".to_string(),"harper".to_string(),"beaned".to_string(),"sewers".to_string(),"caused".to_string(),"willie".to_string(),"farmer".to_string(),"pissed".to_string(),"bevies".to_string(),"bolled".to_string(),"bugler".to_string(),"votive".to_string(),"person".to_string(),"linton".to_string(),"senses".to_string(),"supped".to_string(),"mashed".to_string(),"pincer".to_string(),"wetter".to_string(),"tangos".to_string(),"sticky".to_string(),"lodger".to_string(),"loader".to_string(),"daunts".to_string(),"peaked".to_string(),"moused".to_string(),"sleeps".to_string(),"lasted".to_string(),"tasked".to_string(),"awards".to_string(),"lovely".to_string(),"gushed".to_string(),"spurts".to_string(),"canter".to_string(),"mantis".to_string(),"coaled".to_string(),"groans".to_string(),"dannie".to_string(),"oopses".to_string(),"sneaky".to_string(),"vogues".to_string(),"mobile".to_string(),"plumes".to_string(),"chides".to_string(),"theses".to_string(),"marcia".to_string(),"parser".to_string(),"flexed".to_string(),"stayed".to_string(),"fouler".to_string(),"tusked".to_string(),"quartz".to_string(),"daubed".to_string(),"clancy".to_string(),"rouged".to_string(),"flaked".to_string(),"norton".to_string(),"dunner".to_string(),"corded".to_string(),"shelly".to_string(),"hester".to_string(),"fucker".to_string(),"polled".to_string(),"rodger".to_string(),"yeager".to_string(),"zinced".to_string(),"livens".to_string(),"browne".to_string(),"gonged".to_string(),"pubbed".to_string(),"sapped".to_string(),"thrive".to_string(),"placed".to_string(),"jensen".to_string(),"moises".to_string(),"scopes".to_string(),"stumpy".to_string(),"stocky".to_string(),"heller".to_string(),"levers".to_string(),"morals".to_string(),"wheres".to_string(),"gasped".to_string(),"jobber".to_string(),"leaved".to_string(),"champs".to_string(),"rosier".to_string(),"pallet".to_string(),"shooed".to_string(),"parses".to_string(),"bender".to_string(),"closet".to_string(),"pureed".to_string(),"routes".to_string(),"verges".to_string(),"bulled".to_string(),"foster".to_string(),"rummer".to_string(),"molten".to_string(),"condos".to_string(),"better".to_string(),"cotter".to_string(),"lassos".to_string(),"grafts".to_string(),"vendor".to_string(),"thrace".to_string(),"codded".to_string(),"tinker".to_string(),"bullet".to_string(),"beaker".to_string(),"garden".to_string(),"spiels".to_string(),"popper".to_string(),"skills".to_string(),"plated".to_string(),"farrow".to_string(),"flexes".to_string(),"esters".to_string(),"brains".to_string(),"handel".to_string(),"puller".to_string(),"dickey".to_string(),"creeks".to_string(),"ballot".to_string(),"singer".to_string(),"sicker".to_string(),"spayed".to_string(),"spoils".to_string(),"rubier".to_string(),"missed".to_string(),"framed".to_string(),"bonnet".to_string(),"molder".to_string(),"mugger".to_string(),"waived".to_string(),"taster".to_string(),"robles".to_string(),"tracks".to_string(),"nearer".to_string(),"lister".to_string(),"horsed".to_string(),"drakes".to_string(),"lopped".to_string(),"lubber".to_string(),"busied".to_string(),"button".to_string(),"eluded".to_string(),"ceases".to_string(),"sought".to_string(),"realer".to_string(),"lasers".to_string(),"pollen".to_string(),"crisps".to_string(),"binned".to_string(),"darrel".to_string(),"crafty".to_string(),"gleams".to_string(),"lonely".to_string(),"gordon".to_string(),"harley".to_string(),"damian".to_string(),"whiles".to_string(),"wilton".to_string(),"lesser".to_string(),"mallow".to_string(),"kenyon".to_string(),"wimped".to_string(),"scened".to_string(),"risked".to_string(),"hunter".to_string(),"rooter".to_string(),"ramses".to_string(),"inches".to_string(),"goaded".to_string(),"ferber".to_string(),"freaky".to_string(),"nerved".to_string(),"spoken".to_string(),"lovers".to_string(),"letter".to_string(),"marrow".to_string(),"bulbed".to_string(),"braver".to_string(),"sloped".to_string(),"breads".to_string(),"cannes".to_string(),"bassos".to_string(),"orated".to_string(),"clever".to_string(),"darren".to_string(),"bredes".to_string(),"gouger".to_string(),"servos".to_string(),"trites".to_string(),"troths".to_string(),"flunky".to_string(),"jammed".to_string(),"bugged".to_string(),"watter".to_string(),"motive".to_string(),"humped".to_string(),"writer".to_string(),"pestle".to_string(),"rilled".to_string(),"packer".to_string(),"foists".to_string(),"croats".to_string(),"floury".to_string(),"napier".to_string(),"floors".to_string(),"scotty".to_string(),"sevens".to_string(),"harrow".to_string(),"welter".to_string(),"quacks".to_string(),"daybed".to_string(),"lorded".to_string(),"pulses".to_string(),"pokier".to_string(),"fatten".to_string(),"midges".to_string(),"joints".to_string(),"snoopy".to_string(),"looter".to_string(),"monies".to_string(),"canted".to_string(),"riffed".to_string(),"misses".to_string(),"bunker".to_string(),"piston".to_string(),"yessed".to_string(),"earner".to_string(),"hawked".to_string(),"wedged".to_string(),"brewer".to_string(),"nested".to_string(),"graver".to_string(),"hoaxes".to_string(),"slaves".to_string(),"pricks".to_string(),"magpie".to_string(),"bernie".to_string(),"rapier".to_string(),"roster".to_string(),"poohed".to_string(),"corner".to_string(),"trysts".to_string(),"rogers".to_string(),"whirls".to_string(),"bathed".to_string(),"teasel".to_string(),"opener".to_string(),"minced".to_string(),"sister".to_string(),"dreamy".to_string(),"worker".to_string(),"rinked".to_string(),"panted".to_string(),"triton".to_string(),"mervin".to_string(),"snowed".to_string(),"leafed".to_string(),"thinks".to_string(),"lesson".to_string(),"millet".to_string(),"larson".to_string(),"lagged".to_string(),"likely".to_string(),"stormy".to_string(),"fortes".to_string(),"hordes".to_string(),"wovens".to_string(),"kinked".to_string(),"mettle".to_string(),"seated".to_string(),"shirts".to_string(),"solver".to_string(),"giants".to_string(),"jilted".to_string(),"leaded".to_string(),"mendez".to_string(),"lowers".to_string(),"bidder".to_string(),"greats".to_string(),"pepped".to_string(),"flours".to_string(),"versus".to_string(),"canton".to_string(),"weller".to_string(),"cowper".to_string(),"tapped".to_string(),"dueled".to_string(),"mussed".to_string(),"rubies".to_string(),"bonged".to_string(),"steals".to_string(),"formed".to_string(),"smalls".to_string(),"sculls".to_string(),"docket".to_string(),"ouster".to_string(),"gunned".to_string(),"thumps".to_string(),"curred".to_string(),"withes".to_string(),"putted".to_string(),"buttes".to_string(),"bloats".to_string(),"parsed".to_string(),"galley".to_string(),"preses".to_string(),"tagged".to_string(),"hanger".to_string(),"planes".to_string(),"chords".to_string(),"shafts".to_string(),"carson".to_string(),"posits".to_string(),"zinger".to_string(),"solves".to_string(),"tensed".to_string(),"tastes".to_string(),"rinsed".to_string(),"kenned".to_string(),"bitten".to_string(),"leslie".to_string(),"chanty".to_string(),"candor".to_string(),"daises".to_string(),"baggie".to_string(),"wedded".to_string(),"paints".to_string(),"moored".to_string(),"haloed".to_string(),"hornet".to_string(),"lifted".to_string(),"fender".to_string(),"guiles".to_string(),"swifts".to_string(),"flicks".to_string(),"lancer".to_string(),"spares".to_string(),"pellet".to_string(),"passed".to_string(),"finked".to_string(),"joanna".to_string(),"bidden".to_string(),"swamps".to_string(),"lapped".to_string(),"leered".to_string(),"served".to_string(),"shirrs".to_string(),"choker".to_string(),"limper".to_string(),"marker".to_string(),"nudged".to_string(),"triter".to_string(),"thanks".to_string(),"peered".to_string(),"bruins".to_string(),"loaves".to_string(),"fabled".to_string(),"lathes".to_string(),"pipers".to_string(),"hooped".to_string(),"orates".to_string(),"burned".to_string(),"swines".to_string(),"sprats".to_string(),"warder".to_string(),"colder".to_string(),"crazes".to_string(),"reined".to_string(),"prized".to_string(),"majors".to_string(),"darrow".to_string(),"waifed".to_string(),"rooked".to_string(),"rickey".to_string(),"patter".to_string(),"shrive".to_string(),"gropes".to_string(),"gassed".to_string(),"throve".to_string(),"region".to_string(),"weaken".to_string(),"hettie".to_string(),"walton".to_string(),"galled".to_string(),"convoy".to_string(),"wesson".to_string(),"exudes".to_string(),"tinted".to_string(),"clanks".to_string(),"blinks".to_string(),"slacks".to_string(),"stilts".to_string(),"franny".to_string(),"socket".to_string(),"wished".to_string(),"kidded".to_string(),"knotty".to_string(),"turves".to_string(),"cashes".to_string(),"geared".to_string(),"sunned".to_string(),"glowed".to_string(),"sadden".to_string(),"harlem".to_string(),"testes".to_string(),"sweets".to_string(),"becket".to_string(),"blazes".to_string(),"batter".to_string(),"fellow".to_string(),"clovis".to_string(),"copier".to_string(),"shaped".to_string(),"husked".to_string(),"gimlet".to_string(),"rooney".to_string(),"taints".to_string(),"sashes".to_string(),"bossed".to_string(),"cootie".to_string(),"franck".to_string(),"probed".to_string(),"bagged".to_string(),"smocks".to_string(),"batten".to_string(),"spared".to_string(),"chills".to_string(),"relics".to_string(),"meyers".to_string(),"grader".to_string(),"tromps".to_string(),"dimmer".to_string(),"pasted".to_string(),"pepper".to_string(),"capped".to_string(),"played".to_string(),"junket".to_string(),"easier".to_string(),"palmed".to_string(),"pander".to_string(),"vaguer".to_string(),"bulged".to_string(),"dissed".to_string(),"borges".to_string(),"raises".to_string(),"wallow".to_string(),"jigged".to_string(),"bogged".to_string(),"burped".to_string(),"neater".to_string(),"rammed".to_string(),"fibers".to_string(),"castor".to_string(),"skirts".to_string(),"cancer".to_string(),"tilled".to_string(),"spored".to_string(),"dander".to_string(),"denims".to_string(),"budges".to_string(),"trucks".to_string(),"sowers".to_string(),"yapped".to_string(),"cadges".to_string(),"wrists".to_string(),"hacker".to_string(),"graved".to_string(),"vipers".to_string(),"noshes".to_string(),"minted".to_string(),"lessor".to_string(),"cassia".to_string(),"wrecks".to_string(),"hidden".to_string(),"brando".to_string(),"honeys".to_string(),"chilli".to_string(),"ragged".to_string(),"breded".to_string(),"punier".to_string(),"stacey".to_string(),"sisses".to_string(),"jocked".to_string(),"croaks".to_string(),"dinned".to_string(),"walker".to_string(),"heston".to_string(),"flares".to_string(),"coined".to_string(),"cannot".to_string(),"chocks".to_string(),"leases".to_string(),"wander".to_string(),"balder".to_string(),"warmer".to_string(),"bawled".to_string(),"donnie".to_string(),"damson".to_string(),"header".to_string(),"chilly".to_string(),"models".to_string(),"simper".to_string(),"watery".to_string(),"milked".to_string(),"poises".to_string(),"combed".to_string(),"toilet".to_string(),"gallop".to_string(),"sonnet".to_string(),"loosed".to_string(),"yawned".to_string(),"splays".to_string(),"pauses".to_string(),"bother".to_string(),"graphs".to_string(),"shrews".to_string(),"scones".to_string(),"manuel".to_string(),"milers".to_string(),"hotels".to_string(),"bennie".to_string(),"flores".to_string(),"spells".to_string(),"grimed".to_string(),"tenses".to_string(),"staged".to_string(),"puffer".to_string(),"posies".to_string(),"motion".to_string(),"fudged".to_string(),"fainer".to_string(),"tatter".to_string(),"seraph".to_string(),"nansen".to_string(),"months".to_string(),"muppet".to_string(),"tamera".to_string(),"shaman".to_string(),"falser".to_string(),"becker".to_string(),"lisbon".to_string(),"clefts".to_string(),"weeper".to_string(),"mendel".to_string(),"girder".to_string(),"takers".to_string(),"torsos".to_string(),"forked".to_string(),"dances".to_string(),"stated".to_string(),"yelled".to_string(),"scants".to_string(),"frothy".to_string(),"rolled".to_string(),"yodels".to_string(),"listen".to_string(),"craned".to_string(),"brooms".to_string(),"suffer".to_string(),"easter".to_string(),"shills".to_string(),"craves".to_string(),"bleeps".to_string(),"belled".to_string(),"dished".to_string(),"bordon".to_string(),"zither".to_string(),"jacket".to_string(),"lammer".to_string(),"kirked".to_string(),"shaved".to_string(),"atoned".to_string(),"frumpy".to_string(),"nosier".to_string(),"vender".to_string(),"graced".to_string(),"clingy".to_string(),"chants".to_string(),"wrests".to_string(),"cursed".to_string(),"prunes".to_string(),"tarter".to_string(),"stripe".to_string(),"coffee".to_string(),"veiled".to_string(),"tweeds".to_string(),"shrine".to_string(),"spines".to_string(),"kegged".to_string(),"melvin".to_string(),"gasser".to_string(),"market".to_string(),"marten".to_string(),"peeped".to_string(),"sanger".to_string(),"somber".to_string(),"spider".to_string(),"netted".to_string(),"radium".to_string(),"slings".to_string(),"scarfs".to_string(),"mended".to_string(),"creels".to_string(),"shaves".to_string(),"payers".to_string(),"bunked".to_string(),"movers".to_string(),"beings".to_string(),"conked".to_string(),"cozies".to_string(),"benton".to_string(),"codger".to_string(),"prints".to_string(),"gusset".to_string(),"longed".to_string(),"burner".to_string(),"jambed".to_string(),"mullet".to_string(),"fogged".to_string(),"scores".to_string(),"carbon".to_string(),"sleeks".to_string(),"helped".to_string(),"waxier".to_string(),"gilded".to_string(),"harlot".to_string(),"winces".to_string(),"tenser".to_string(),"lowell".to_string(),"ramsey".to_string(),"kennan".to_string(),"booted".to_string(),"beaver".to_string(),"rested".to_string(),"shouts".to_string(),"hickey".to_string(),"looped".to_string(),"swings".to_string(),"wonted".to_string(),"dilled".to_string(),"defers".to_string(),"lolled".to_string(),"pupped".to_string(),"cruets".to_string(),"solved".to_string(),"romper".to_string(),"defter".to_string(),"chokes".to_string(),"kithed".to_string(),"garnet".to_string(),"bookie".to_string(),"stared".to_string(),"stares".to_string(),"latter".to_string(),"lazies".to_string(),"fanned".to_string(),"wagged".to_string(),"dunces".to_string(),"corked".to_string(),"cloned".to_string(),"prided".to_string(),"baxter".to_string(),"pusses".to_string(),"boomed".to_string(),"masses".to_string(),"warren".to_string(),"weaves".to_string(),"delves".to_string(),"handed".to_string(),"merton".to_string(),"lusher".to_string(),"hepper".to_string(),"gibber".to_string(),"sender".to_string(),"parsec".to_string(),"snares".to_string(),"masher".to_string(),"seamed".to_string(),"sweats".to_string(),"welles".to_string(),"gagged".to_string(),"curter".to_string(),"mother".to_string(),"beeped".to_string(),"vealed".to_string(),"shoved".to_string(),"slaver".to_string(),"hacked".to_string(),"gutted".to_string(),"ranged".to_string(),"bashed".to_string(),"closer".to_string(),"storks".to_string(),"meshed".to_string(),"cortex".to_string(),"copper".to_string(),"severn".to_string(),"gripes".to_string(),"carlos".to_string(),"scares".to_string(),"crates".to_string(),"boiled".to_string(),"ginned".to_string(),"mouses".to_string(),"raided".to_string(),"greyed".to_string(),"verier".to_string(),"slopes".to_string(),"fenced".to_string(),"sniper".to_string(),"priced".to_string(),"flawed".to_string(),"buffed".to_string(),"spacey".to_string(),"favors".to_string(),"platen".to_string(),"miller".to_string(),"walled".to_string(),"cutter".to_string(),"skated".to_string(),"holier".to_string(),"beamed".to_string(),"waiter".to_string(),"drowns".to_string(),"clomps".to_string(),"quarks".to_string(),"bested".to_string(),"frisks".to_string(),"purged".to_string(),"scalds".to_string(),"marian".to_string(),"flower".to_string(),"howled".to_string(),"plover".to_string(),"bikers".to_string(),"trails".to_string(),"hagged".to_string(),"smirks".to_string(),"sitter".to_string(),"carmen".to_string(),"lanced".to_string(),"plants".to_string(),"nobler".to_string(),"yakked".to_string(),"thesis".to_string(),"lassen".to_string(),"margin".to_string(),"wagner".to_string(),"sifter".to_string(),"houses".to_string(),"screws".to_string(),"booker".to_string(),"dormer".to_string(),"meters".to_string(),"padded".to_string(),"loaded".to_string(),"cartel".to_string(),"sutton".to_string(),"willis".to_string(),"chatty".to_string(),"dunked".to_string(),"dreamt".to_string(),"dalton".to_string(),"fables".to_string(),"coveys".to_string(),"muller".to_string(),"shanty".to_string(),"adders".to_string(),"tailor".to_string(),"helper".to_string(),"liters".to_string(),"butted".to_string(),"maiman".to_string(),"hollie".to_string(),"gallon".to_string(),"xavier".to_string(),"shrank".to_string(),"mickey".to_string(),"rather".to_string(),"powers".to_string(),"keened".to_string(),"doused".to_string(),"kisses".to_string(),"flanks".to_string(),"dotted".to_string(),"phased".to_string(),"dumped".to_string(),"linger".to_string(),"kramer".to_string(),"spaced".to_string(),"soften".to_string(),"strife".to_string(),"rowers".to_string(),"hovers".to_string(),"crimes".to_string(),"crooks".to_string(),"carrel".to_string(),"braces".to_string(),"lander".to_string(),"shrove".to_string(),"skulks".to_string(),"banker".to_string(),"itches".to_string(),"dropsy".to_string(),"misted".to_string(),"pulped".to_string(),"cloche".to_string(),"fawned".to_string(),"states".to_string(),"teared".to_string(),"beeper".to_string(),"raider".to_string(),"groves".to_string(),"livery".to_string(),"aerier".to_string(),"keenan".to_string(),"severe".to_string(),"sabres".to_string(),"bogies".to_string(),"coated".to_string(),"harlow".to_string(),"tanked".to_string(),"mellow".to_string(),"cozier".to_string(),"shanks".to_string(),"spooky".to_string(),"blamed".to_string(),"tricks".to_string(),"sleets".to_string(),"punted".to_string(),"jumped".to_string(),"caxton".to_string(),"warped".to_string(),"halley".to_string(),"frisky".to_string(),"shines".to_string(),"skater".to_string(),"lumber".to_string(),"truces".to_string(),"sliced".to_string(),"gibbet".to_string(),"narked".to_string(),"chives".to_string(),"graves".to_string(),"gummed".to_string(),"holler".to_string(),"glazes".to_string(),"nieves".to_string(),"hushed".to_string(),"nought".to_string(),"prated".to_string(),"chored".to_string(),"cloudy".to_string(),"kidder".to_string(),"huston".to_string(),"straws".to_string(),"twined".to_string(),"gifted".to_string(),"rodney".to_string(),"haloes".to_string(),"france".to_string(),"wirier".to_string(),"mercia".to_string(),"rubbed".to_string(),"coaxed".to_string(),"sumner".to_string(),"snipes".to_string(),"nipper".to_string(),"leiden".to_string(),"madman".to_string(),"margie".to_string(),"footed".to_string(),"firmed".to_string(),"budded".to_string(),"froths".to_string(),"senior".to_string(),"hoover".to_string(),"tailed".to_string(),"glider".to_string(),"straps".to_string(),"stalks".to_string(),"billow".to_string(),"racked".to_string(),"javier".to_string(),"zoomed".to_string(),"shades".to_string(),"whores".to_string(),"braids".to_string(),"roused".to_string(),"sudden".to_string(),"dogies".to_string(),"fencer".to_string(),"snaked".to_string(),"flings".to_string(),"traded".to_string(),"gunner".to_string(),"snider".to_string(),"staten".to_string(),"levees".to_string(),"lathed".to_string(),"sailor".to_string(),"waited".to_string(),"muster".to_string(),"clothe".to_string(),"lulled".to_string(),"cargos".to_string(),"revved".to_string(),"sooths".to_string(),"flamed".to_string(),"borers".to_string(),"feller".to_string(),"bladed".to_string(),"oliver".to_string(),"collin".to_string(),"wusses".to_string(),"murder".to_string(),"parted".to_string(),"jailed".to_string(),"frayed".to_string(),"doored".to_string(),"cheeks".to_string(),"misled".to_string(),"belted".to_string(),"winter".to_string(),"merges".to_string(),"shaven".to_string(),"fudges".to_string(),"tabbed".to_string(),"forget".to_string(),"sloths".to_string(),"cachet".to_string(),"mealed".to_string(),"sassed".to_string(),"salter".to_string(),"haunts".to_string(),"ranger".to_string(),"rivets".to_string(),"deeded".to_string(),"reaped".to_string(),"damped".to_string(),"crated".to_string(),"youths".to_string(),"whacks".to_string(),"tamers".to_string(),"misery".to_string(),"seeped".to_string(),"eerier".to_string(),"tiller".to_string(),"busses".to_string(),"gloved".to_string(),"hushes".to_string(),"cronus".to_string(),"pruned".to_string(),"casket".to_string(),"direst".to_string(),"guilds".to_string(),"motley".to_string(),"spools".to_string(),"fevers".to_string(),"snores".to_string(),"greece".to_string(),"elides".to_string(),"waists".to_string(),"rattle".to_string(),"trader".to_string(),"juster".to_string(),"rashes".to_string(),"stoney".to_string(),"pipped".to_string(),"solder".to_string(),"sinner".to_string(),"prides".to_string(),"rugged".to_string(),"steers".to_string(),"gnarly".to_string(),"titter".to_string(),"cities".to_string(),"walter".to_string(),"stolen".to_string(),"steaks".to_string(),"hawker".to_string(),"weaned".to_string(),"jobbed".to_string(),"jacked".to_string(),"pikers".to_string(),"hipper".to_string(),"spoilt".to_string(),"beeves".to_string(),"craved".to_string(),"gotten".to_string(),"balked".to_string(),"sherry".to_string(),"looney".to_string(),"crisis".to_string(),"callie".to_string(),"swiped".to_string(),"fished".to_string(),"rooted".to_string(),"bopped".to_string(),"bowler".to_string(),"escher".to_string(),"chumps".to_string(),"jerrod".to_string(),"lefter".to_string(),"snooty".to_string(),"fillet".to_string(),"scales".to_string(),"comets".to_string(),"lisped".to_string(),"decked".to_string(),"clowns".to_string(),"horned".to_string(),"robber".to_string(),"bottle".to_string(),"reeled".to_string(),"crapes".to_string(),"banter".to_string(),"martel".to_string(),"dowels".to_string(),"brandt".to_string(),"sweeps".to_string(),"heeled".to_string(),"tabled".to_string(),"manors".to_string(),"danger".to_string(),"dionne".to_string(),"prayer".to_string(),"decker".to_string(),"millie".to_string(),"boated".to_string(),"damned".to_string(),"horses".to_string(),"globes".to_string(),"failed".to_string(),"lammed".to_string(),"nigher".to_string(),"joyner".to_string(),"sobers".to_string(),"chided".to_string(),"tipper".to_string(),"parcel".to_string(),"flakes".to_string(),"fugger".to_string(),"elated".to_string(),"hinder".to_string(),"hopper".to_string(),"crafts".to_string(),"wipers".to_string(),"badder".to_string(),"jessie".to_string(),"matted".to_string(),"wafted".to_string(),"pealed".to_string(),"cheats".to_string(),"elites".to_string(),"torres".to_string(),"bushed".to_string(),"sneaks".to_string(),"tidies".to_string(),"brings".to_string(),"stalls".to_string(),"payees".to_string(),"zonked".to_string(),"danker".to_string(),"poshes".to_string(),"smelts".to_string(),"stoops".to_string(),"warden".to_string(),"chicks".to_string(),"ramsay".to_string(),"budged".to_string(),"firmer".to_string(),"glazed".to_string(),"heated".to_string(),"slices".to_string(),"hovels".to_string(),"belied".to_string(),"shifts".to_string(),"pauper".to_string(),"tinges".to_string(),"weston".to_string(),"casted".to_string(),"titles".to_string(),"droves".to_string(),"roomer".to_string(),"modals".to_string(),"seamen".to_string(),"wearer".to_string(),"blonde".to_string(),"berlin".to_string(),"libbed".to_string(),"tensor".to_string(),"hokier".to_string(),"lambed".to_string(),"graped".to_string(),"headed".to_string(),"copped".to_string(),"eroses".to_string(),"fagged".to_string(),"filler".to_string(),"keener".to_string(),"stages".to_string(),"civets".to_string(),"spills".to_string(),"tithed".to_string(),"sullen".to_string(),"sucked".to_string(),"briton".to_string(),"whaler".to_string(),"hooded".to_string(),"tittle".to_string(),"bucket".to_string(),"furled".to_string(),"darned".to_string(),"planet".to_string(),"clucks".to_string(),"batted".to_string(),"dagger".to_string(),"brides".to_string(),"severs".to_string(),"pathos".to_string(),"grainy".to_string(),"relied".to_string(),"carpel".to_string(),"makers".to_string(),"lancet".to_string(),"slowed".to_string(),"messed".to_string(),"ravels".to_string(),"faster".to_string(),"gabbed".to_string(),"chance".to_string(),"grayed".to_string(),"santos".to_string(),"spends".to_string(),"chinos".to_string(),"saints".to_string(),"swirly".to_string(),"dories".to_string(),"wilson".to_string(),"milton".to_string(),"clangs".to_string(),"manual".to_string(),"nodded".to_string(),"signer".to_string(),"stript".to_string(),"etched".to_string(),"vaster".to_string(),"wastes".to_string(),"stored".to_string(),"minces".to_string(),"purred".to_string(),"marvin".to_string(),"pinned".to_string(),"skulls".to_string(),"heaved".to_string(),"wadded".to_string(),"fowled".to_string(),"hashed".to_string(),"mullen".to_string(),"relief".to_string(),"hatted".to_string(),"primed".to_string(),"chaffs".to_string(),"canned".to_string(),"lackey".to_string(),"showed".to_string(),"shandy".to_string(),"chases".to_string(),"maggie".to_string(),"deafen".to_string(),"bussed".to_string(),"differ".to_string(),"worked".to_string(),"marted".to_string(),"ducked".to_string(),"socked".to_string(),"fussed".to_string(),"greyer".to_string(),"herder".to_string(),"trusty".to_string(),"follow".to_string(),"samson".to_string(),"babies".to_string(),"whorls".to_string(),"stanks".to_string(),"manson".to_string(),"cranes".to_string(),"murrow".to_string(),"shrink".to_string(),"genius".to_string(),"holder".to_string(),"lenses".to_string(),"yucked".to_string(),"termed".to_string(),"ruined".to_string(),"junker".to_string(),"belies".to_string(),"joshed".to_string(),"cooled".to_string(),"basted".to_string(),"greeks".to_string(),"fuller".to_string(),"healer".to_string(),"carver".to_string(),"havens".to_string(),"drunks".to_string(),"sucker".to_string(),"lotion".to_string(),"glared".to_string(),"healed".to_string(),"pocked".to_string(),"rifles".to_string(),"weaved".to_string(),"canoed".to_string(),"punter".to_string(),"hinton".to_string(),"settle".to_string(),"boobed".to_string(),"hinted".to_string(),"scored".to_string(),"harder".to_string(),"status".to_string(),"sloven".to_string(),"hayden".to_string(),"golfed".to_string(),"scoots".to_string(),"bloods".to_string(),"slaked".to_string(),"jugged".to_string(),"louses".to_string(),"cassie".to_string(),"shaded".to_string(),"rushed".to_string(),"pitied".to_string(),"barked".to_string(),"honked".to_string(),"rasher".to_string(),"forced".to_string(),"shaver".to_string(),"vowels".to_string(),"holden".to_string(),"pelvis".to_string(),"blades".to_string(),"chests".to_string(),"preyer".to_string(),"floods".to_string(),"deanna".to_string(),"cation".to_string(),"mapper".to_string(),"falter".to_string(),"dabbed".to_string(),"mocker".to_string(),"nestle".to_string(),"shucks".to_string(),"heeded".to_string(),"ticker".to_string(),"binges".to_string(),"summer".to_string(),"slumps".to_string(),"lusted".to_string(),"scampi".to_string(),"crofts".to_string(),"gorges".to_string(),"pardon".to_string(),"torses".to_string(),"smokes".to_string(),"lashed".to_string(),"bailey".to_string(),"jabbed".to_string(),"calmer".to_string(),"preset".to_string(),"forbes".to_string(),"hasted".to_string(),"wormed".to_string(),"winged".to_string(),"minors".to_string(),"banner".to_string(),"grazed".to_string(),"hewers".to_string(),"kernel".to_string(),"jolted".to_string(),"sniped".to_string(),"clunky".to_string(),"ratios".to_string(),"blinds".to_string(),"ganges".to_string(),"misers".to_string(),"spikes".to_string(),"riders".to_string(),"hallow".to_string(),"grumpy".to_string(),"barren".to_string(),"summed".to_string(),"infers".to_string(),"places".to_string(),"jarred".to_string(),"killer".to_string(),"plaint".to_string(),"goofed".to_string(),"subbed".to_string(),"prudes".to_string(),"sipped".to_string(),"kookie".to_string(),"whines".to_string(),"droopy".to_string(),"palled".to_string(),"cherry".to_string(),"proves".to_string(),"mobbed".to_string(),"spaded".to_string(),"cheese".to_string(),"pluses".to_string(),"bathes".to_string(),"motels".to_string(),"spewed".to_string(),"soaked".to_string(),"howler".to_string(),"puffed".to_string(),"malled".to_string(),"shrike".to_string(),"slided".to_string(),"fulled".to_string(),"pouted".to_string(),"shames".to_string(),"lessen".to_string(),"ringed".to_string(),"teemed".to_string(),"grands".to_string(),"linked".to_string(),"wooten".to_string(),"feuded".to_string(),"deaden".to_string(),"scents".to_string(),"flutes".to_string(),"salton".to_string()]),
42);

}
}

```

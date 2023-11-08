---
title: 126. word ladder ii
date: '2021-09-02'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0126 word ladder ii
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={126}/>
 

  A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

  

  	Every adjacent pair of words differs by a single letter.

  	Every si for 1 <TeX>\leq</TeX> i <TeX>\leq</TeX> k is in wordList. Note that beginWord does not need to be in wordList.

  	sk <TeX>=</TeX><TeX>=</TeX> endWord

  

  Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

   

 >   Example 1:

  

 >   Input: beginWord <TeX>=</TeX> "hit", endWord <TeX>=</TeX> "cog", wordList <TeX>=</TeX> ["hot","dot","dog","lot","log","cog"]

 >   Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

 >   Explanation: There are 2 shortest transformation sequences:

 >   "hit" -> "hot" -> "dot" -> "dog" -> "cog"

 >   "hit" -> "hot" -> "lot" -> "log" -> "cog"

  

 >   Example 2:

  

 >   Input: beginWord <TeX>=</TeX> "hit", endWord <TeX>=</TeX> "cog", wordList <TeX>=</TeX> ["hot","dot","dog","lot","log"]

 >   Output: []

 >   Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> beginWord.length <TeX>\leq</TeX> 5

 >   	endWord.length <TeX>=</TeX><TeX>=</TeX> beginWord.length

 >   	1 <TeX>\leq</TeX> wordList.length <TeX>\leq</TeX> 1000

 >   	wordList[i].length <TeX>=</TeX><TeX>=</TeX> beginWord.length

 >   	beginWord, endWord, and wordList[i] consist of lowercase English letters.

 >   	beginWord !<TeX>=</TeX> endWord

 >   	All the words in wordList are unique.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::VecDeque;
use std::collections::HashMap;
use std::collections::HashSet;

#[derive(Debug, Clone, PartialEq, Eq)]
pub enum State {
    Unvisited,
    InQueue,
    Visited,
}
impl Solution {
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

    pub fn bfs(graph: &HashMap<usize, Vec<usize>>, queue: &mut VecDeque<(usize, usize)>, visited: &mut Vec<State>, parents: &mut Vec<usize>, paths: &mut Vec<Vec<Vec<usize>>>, oposite_visited: &Vec<State>) -> bool {
        let mut meet = false;
        if queue.is_empty() {
            return meet;
        }
        let (v, steps) = queue.front().unwrap();
        let end_steps = steps + 1;
        loop {
            if queue.is_empty() {
                return meet;
            }    
            let (v, steps) = queue.front().unwrap();
            let cur_steps = steps + 0;
            if cur_steps == end_steps {
                return meet;
            }
            let (v, steps) = queue.pop_front().unwrap();
            visited[v] = State::Visited;
            if graph.get(&v).is_none() {
                continue;
            }
            let neighbors = graph.get(&v).unwrap();
            for  i in 0..neighbors.len() {
                let neighbor = neighbors[i];
                if visited[neighbor] == State::Unvisited {
                    parents[neighbor] = v;
                    /*
                    if paths[neighbor].len() == 0 {
                        paths[neighbor] = vec![vec![v]];
                    } else {
                    }
                    */
                    let parent_paths = paths[v].clone();
                    if parent_paths.len() == 0 {
                        paths[neighbor] = vec![vec![v]];
                    } else {
                        let curr_paths = &mut paths[neighbor];
                        for j in 0..parent_paths.len() {
                            let mut path = parent_paths[j].clone();
                            path.push(v);
                            curr_paths.push(path);
                        }    
                    }
                    visited[neighbor] = State::InQueue;
                    if oposite_visited[neighbor] == State::InQueue {
                        meet = true;
                    }
                    queue.push_back((neighbor, cur_steps + 1));
                } else if visited[neighbor] == State::InQueue {
                    // Vec<Vec<Vec<usize>>>
                    let parent_path_len = paths[v][0].len();
                    let child_path_len = paths[neighbor][0].len();
                    if parent_path_len < child_path_len {
                        let mut new_paths: Vec<Vec<usize>> = vec![];
                        for path in paths[v].iter() {
                            let mut new_path = path.clone();
                            new_path.push(v);
                            new_paths.push(new_path);
                            // paths[neighbor].push(new_path);
                        }
                        for i in 0..new_paths.len() {
                            paths[neighbor].push(new_paths[i].clone());
                        }    
                    }
                }
            }
        }
    }
    pub fn calculate_intersection(begin_queue: &mut VecDeque<(usize, usize)>, end_queue: &mut VecDeque<(usize, usize)>) -> HashSet<usize> {
        let mut begin_set: HashSet<usize> = HashSet::new();
        while !begin_queue.is_empty() {
            let (v, _) = begin_queue.pop_front().unwrap();
            begin_set.insert(v);
        }
        let mut end_set: HashSet<usize> = HashSet::new();
        while !end_queue.is_empty() {
            let (v, _) = end_queue.pop_front().unwrap();
            end_set.insert(v);
        }
        let mut intersection: HashSet<usize> = HashSet::new();
        for &x in begin_set.intersection(&end_set) {
            intersection.insert(x);       
        }
        return intersection;
    }
    pub fn find_ladders(begin_word: String, end_word: String, word_list: Vec<String>) -> Vec<Vec<String>> {
        let mut word_list = word_list;
        let n = word_list.len();
        let begin_option: Option<usize> = (0..n).into_iter().find(|&i| Self::is_word_same(&begin_word, &word_list[i]));
        let begin = if begin_option.is_none() {n} else {begin_option.unwrap()};
        if begin_option.is_none() {
            word_list.push(begin_word);
        }
        let mut graph: HashMap<usize, Vec<usize>> = Self::build_graph(&word_list);
        // println!("graph: {:?}", graph);
        let n = word_list.len();
        let end: Option<usize> = (0..n).into_iter().find(|&i| Self::is_word_same(&end_word, &word_list[i]));
        if end.is_none() {
            return vec![];
        }
        let end = end.unwrap();
        //println!("begin: {:?}", begin);
        //println!("end: {:?}", end);

        let mut begin_visited: Vec<State> = vec![State::Unvisited; n]; 
        let mut begin_paths: Vec<Vec<Vec<usize>>> = vec![vec![]; n];
        let mut begin_parents: Vec<usize> = vec![usize::MAX; n];
        let mut begin_queue:VecDeque<(usize, usize)> = VecDeque::new();
        begin_queue.push_back((begin, 0));
        begin_visited[begin] = State::InQueue;
        let mut end_visited: Vec<State> = vec![State::Unvisited; n]; 
        let mut end_parents: Vec<usize> = vec![usize::MAX; n];
        let mut end_paths: Vec<Vec<Vec<usize>>> = vec![vec![]; n];
        let mut end_queue:VecDeque<(usize, usize)> = VecDeque::new();
        end_queue.push_back((end, 0));
        end_visited[end] = State::InQueue;

        while !begin_queue.is_empty() || !end_queue.is_empty() {
            let has_met = Self::bfs(&graph, &mut begin_queue, &mut begin_visited, &mut begin_parents,&mut begin_paths, &end_visited);
            if has_met {
                break;
            }
            let has_met = Self::bfs(&graph, &mut end_queue, &mut end_visited, &mut end_parents, &mut end_paths, &begin_visited);
            if has_met {
                break;
            }
        }
        let intersection: HashSet<usize> = Self::calculate_intersection(&mut begin_queue, &mut end_queue);
        let mut results: Vec<Vec<String>> = vec![];
    
        //println!("begin_paths: {:?}", begin_paths);
        //println!("end_paths: {:?}", end_paths);
        // println!("intersection: {:?}", intersection);
    
        for &x in intersection.iter() {
            /*
            println!("x: {}, word: {}", x, word_list[x]);
            for i in 0..begin_paths[x].len() {
                let result: Vec<String> = begin_paths[x][i].iter().map(|&k| word_list[k].clone()).collect();
                println!("begin_path: {:?}", result);
            }
            for i in 0..end_paths[x].len() {
                let result: Vec<String> = end_paths[x][i].iter().map(|&k| word_list[k].clone()).collect();
                println!("end_paths: {:?}", result);
            }
            println!("begin_paths: {:?}", begin_paths[x]);
            println!("end_paths: {:?}", end_paths[x]);
            */
            if end_paths[x].len() == 0 {
                for i in 0..begin_paths[x].len() {
                    let mut indices = begin_paths[x][i].clone();
                    indices.push(x);
                    let result: Vec<String> = indices.iter().map(|&k| word_list[k].clone()).collect();
                    results.push(result);        
                }
            } else {
                for i in 0..begin_paths[x].len() {
                    for j in 0..end_paths[x].len() {
                        let mut indices = begin_paths[x][i].clone();
                        indices.push(x);
                        for k in (0..end_paths[x][j].len()).rev() {
                            indices.push(end_paths[x][j][k]);
                        }
                        let result: Vec<String> = indices.iter().map(|&k| word_list[k].clone()).collect();
                        results.push(result);    
                    }
                }    
            }
        }
        results        
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_126() {
        assert_eq!(
            Solution::find_ladders("hit".to_string(), "cog".to_string(), 
            vec!["hot".to_string(),"dot".to_string(),"dog".to_string(),"lot".to_string(),"log".to_string(),"cog".to_string()]),
            vec![
                vec!["hit".to_string(),"hot".to_string(),"lot".to_string(),"log".to_string(),"cog".to_string()],
                vec!["hit".to_string(),"hot".to_string(),"dot".to_string(),"dog".to_string(),"cog".to_string()],
            ]);
        
        let empty: Vec<Vec<String>> = vec![];
        assert_eq!(
            Solution::find_ladders("hot".to_string(), "dog".to_string(), vec!["hot".to_string(),"dog".to_string()]), empty);
        assert_eq!(Solution::find_ladders("a".to_string(), "c".to_string(), vec!["a".to_string(),"b".to_string(),"c".to_string()]), vec![vec!["a".to_string(),"c".to_string()]]);
        assert_eq!(
            Solution::find_ladders("red".to_string(), "tax".to_string(), 
            vec_string!["ted","tex","red","tax","tad","den","rex","pee"]),
            vec![
                vec_string!["red","ted","tad","tax"],
                vec_string!["red","ted","tex","tax"],
                vec_string!["red","rex","tex","tax"]
            ]);
        assert_eq!(
            Solution::find_ladders("cet".to_string(), "ism".to_string(), 
            vec_string!["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]),
            vec![
                vec_string!["cet","get","gee","gte","ate","ats","its","ito","ibo","ibm","ism"],
                vec_string!["cet","cat","can","ian","inn","ins","its","ito","ibo","ibm","ism"],
                vec_string!["cet","cot","con","ion","inn","ins","its","ito","ibo","ibm","ism"]
            ]);
    }
}

```

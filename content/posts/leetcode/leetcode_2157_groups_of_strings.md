---
title: 2157. groups of strings
date: '2022-09-13'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 2157 groups of strings
---

You are given a 0-indexed array of strings words. Each string consists of lowercase English letters only. No letter occurs more than once in any string of words.



Two strings s1 and s2 are said to be connected if the set of letters of s2 can be obtained from the set of letters of s1 by any one of the following operations:



Adding exactly one letter to the set of the letters of s1.

Deleting exactly one letter from the set of the letters of s1.

Replacing exactly one letter from the set of the letters of s1 with any letter, including itself.

The array words can be divided into one or more non-intersecting groups. A string belongs to a group if any one of the following is true:



It is connected to at least one other string of the group.

It is the only string present in the group.

Note that the strings in words should be grouped in such a manner that a string belonging to a group cannot be connected to a string present in any other group. It can be proved that such an arrangement is always unique.



Return an array ans of size 2 where:



ans[0] is the total number of groups words can be divided into, and

ans[1] is the size of the largest group.

 



 > Example 1:



 > Input: words <TeX>=</TeX> ["a","b","ab","cde"]

 > Output: [2,3]

 > Explanation:

 > - words[0] can be used to obtain words[1] (by replacing 'a' with 'b'), and words[2] (by adding 'b'). So words[0] is connected to words[1] and words[2].

 > - words[1] can be used to obtain words[0] (by replacing 'b' with 'a'), and words[2] (by adding 'a'). So words[1] is connected to words[0] and words[2].

 > - words[2] can be used to obtain words[0] (by deleting 'b'), and words[1] (by deleting 'a'). So words[2] is connected to words[0] and words[1].

 > - words[3] is not connected to any string in words.

 > Thus, words can be divided into 2 groups ["a","b","ab"] and ["cde"]. The size of the largest group is 3.  

 > Example 2:



 > Input: words <TeX>=</TeX> ["a","ab","abc"]

 > Output: [1,3]

 > Explanation:

 > - words[0] is connected to words[1].

 > - words[1] is connected to words[0] and words[2].

 > - words[2] is connected to words[1].

 > Since all strings are connected to each other, they should be grouped together.

 > Thus, the size of the largest group is 3.

 



**Constraints:**



 > 1 <TeX>\leq</TeX> words.length <TeX>\leq</TeX> 2  104

 > 1 <TeX>\leq</TeX> words[i].length <TeX>\leq</TeX> 26

 > words[i] consists of lowercase English letters only.

 > No letter occurs more than once in words[i].


## Solution
### Rust
```rust

pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn group_strings(words: Vec<String>) -> Vec<i32> {
        pub fn build_graph(words: &Vec<String>) -> Vec<Vec<usize>> {
            pub fn convert_word_hashmap(word: &String) -> [i32; 26] {
                let chars: Vec<char> = word.chars().collect();
                let mut result = [0; 26];
                for i in 0..chars.len() {
                    let ch = chars[i] as usize - 'a' as usize;
                    result[ch] += 1;
                }
                result
            }
            pub fn is_distance_one(word1: &[i32; 26], word2: &[i32; 26]) -> bool {
                let sum_1: i32 = word1.iter().sum();
                let sum_2: i32 = word2.iter().sum();
                let diff_sum: i32 = (0..26).into_iter().map(|x| (word1[x] - word2[x]).abs()).sum();
                // println!("sum_1: {}, sum_2: {}, diff_sum: {}", sum_1, sum_2, diff_sum);
                if sum_1 == sum_2 {
                    return diff_sum == 2;
                }
                if sum_1 == sum_2 + 1 && diff_sum == 1 {
                    return true;
                }
                if sum_2 == sum_1 + 1 && diff_sum == 1 {
                    return true;
                }
                false
            }
            let n = words.len();
            let mut graph: Vec<Vec<usize>> = vec![vec![]; n];
            let words_hashmaps: Vec<[i32; 26]> = words.iter().map(convert_word_hashmap).collect();
            // println!("{:?}", words_hashmaps);
            for i in 0..n {
                let len_i = words[i].len();
                for j in i + 1..n {
                    let len_j = words[j].len();
                    if is_distance_one(&words_hashmaps[i],  &words_hashmaps[j]) {
                        graph[i].push(j);
                        graph[j].push(i);
                    }
                }
            }
            graph
        }
        
        pub fn dfs(graph: &Vec<Vec<usize>>, v: usize, visited: &mut Vec<bool>, count: &mut i32) {
            visited[v] = true;
            *count = *count + 1;
    
            let neighbors = &graph[v];
            for i in 0..neighbors.len() {
                if !visited[neighbors[i]] {
                    dfs(graph, neighbors[i], visited, count);
                }
            }
        }
        let n = words.len();
        let graph = build_graph(&words);
        let mut count = 0;
        for i in 0..n {
            if graph[i].len() == 0 {
                count += 1;
            } else {
                println!("{}: {:?}", words[i], graph[i]);
            }
        }
        println!("count: {}", count);
        // println!("{:?}", graph);
        let mut visited: Vec<bool> = vec![false; n];
        
        let mut groups = 0;
        let mut max_graph = i32::MIN;
        while let Some(v) = (0..n).into_iter().find(|&x| !visited[x]) {
            let mut count = 0;
            dfs(&graph, v, &mut visited, &mut count);
            groups += 1;
            max_graph = i32::max(max_graph, count);
        }
        vec![groups, max_graph]    
    }
    pub fn most_words_found(sentences: Vec<String>) -> i32 {
        /* 
        let nums:Vec<usize> = sentences.iter().map(|sentence| sentence.split(" ").count()).collect();
        nums.iter().max() as i32
        */
        0i32
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_2157() {
        // assert_eq!(Solution::group_strings(vec!["a".to_string(), "b".to_string(), "ab".to_string(),"cde".to_string()]), vec![2, 3]);
        // assert_eq!(Solution::group_strings(vec!["a".to_string(), "ab".to_string(), "abc".to_string()]), vec![1, 3]);
        assert_eq!(Solution::group_strings(vec_string!["umeihvaq","ezflcmsur","ynikwecaxgtrdbu","u","q","gwrv","ftcuw","ocdgslxprzivbja","zqrktuepxs","cpqolvnwxz","geqis","xgfdazthbrolci","vwnrjqzsoepa","udzckgenvbsty","lpqcw","nekpvchqfgdo","iapjhxvdrmwetz","gw","waxokchnmifsruj","vqp","vbpkij","ufjvbstzh","swiu","knslbdcahfrox","ctofplkhednmv","g","zk","idretzjbpl","pxqdauys","mfgrqaktbzpv","vdtq","wyxjrcie","kl","jpcdzmli","oth","yumdawhfbskcjo","rvfksqhu","swemnvjpg","rnl","zgd","rmzdbcsqht","ure","qlusoaxprtebn","zkbmvtpya","jszxuwevfidkm","smlft","cpwugmbzfsqr","cblkjevhp","iyfnozaulex","qvlok","wsgm","du","awyplckj","aey","ycsjqnt","vtoqzsyx","ejqixsmrdhlofyp","kvlmurbzjg","lysdahgpwmrcn","af","jkezhdu","etjzqiyghdnovm","ycwdfnluoke","kwshbx","pyvaznljqwes","xakinu","e","zjexfgvhtabwcy","thuvwlnjkbxym","jorzeslpidmhubq","wnr","qzdv","qeovrbmwzgpdh","jkioenptaygfubh","bvndzxijope","cudizhjntbes","rnhzitpqoexwb","ihezcmfqouyl","q","mwtsdjqn","hrmc","hxaocbyikluvqsf","d","vgwjzuaondbcm","ibqxltf","rzyhguptmesqo","ruwgy","jvprwhtzuf","aupngodjexkiw","yhijelwpvtsrbqc","gtick","koilywcfbs","elv","dehxzlitskq","ptvbkql","msfxyjahlzo","oslxzfwrpmtyh","gypuchkwa","rsqij","tw","igbcylqfhtmjkr","nryhzjgi","pw","bnfairow","xjzrf","olxfypjtmrncuv","ifhue","akcvofuyzwbj","tvhxfeuiykpwbsz","wnrztclfpm","ozvypnfwrqg","cwkgr","gjyzrucplbsfe","pdtzmfoy","wehd","bnvqhcmg","uyw","sgynxljqbf","tvxbq","wcmguioelbdrkvx","okvtyexuj","hjbc","uidcswzm","jemtkvshizaub","rmb","jpgnqdemzcxa","dmalekhiyj","akocedu","rlpqufcv","r","lohgs","xapnorj","cdb","icopdtzxy","xcrflvojqgpkwt","elv","rp","yv","u","atdxqeilhkg","olfvmrgkb","rplxskabvtqmhw","n","rldswkyoujmfxpn","rvgejzdusoya","hvoft","wskgmjchz","luagnzkj","ywe","i","wcqtsk","umpvywknjbxacsd","ynavjpcrgq","jyftmklci","xfol","zh","kut","zvawyielscotkn","p","wykpqdjoz","uabtpxkvq","uabtifwhrvxc","sdcamqup","srghwfptloxvke","sfdywtx","tuohnxzjqmac","pwxjyhdurnfz","axgfcuqtiyhjz","rwqpyh","bmoznqavicdgp","jcu","vnkc","jpb","nvfqyahjkul","radpctwixygb","pvjmk","s","dzyqjbwucne","mgh","ivc","eaqc","yjimsadtcwbgk","lo","ayirlsfevtwpnd","wcsk","xlvejy","kcjrqf","a","ixsdga","vk","cqxyfotziwrvl","zmxboiewhfdjlnr","kdpwngf","zyretijxpw","ncw","ljw","mrxeciy","aqwcofnjypsgi","byuvhj","ukidyqzhxgowmc","cpqsmu","auwmcrpdisbzokg","pxgwmvfq","azgljrsyeqwxfic","xmlgpdrzwqe","emgdcqntjpwrf","hrwq","zmjkx","npabcide","dvlfxnt","kilqsvmborf","lvsxjnbimhpzfow","sqcym","tcjmkwq","yugkwdzvmteon","pq","nklmb","azqcnodkimtxve","ovpcfe","uqkcwjimbvdyx","xvdazh","xk"]), 
            vec![190, 21]);
    }
}

```

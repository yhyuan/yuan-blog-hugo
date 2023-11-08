---
title: 721. accounts merge
date: '2022-05-01'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0721 accounts merge
---

 

  Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

  Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

  After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

   

 >   Example 1:

  

 >   Input: accounts <TeX>=</TeX> [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

 >   Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

 >   Explanation:

 >   The first and third John's are the same person as they have the common email "johnsmith@mail.com".

 >   The second John and Mary are different people as none of their email addresses are used by other accounts.

 >   We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 

 >   ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

  

 >   Example 2:

  

 >   Input: accounts <TeX>=</TeX> [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]

 >   Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> accounts.length <TeX>\leq</TeX> 1000

 >   	2 <TeX>\leq</TeX> accounts[i].length <TeX>\leq</TeX> 10

 >   	1 <TeX>\leq</TeX> accounts[i][j] <TeX>\leq</TeX> 30

 >   	accounts[i][0] consists of English letters.

 >   	accounts[i][j] (for j > 0) is a valid email.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
use std::collections::HashMap;
use std::collections::HashSet;
impl Solution {
    pub fn dfs(graph: &HashMap<usize, HashSet<usize>>, visited: &mut Vec<bool>, cluster: &mut Vec<usize>, index: usize) {
        visited[index] = true;
        if graph.contains_key(&index) {
            let neighbors = graph.get(&index).unwrap();
            for &neighbor in neighbors.iter() {
                if visited[neighbor] {
                    continue;
                }
                Self::dfs(graph, visited, cluster, neighbor);
            }
        }
        cluster.push(index);
    } 
    pub fn accounts_merge(accounts: Vec<Vec<String>>) -> Vec<Vec<String>> {
        let n = accounts.len();
        let mut emails: Vec<String> = vec![];
        let mut name_hashmap: HashMap<usize, usize> = HashMap::new();
        let mut hashmap: HashMap<String, usize> = HashMap::new();
        let mut graph: HashMap<usize, HashSet<usize>> = HashMap::new();
        for i in 0..n {
            for j in 1..accounts[i].len() {
                let email = &accounts[i][j];
                if !hashmap.contains_key(email) {
                    let size = emails.len();
                    hashmap.insert(email.clone(), size);
                    name_hashmap.insert(size, i);
                    emails.push(email.clone());
                }
                if j >= 2 {
                    let pre_email = &accounts[i][j - 1];
                    let start = hashmap.get(pre_email).unwrap();
                    let end = hashmap.get(email).unwrap();
                    let mut ends: HashSet<usize> = if graph.contains_key(start) {graph.get(start).unwrap().clone()} else {HashSet::new()};
                    ends.insert(*end);
                    graph.insert(*start, ends);

                    let mut starts: HashSet<usize> = if graph.contains_key(end) {graph.get(end).unwrap().clone()} else {HashSet::new()};
                    starts.insert(*start);
                    graph.insert(*end, starts);
                }
            }
        }
        let n = emails.len();
        let mut visited = vec![false; n];
        let mut result: Vec<Vec<String>> = vec![];
        for i in 0..n {
            if visited[i] {
                continue;
            }
            let mut cluster: Vec<usize> = vec![];
            Self::dfs(&graph, &mut visited, &mut cluster, i);
            let accound_index = *name_hashmap.get(&i).unwrap();
            let name = accounts[accound_index][0].clone();
            // println!("name: {}, cluster: {:?}", name, cluster);
            let mut emails = cluster.iter().map(|&i| emails[i].clone()).collect::<Vec<_>>();
            emails.sort();
            emails.insert(0, name);
            result.push(emails);
        }
        
        result
    }
}
*/
use std::collections::HashSet;
use std::collections::HashMap;
pub struct DisjointSet {
    parents: Vec<usize>,
    sizes: Vec<usize>,
}

impl DisjointSet {
    pub fn new(n: usize) -> DisjointSet {
        let mut parents = vec![0usize; n];
        for i in 0..n {
            parents[i] = i;
        }
        DisjointSet { 
            parents: parents,
            sizes: vec![1; n],
        }
    }

    pub fn find(&self, i: usize) -> usize {
        let mut i = i;
        while self.parents[i] != i {
            i = self.parents[i];
        }
        i
    }

    pub fn union(&mut self, i: usize, j: usize) {
        let i_parent = self.find(i);
        let j_parent = self.find(j);
        /*
        if i == 0 && j == 2 {
            println!("i_parent: {}, j_parent: {}", i_parent, j_parent);
        }
        */
        if i_parent == j_parent {
            return;
        }
        let i_size = self.sizes[i];
        let j_size = self.sizes[j];
        if i_size > j_size {
            self.parents[j_parent] = self.parents[i]; 
        } else {
            self.parents[i_parent] = self.parents[j]; 
        }
        self.sizes[j] = i_size + j_size;
        self.sizes[i] = i_size + j_size;
    }
}
impl Solution {
    pub fn accounts_merge(accounts: Vec<Vec<String>>) -> Vec<Vec<String>> {
        let n = accounts.len();
        let mut name_lookup_hashmap: HashMap<String, String> = HashMap::new();
        let mut email_set: HashSet<String> = HashSet::new();
        for i in 0..n {
            let name = &accounts[i][0];
            for j in 1..accounts[i].len() {
                email_set.insert(accounts[i][j].clone());
                name_lookup_hashmap.insert(accounts[i][j].clone(), name.clone());
            }
        }
        let mut emails = email_set.iter().collect::<Vec<_>>();
        emails.sort();
        let mut email_lookup_hashmap: HashMap<String, usize> = HashMap::new();
        for i in 0..emails.len() {
            email_lookup_hashmap.insert(emails[i].clone(), i);
        }
        let mut disjointSet: DisjointSet = DisjointSet::new(emails.len());

        for i in 0..n {
            let name = &accounts[i][0];
            let mut pre_index = 0usize;
            for j in 1..accounts[i].len() {
                let index = *email_lookup_hashmap.get(&accounts[i][j]).unwrap();
                if j == 1 {
                    pre_index = index;
                    continue;
                }
                //println!("pre_index: {}, index: {}", pre_index, index);
                disjointSet.union(pre_index, index);
                //println!("parents: {:?}", disjointSet.parents);
            }
        }
        //println!("emails: {:?}", emails);
        //println!("parents: {:?}", disjointSet.parents);
        let mut hashmap: HashMap<usize, Vec<usize>> = HashMap::new();
        for i in 0..emails.len() {
            let mut index = disjointSet.parents[i];
            while index != disjointSet.parents[index] {
                index = disjointSet.parents[index];
            }
            if hashmap.contains_key(&index) {
                let indices = hashmap.get(&index).unwrap();
                let mut indices = indices.clone();
                indices.push(i);
                hashmap.insert(index, indices);
            } else {
                hashmap.insert(index, vec![i]);
            }
        }
        let mut result: Vec<Vec<String>> = vec![];
        for (key, indices) in hashmap.iter() {
            let email = emails[*key].clone();
            let name = name_lookup_hashmap.get(&email).unwrap();
            //println!("{:?}", indices);
            let mut row = indices.into_iter().map(|&i| emails[i].clone()).collect::<Vec<_>>();
            row.insert(0, name.clone());
            result.push(row);
        }
        //println!("hashmap: {:?}", hashmap);

        result
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_721() {
        /*
        assert_eq!(Solution::accounts_merge(vec![
            vec_string!["John","johnsmith@mail.com","john_newyork@mail.com"],
            vec_string!["John","johnsmith@mail.com","john00@mail.com"],
            vec_string!["Mary","mary@mail.com"],
            vec_string!["John","johnnybravo@mail.com"]]), 
        vec![
            vec_string!["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
            vec_string!["Mary","mary@mail.com"],
            vec_string!["John","johnnybravo@mail.com"]]);
        
        assert_eq!(Solution::accounts_merge(vec![
            vec_string!["David","David0@m.co","David4@m.co","David3@m.co"],
            vec_string!["David","David5@m.co","David5@m.co","David0@m.co"],
            vec_string!["David","David1@m.co","David4@m.co","David0@m.co"],
            vec_string!["David","David0@m.co","David1@m.co","David3@m.co"],
            vec_string!["David","David4@m.co","David1@m.co","David3@m.co"]
            ]), 
        vec![vec_string!["David","David0@m.co","David1@m.co","David3@m.co","David4@m.co","David5@m.co"]]);
        */
        /*
        assert_eq!(Solution::accounts_merge(vec![
            vec_string!["David","David0@m.co","David1@m.co"],
            vec_string!["David","David3@m.co","David4@m.co"],
            vec_string!["David","David4@m.co","David5@m.co"],
            vec_string!["David","David2@m.co","David3@m.co"],
            vec_string!["David","David1@m.co","David2@m.co"]]), 
            vec![vec_string!["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]);
        */
        assert_eq!(Solution::accounts_merge(vec![
            vec_string!["David","David0@m.co","David5@m.co","David0@m.co"],
            vec_string!["Lily","Lily4@m.co","Lily2@m.co","Lily0@m.co"],
            vec_string!["Fern","Fern5@m.co","Fern2@m.co","Fern6@m.co"],
            vec_string!["Gabe","Gabe0@m.co","Gabe6@m.co","Gabe8@m.co"],
            vec_string!["Alex","Alex7@m.co","Alex5@m.co","Alex7@m.co"],
            vec_string!["Lily","Lily4@m.co","Lily6@m.co","Lily7@m.co"],
            vec_string!["Alex","Alex0@m.co","Alex4@m.co","Alex5@m.co"],
            vec_string!["John","John4@m.co","John2@m.co","John0@m.co"]            
            ]), 
            vec![
                vec_string!["David","David0@m.co","David5@m.co"],
                vec_string!["Fern","Fern2@m.co","Fern5@m.co","Fern6@m.co"],
                vec_string!["Gabe","Gabe0@m.co","Gabe6@m.co","Gabe8@m.co"],
                vec_string!["Alex","Alex0@m.co","Alex4@m.co","Alex5@m.co","Alex7@m.co"],
                vec_string!["Lily","Lily0@m.co","Lily2@m.co","Lily4@m.co","Lily6@m.co","Lily7@m.co"],
                vec_string!["John","John0@m.co","John2@m.co","John4@m.co"]
            ]);
    }
}

```

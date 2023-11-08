---
title: 2115. find all possible recipes from given supplies
date: '2022-09-07'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 2115 find all possible recipes from given supplies
---


You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.



You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.



Return a list of all the recipes that you can create. You may return the answer in any order.



Note that two recipes may contain each other in their ingredients.







> Example 1:
> Input: recipes <TeX>=</TeX> ["bread"], ingredients <TeX>=</TeX> [["yeast","flour"]], supplies <TeX>=</TeX> ["yeast","flour","corn"]
> Output: ["bread"]
> Explanation:
> We can create "bread" since we have the ingredients "yeast" and "flour".
> Example 2:
> Input: recipes <TeX>=</TeX> ["bread","sandwich"], ingredients <TeX>=</TeX> [["yeast","flour"],["bread","meat"]], supplies <TeX>=</TeX> ["yeast","flour","meat"]
> Output: ["bread","sandwich"]
> Explanation:
> We can create "bread" since we have the ingredients "yeast" and "flour".
> We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
> Example 3:
> Input: recipes <TeX>=</TeX> ["bread","sandwich","burger"], ingredients <TeX>=</TeX> [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies <TeX>=</TeX> ["yeast","flour","meat"]
> Output: ["bread","sandwich","burger"]
> Explanation:
> We can create "bread" since we have the ingredients "yeast" and "flour".
> We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
> We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".
**Constraints:**
> n <TeX>=</TeX><TeX>=</TeX> recipes.length <TeX>=</TeX><TeX>=</TeX> ingredients.length
> 1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 100
> 1 <TeX>\leq</TeX> ingredients[i].length, supplies.length <TeX>\leq</TeX> 100
> 1 <TeX>\leq</TeX> recipes[i].length, ingredients[i][j].length, supplies[k].length <TeX>\leq</TeX> 10
> recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
> All the values of recipes and supplies combined are unique.
> Each ingredients[i] does not contain any duplicate values.


## Solution


### Rust
```rust
pub struct Solution {}

use std::collections::HashMap;

impl Solution {
pub fn find_all_recipes(recipes: Vec<String>, ingredients: Vec<Vec<String>>, supplies: Vec<String>) -> Vec<String> {
let mut graph: HashMap<String, Vec<String>> = HashMap::new();
let mut indegrees: HashMap<String ,i32> = HashMap::new();
let n = recipes.len();
for i in 0..n {
for j in 0..ingredients[i].len() {
if graph.contains_key(&ingredients[i][j]) {
graph.get_mut(&ingredients[i][j]).unwrap().push(recipes[i].clone());
} else {
graph.insert(ingredients[i][j].clone(), vec![recipes[i].clone()]);
}
if indegrees.contains_key(&recipes[i]) {
*indegrees.get_mut(&recipes[i]).unwrap() += 1;
} else {
indegrees.insert(recipes[i].clone(), 1);
}
}
}
let mut ans: Vec<String> = vec![];
let mut completed_recipes: Vec<String> = supplies.clone();
loop {
let mut next_completed_recipes: Vec<String> = vec![];
for i in 0..completed_recipes.len() {
// println!("completed_recipes[i]: {}", completed_recipes[i]);
if !graph.contains_key(&completed_recipes[i]) {
continue;
}
for j in 0..graph[&completed_recipes[i]].len() {
let end_node = &graph[&completed_recipes[i]][j];
// println!("end_node: {}", end_node);
let indegree_node = indegrees[end_node];
if indegree_node == 1 {
next_completed_recipes.push(end_node.clone());
ans.push(end_node.clone());
indegrees.remove_entry(end_node);
} else {
*indegrees.get_mut(end_node).unwrap() -= 1;
}
}
}
completed_recipes = next_completed_recipes;
if completed_recipes.len() == 0 {
break;
}
}
ans
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_2096() {
assert_eq!(Solution::find_all_recipes(vec_string!["bread","sandwich","burger"], vec![vec_string!["yeast","flour"],vec_string!["bread","meat"],vec_string!["sandwich","meat","bread"]], vec_string!["yeast","flour","meat"]), vec_string!["bread","sandwich","burger"]);
}
}

```

---
title: 388. longest absolute file path
date: '2022-02-12'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0388 longest absolute file path
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={388}/>
 

  Suppose we have a file system that stores both files and directories. An example of one system is represented in the following picture:

  ![](https://assets.leetcode.com/uploads/2020/08/28/mdir.jpg)

  Here, we have dir as the only directory in the root. dir contains two subdirectories, subdir1 and subdir2. subdir1 contains a file file1.ext and subdirectory subsubdir1. subdir2 contains a subdirectory subsubdir2, which contains a file file2.ext.

  In text form, it looks like this (with ⟶ representing the tab character):

  

  dir

  ⟶ subdir1

  ⟶ ⟶ file1.ext

  ⟶ ⟶ subsubdir1

  ⟶ subdir2

  ⟶ ⟶ subsubdir2

  ⟶ ⟶ ⟶ file2.ext

  

  If we were to write this representation in code, it will look like this: "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext". Note that the '\n' and '\t' are the new-line and tab characters.

  Every file and directory has a unique absolute path in the file system, which is the order of directories that must be opened to reach the file/directory itself, all concatenated by '/'s. Using the above example, the absolute path to file2.ext is "dir/subdir2/subsubdir2/file2.ext". Each directory name consists of letters, digits, and/or spaces. Each file name is of the form name.extension, where name and extension consist of letters, digits, and/or spaces.

  Given a string input representing the file system in the explained format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/08/28/dir1.jpg)

 >   Input: input <TeX>=</TeX> "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"

 >   Output: 20

 >   Explanation: We have only one file, and the absolute path is "dir/subdir2/file.ext" of length 20.

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2020/08/28/dir2.jpg)

 >   Input: input <TeX>=</TeX> "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

 >   Output: 32

 >   Explanation: We have two files:

 >   "dir/subdir1/file1.ext" of length 21

 >   "dir/subdir2/subsubdir2/file2.ext" of length 32.

 >   We return 32 since it is the longest absolute path to a file.

  

 >   Example 3:

  

 >   Input: input <TeX>=</TeX> "a"

 >   Output: 0

 >   Explanation: We do not have any files, just a single directory named "a".

  

 >   Example 4:

  

 >   Input: input <TeX>=</TeX> "file1.txt\nfile2.txt\nlongfile.txt"

 >   Output: 12

 >   Explanation: There are 3 files at the root directory.

 >   Since the absolute path for anything at the root directory is just the name itself, the answer is "longfile.txt" with length 12.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> input.length <TeX>\leq</TeX> 10^4

 >   	input may contain lowercase or uppercase English letters, a new line character '\n', a tab character '\t', a dot '.', a space ' ', and digits.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn length_longest_path(input: String) -> i32 {
        if input.len() == 0 {
            return 0;
        }
        if !input.contains("\n") && !input.contains(".") {
            return 0;
        }
        let items: Vec<&str> = input.split("\n").collect();
        let sub_folder_n = items.iter().filter(|s| s.contains("\t")).count();
        if sub_folder_n == 0 {
            return items.iter()
                .filter(|filename| filename.contains('.')).map(|filename| filename.len()).max().unwrap() as i32;
        }
        println!("items: {:?}", items);
        let mut result = 0i32;
        let mut stack: Vec<usize> = vec![];
        for item in items {
            let mut i = 0;
            while item.chars().nth(i).unwrap() == '\t' {
                i += 1;
            }
            while stack.len() > i {
                stack.pop();
            }
            if item.contains('.') { //is filename
                let length: usize = stack.iter().sum::<usize>() + stack.len() + item.len() - i;
                result = i32::max(result, length as i32);
            } else { //folder
                stack.push(item.len() - i);
            }
        }
        result
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_388() {
        assert_eq!(Solution::length_longest_path("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext".to_string()), 20);
        assert_eq!(Solution::length_longest_path("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext".to_string()), 32);
        assert_eq!(Solution::length_longest_path("a".to_string()), 0);
        assert_eq!(Solution::length_longest_path("file1.txt\nfile2.txt\nlongfile.txt".to_string()), 12);
        assert_eq!(Solution::length_longest_path("a.tar.gz".to_string()), 8);
    }
}

```

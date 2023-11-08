---
title: 2166. design bitset
date: '2022-09-18'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 2166 design bitset
---


A Bitset is a data structure that compactly stores bits.



Implement the Bitset class:



Bitset(int size) Initializes the Bitset with size bits, all of which are 0.

void fix(int idx) Updates the value of the bit at the index idx to 1. If the value was already 1, no change occurs.

void unfix(int idx) Updates the value of the bit at the index idx to 0. If the value was already 0, no change occurs.

void flip() Flips the values of each bit in the Bitset. In other words, all bits with value 0 will now have value 1 and vice versa.

boolean all() Checks if the value of each bit in the Bitset is 1. Returns true if it satisfies the condition, false otherwise.

boolean one() Checks if there is at least one bit in the Bitset with value 1. Returns true if it satisfies the condition, false otherwise.

int count() Returns the total number of bits in the Bitset which have value 1.

String toString() Returns the current composition of the Bitset. Note that in the resultant string, the character at the ith index should coincide with the value at the ith bit of the Bitset.

 



 > Example 1:



 > Input

 > ["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one", "unfix", "count", "toString"]

 > [[5], [3], [1], [], [], [0], [], [], [0], [], []]

 > Output

 > [null, null, null, null, false, null, null, true, null, 2, "01010"]



 > Explanation

 > Bitset bs <TeX>=</TeX> new Bitset(5); // bitset <TeX>=</TeX> "00000".

 > bs.fix(3);     // the value at idx <TeX>=</TeX> 3 is updated to 1, so bitset <TeX>=</TeX> "00010".

 > bs.fix(1);     // the value at idx <TeX>=</TeX> 1 is updated to 1, so bitset <TeX>=</TeX> "01010". 

 > bs.flip();     // the value of each bit is flipped, so bitset <TeX>=</TeX> "10101". 

 > bs.all();      // return False, as not all values of the bitset are 1.

 > bs.unfix(0);   // the value at idx <TeX>=</TeX> 0 is updated to 0, so bitset <TeX>=</TeX> "00101".

 > bs.flip();     // the value of each bit is flipped, so bitset <TeX>=</TeX> "11010". 

 > bs.one();      // return True, as there is at least 1 index with value 1.

 > bs.unfix(0);   // the value at idx <TeX>=</TeX> 0 is updated to 0, so bitset <TeX>=</TeX> "01010".

 > bs.count();    // return 2, as there are 2 bits with value 1.

 > bs.toString(); // return "01010", which is the composition of bitset.

 



**Constraints:**



 > 1 <TeX>\leq</TeX> size <TeX>\leq</TeX> 105

 > 0 <TeX>\leq</TeX> idx <TeX>\leq</TeX> size - 1

 > At most 105 calls will be made in total to fix, unfix, flip, all, one, count, and toString.

 > At least one call will be made to all, one, count, or toString.

 > At most 5 calls will be made to toString.


## Solution
### Rust
```rust
pub struct Solution {}
struct Bitset {
    data: Vec<u128>,
    size: u32
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Bitset {

    fn new(size: i32) -> Self {
        Bitset {
            data: vec![0u128; size as usize / 128 + 1],
            size: size as u32
        }
    }
    
    fn fix(&mut self, idx: i32) {
        let idx = idx as usize;
        let i = idx / 128;
        let j = idx % 128;
        self.data[i] |= 1u128 << j; //0b0000_1000;
    }
    
    fn unfix(&mut self, idx: i32) {
        let idx = idx as usize;
        let i = idx / 128;
        let j = idx % 128;
        self.data[i] &= !(1u128 << j); //0b1111_0111;
    }
    
    fn flip(&mut self) {
        let j = self.size % 128;
        for i in 0..self.data.len() {
            self.data[i] = !self.data[i];
        }
        
    }
    
    fn all(&self) -> bool {
        for i in 0..self.data.len() - 1 {
            if self.data[i] != u128::MAX {
                return false;
            }
        }
        let j = self.size % 128;
        let mut v = self.data[self.data.len() - 1];
        for i in 0..j{
            if v % 2 == 0 {
                return false;
            }
            v = v / 2;
        }
        true
    }
    
    fn one(&self) -> bool {
        for i in 0..self.data.len() - 1 {
            if self.data[i] != 0u128 {
                return true;
            }
        }
        let j = self.size % 128;
        let mut v = self.data[self.data.len() - 1];
        for i in 0..j{
            if v % 2 == 1 {
                return true;
            }
            v = v / 2;
        }
        false
    }
    
    fn count(&self) -> i32 {
        let mut count = 0;
        for i in 0..self.data.len() - 1 {
            let c = self.data[i].count_ones();
            count = count + c;
        }
        let j = self.size % 128;
        let mut v = self.data[self.data.len() - 1];
        for i in 0..j{
            if v % 2 == 1 {
                count = count + 1;
            }
            v = v / 2;
        }
        count as i32
    }
    
    fn to_string(&self) -> String {
        let mut result = "".to_string();
        for i in 0..self.data.len() - 1 {
            let s = format!("{:0128b}", self.data[i]);
            let s: String = s.chars().rev().collect();
            result.push_str(&s);
        }
        let mut chars: Vec<char> = vec![];
        let j = self.size % 128;
        let mut v = self.data[self.data.len() - 1];
        for i in 0..j{
            if v % 2 == 1 {
                chars.insert(0, '1');
            } else {
                chars.insert(0, '0');                
            }
            v = v / 2;
        }
        let s: String = chars.iter().rev().collect();
        //let t: String = s.chars().rev().collect();
        result.push_str(&s);
        result
    }
}

```

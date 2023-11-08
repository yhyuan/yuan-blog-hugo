---
title: 900. rle iterator
date: '2022-06-05'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0900 rle iterator
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={900}/>
 

  We can use run-length encoding (i.e., RLE) to encode a sequence of integers. In a run-length encoded array of even length encoding (0-indexed), for all even i, encoding[i] tells us the number of times that the non-negative integer value encoding[i + 1] is repeated in the sequence.

  

  	For example, the sequence arr <TeX>=</TeX> [8,8,8,5,5] can be encoded to be encoding <TeX>=</TeX> [3,8,2,5]. encoding <TeX>=</TeX> [3,8,0,9,2,5] and encoding <TeX>=</TeX> [2,8,1,8,2,5] are also valid RLE of arr.

  

  Given a run-length encoded array, design an iterator that iterates through it.

  Implement the RLEIterator class:

  

  	RLEIterator(int[] encoded) Initializes the object with the encoded array encoded.

  	int next(int n) Exhausts the next n elements and returns the last element exhausted in this way. If there is no element left to exhaust, return -1 instead.

  

   

 >   Example 1:

  

 >   Input

 >   ["RLEIterator", "next", "next", "next", "next"]

 >   [[[3, 8, 0, 9, 2, 5]], [2], [1], [1], [2]]

 >   Output

 >   [null, 8, 8, 5, -1]

 >   Explanation

 >   RLEIterator rLEIterator <TeX>=</TeX> new RLEIterator([3, 8, 0, 9, 2, 5]); // This maps to the sequence [8,8,8,5,5].

 >   rLEIterator.next(2); // exhausts 2 terms of the sequence, returning 8. The remaining sequence is now [8, 5, 5].

 >   rLEIterator.next(1); // exhausts 1 term of the sequence, returning 8. The remaining sequence is now [5, 5].

 >   rLEIterator.next(1); // exhausts 1 term of the sequence, returning 5. The remaining sequence is now [5].

 >   rLEIterator.next(2); // exhausts 2 terms, returning -1. This is because the first term exhausted was 5,

 >   but the second term did not exist. Since the last term exhausted does not exist, we return -1.

  

   

  **Constraints:**

  

 >   	2 <TeX>\leq</TeX> encoding.length <TeX>\leq</TeX> 1000

 >   	encoding.length is even.

 >   	0 <TeX>\leq</TeX> encoding[i] <TeX>\leq</TeX> 10^9

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 10^9

 >   	At most 1000 calls will be made to next.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
struct RLEIterator {
    freq: HashMap<usize, i32>,
    nums: Vec<i32>,
    cur: usize,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RLEIterator {

    fn new(encoding: Vec<i32>) -> Self {
        let mut freq: HashMap<usize, i32> = HashMap::new();
        let mut nums: Vec<i32> = vec![];
        let n = encoding.len();
        let mut freq_val = 0;
        for i in 0..n {
            if i % 2 == 0 {
                freq_val = encoding[i];
            } else {
                if freq_val > 0 {
                    nums.push(encoding[i]);
                    freq.insert(nums.len() - 1, freq_val);    
                }
            }
        }
        let cur = 0;
        Self { freq, nums, cur }
    }
    
    fn next(&mut self, n: i32) -> i32 {
        let mut n = n;
        while n > 0 {
            if self.cur == self.nums.len() {
                return -1;
            }
            let digit = self.nums[self.cur];
            let digit_freq = self.freq[&self.cur];
            if digit_freq > n {
                self.freq.insert(self.cur, digit_freq - n);
                return digit;
            } else {
                // self.freq.remove_entry(&digit);
                //println!("remove: {}, n: {}, digit_freq: {}", self.digits[0], n, digit_freq);
                //self.digits.remove(0);
                self.cur += 1;
                if digit_freq == n {
                    return digit;
                }
                n = n - digit_freq;
            }
        }
        unreachable!()
    }
}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * let obj = RLEIterator::new(encoding);
 * let ret_1: i32 = obj.next(n);
 */

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_900() {
        
        let mut obj = RLEIterator::new(vec![3, 8, 0, 9, 2, 5]);
        assert_eq!(obj.next(2), 8);
        assert_eq!(obj.next(1), 8);
        assert_eq!(obj.next(1), 5);
        assert_eq!(obj.next(2), -1);
        
        let mut obj = RLEIterator::new(vec![
            368,989,
            261,777,
            431,358,
            63,864,
            702,903,
            452,677,
            119,398,
            207,42,
            948,216,
            146,198,
            378,546,
            151,989,
            983,148,
            406,680,
            878,495,
            917,322,
            498,499,
            670,202,
            610,218,
            340,963,
            899,818,
            35,148,
            257,784,
            843,583,
            718,807,
            66,84,
            869,39,225,40,15,844,330,160,148,656,969,505,901,502,574,679,805,758,991,747,906,206,535,599,826,482,791,388,586,852,798,657,0,182,507,254,65,860,943,303,408,810,62,641,127,287,830,55,35,418,492,864,717,674,151,987,411,612,387,47,471,151,32,618,630,105,549,347,383,777,490,882,610,467,632,338,124,683,622,789,127,912,800,917,873,681,811,519,786,189,782,445,757,455,790,75,44,935,486,901,945,667,572,216,93,820,889,780,699,420,305,113,426,566,923,936,416,99,774,735,30,447,687,30,920,963,723,78,70,359,29,348,9,975,819,70,894,208,204,674,939,123,7,369,24,605,860,187,112,344,960,130,967,362,473,292,938,959,636,184,993,102,581,156,898,946,805,316,243,755,291,420,46,132,20,77,73,420,551,741,142,422,637,84,445,369,949,57,409,417,728,320,204,293,471,951,797,277,558,688,796,446,399,768,432,248,453,938,142,462,637,483,203,1,699,619,7,298,769,629,545,156,707,471,678,760,232,762,280,984,120,884,40,256,526,582,396,102,252,283,755,909,596,35,793,305,340,530,249,920,163,415,289,520,574,627,531,411,635,403,779,788,292,372,629,157,697,381,591,139,668,354,473,415,477,695,318,652,60,300,745,52,621,25,472,889,10,527,66,867,686,742,669,6,41,621,1000,874,700,727,226,752,288,105,461,330,168,422,898,435,447,709,524,129,911,444,790,389,807,389,220,196,940,587,49,388,234,84,186,57,638,173,611,613,705,512,284,878,353,458,632,516,957,955,930,935,581,490,704,215,266,43,163,3,655,140,787,681,971,396,922,454,339,102,883,795,323,456,325,28,44,369,209,525,187,201,673,736,312,860,254,344,713,44,935,72,461,725,47,809,979,460,118,81,98,766,414,920,441,77,427,755,830,39,180,490,128,871,935,319,435,557,285,541,201,296,442,605,536,261,232,118,784,98,733,249,284,736,660,742,515,859,121,645,118,738,359,675,704,661,221,832,240,518,675,233,629,287,171,810,553,328,586,25,129,395,976,510,76,765,782,775,570,696,213,733,816,760,353,591,629,901,108,834,526,358,456,12,220,653,661,495,954,481,314,848,259,604,704,822,786,384,59,38,727,962,343,441,726,658,260,672,305,356,540,733,151,22,628,24,45,226,654,66,62,973,423,893,216,435,358,177,329,987,748,383,409,264,531,736,687,463,41,922,409,390,3,138,869,514,733,148,330,840,821,247,21,807,169,788,684,168,78,928,598,621,457,150,602,252,806,733,27,933,36,89,293,150,236,356,736,405,270,492,392,311,901,550,978,773,571,262,687,456,722,404,496,20,740,34,681,582,776,290,686,207,529,340,979,972,209,566,329,969,925,586,720,682,353,917,900,330,748,9,817,565,953,363,626,323,783,601,988,1,140,43,125,930,949,480,947,819,779,748,187,549,424,950,174,170,659,157,110,504,797,605,755,266,285,429,991,718,947,538,555,991,190,783,792,845,750,155,661,924,563,361,950,562,412,614,804,228,15,529,942,680,631,628,497,731,249,892,274,945,927,78,448,744,450,509,807,705,958,164,924,928,635,941,252,882,774,610,90,30,10,250,763,387,776,626,389,881,38,465,830,126,711,328,24,474,522,41,566,347,4,190,110,541,43,929,845,946,315,906,985,765,275,671,596,404,306,59,125,134,481,642,764,46,824,43,555,744,631,950,345,586,82,560,814,201,261,701,254,259,936,999,155,901,553,38,586,642,33,758,818,71,649,457,238,459,159,333,655,476,556,543,821,343,813,80,428,352,452,834,512,988,862,118,317,22,734,19,886,193,414,62,311,389,52,768,712,358,836,77,54,355,902,757,672,563,804,412,30,803,190,388,357,123,351,177,616,654,13,456,554,872,496,80,51,862,791,859,262,648,95,827,333,956,471,33,909,626,287,36,377,157,548,147,174,921,640,242,879,625,946,483,888,679,44,240,281,170,238,226,879,463,877,138,565,13,931,5,390,802,1000,19,824,510,38,777,112,612,779,674,380,26,436,914,333,248,137,510,533,73,408,659,967,431,436,471,225,395,645,397,581,836,998,885,372,21,612,475,237,40,321,798,965,106,878,48,714,26,421,871,393,925,713,604,161,340,411,590,997,283,504,934,345,629]);
        assert_eq!(obj.next(11650), 807);
        //assert_eq!(obj.next(1), 8);
        //assert_eq!(obj.next(1), 5);
        //assert_eq!(obj.next(2), -1);

    }
}

```

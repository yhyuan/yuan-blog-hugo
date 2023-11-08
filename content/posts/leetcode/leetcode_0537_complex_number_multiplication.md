---
title: 537. complex number multiplication
date: '2022-03-28'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0537 complex number multiplication
---

 

  A [complex number](https://en.wikipedia.org/wiki/Complex_number) can be represented as a string on the form "real+imaginaryi" where:

  

  	real is the real part and is an integer in the range [-100, 100].

  	imaginary is the imaginary part and is an integer in the range [-100, 100].

  	i^2 <TeX>=</TeX><TeX>=</TeX> -1.

  

  Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.

   

 >   Example 1:

  

 >   Input: num1 <TeX>=</TeX> "1+1i", num2 <TeX>=</TeX> "1+1i"

 >   Output: "0+2i"

 >   Explanation: (1 + i)  (1 + i) <TeX>=</TeX> 1 + i2 + 2  i <TeX>=</TeX> 2i, and you need convert it to the form of 0+2i.

  

 >   Example 2:

  

 >   Input: num1 <TeX>=</TeX> "1+-1i", num2 <TeX>=</TeX> "1+-1i"

 >   Output: "0+-2i"

 >   Explanation: (1 - i)  (1 - i) <TeX>=</TeX> 1 + i2 - 2  i <TeX>=</TeX> -2i, and you need convert it to the form of 0+-2i.

  

   

  **Constraints:**

  

 >   	num1 and num2 are valid complex numbers.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
#[derive(PartialEq, Eq, Clone, Debug)]
struct ComplexNumber {
    real: i32,
    img: i32,
}

impl ComplexNumber {
    pub fn new(num: String) -> Self {
        let items: Vec<&str> = num.split("+").collect();
        if items.len() != 2 {
            core::panic!("Wrong input!");
        }
        let real_str = items[0];
        let img_str = items[1];
        let last_char = img_str.chars().last().unwrap();
        if last_char != 'i' {
            core::panic!("Wrong input!")
        }
        
        let img_str = &img_str[..img_str.len() - 1];
        let real = real_str.parse::<i32>().unwrap();
        let img = img_str.parse::<i32>().unwrap();
        ComplexNumber {real: real, img: img}
    }
}

impl std::ops::Mul for ComplexNumber {
    // The multiplication of rational numbers is a closed operation.
    type Output = Self;

    fn mul(self, rhs: Self) -> Self {
        let real = self.real * rhs.real - self.img * rhs.img;
        let img = self.img * rhs.real + self.real * rhs.img;
        ComplexNumber {real: real, img: img}
    }
}

impl std::fmt::Display for ComplexNumber {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "{}+{}i", self.real, self.img)
    }
}

impl Solution {
    pub fn complex_number_multiply(num1: String, num2: String) -> String {
        let num1 = ComplexNumber::new(num1);
        let num2 = ComplexNumber::new(num2);
        let num = num1 * num2;
        format!("{}", num)
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_537() {
        assert_eq!(Solution::complex_number_multiply("1+1i".to_string(), "1+1i".to_string()), "0+2i".to_string());
        assert_eq!(Solution::complex_number_multiply("1+-1i".to_string(), "1+-1i".to_string()), "0+-2i".to_string());
    }
}

```

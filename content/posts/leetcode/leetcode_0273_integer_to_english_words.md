---
title: 273. integer to english words
date: '2021-12-10'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0273 integer to english words
---

 

  Convert a non-negative integer num to its English words representation.

   

 >   Example 1:

 >   Input: num <TeX>=</TeX> 123

 >   Output: "One Hundred Twenty Three"

 >   Example 2:

 >   Input: num <TeX>=</TeX> 12345

 >   Output: "Twelve Thousand Three Hundred Forty Five"

 >   Example 3:

 >   Input: num <TeX>=</TeX> 1234567

 >   Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

 >   Example 4:

 >   Input: num <TeX>=</TeX> 1234567891

 >   Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

   

  **Constraints:**

  

 >   	0 <TeX>\leq</TeX> num <TeX>\leq</TeX> 2^31 - 1


## Solution
Solution:

Let's divide to the following cases:

0. We can simply return "Zero"

less than 1000 and larger than 0. We will write a function to process it. 

less than 1000000 and <TeX>\geq</TeX> 1000. We separate the number to divide 1000 and get it s remain. If the remain is 0, we can simply convert the division result and add "Thousand" behind it. Otherwise, we call the function again with division result and remain and put them together with Thousand. 

less than 1000000000 and <TeX>\geq</TeX> 1000000. We separate the number to divide 1000000 and get it s remain. If the remain is 0, we can simply convert the division result and add "Million" behind it. Otherwise, we call the function again with division result and remain and put them together with Million. 

<TeX>\geq</TeX> 1000000000. We separate the number to divide 1000000000 and get it s remain. If the remain is 0, we can simply convert the division result and add "Billion" behind it. Otherwise, we call the function again with division result and remain and put them together with Billion.

So the key to solve this problem is to deal with case 2 (larger than 0 and less than 1000). First let's define the following array:

```
numbers = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
 tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
```
Then, let's analyze the following cases:

num less than 20. We can simple find the sting in numbers and return it. 

num less than 100 and num <TeX>\geq</TeX> 20. We can find whether num can be divided by 10 or not. we can run the string in tens or put the remain behind it. 

num less than 1000 and num <TeX>\geq</TeX> 100. We first get hundred digit.

The remain part is 0. So we can simply add a "Hundred" after look up in numbers. 

The remain part is less than 20. We can lookup the string inside numbers and added it behind Hundred. 

The remain part is 30, 40, ... 90. We can lookup the string in tens and added it behind Hundred.

We can lookup the string in tens and string in numbers and added it behind Hundred. 

### Python
```python
def numberToWords(self, num: int) -> str:
  numbers = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
  tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
  if num == 0:
    return "Zero"
  if num < 1000:
    if num < 20:
      return numbers[num]

    if num < 100:
      ten = num // 10
      one = num % 10
      if one == 0:
        return tens[ten]
      return tens[ten] + " " + numbers[one]

    hundred = num // 100
    hundred_remain = num % 100
    if hundred_remain == 0:
      return numbers[hundred] + " Hundred"
    if hundred_remain < 20:
      return numbers[hundred] + " Hundred " + numbers[hundred_remain]
    ten = hundred_remain // 10
    one = num % 10
    if one == 0:
      return numbers[hundred] + " Hundred " + tens[ten]
    return numbers[hundred] + " Hundred " + tens[ten] + " " + numbers[one]
        
  if num < 1000000:
    thousand = num // 1000
    thousand_remain = num % 1000
    if thousand_remain == 0:
      return self.numberToWords(thousand) + " Thousand"
    return self.numberToWords(thousand) + " Thousand " + self.numberToWords(thousand_remain)
        
  if num < 1000000000:
    million = num // 1000000
    million_remain = num % 1000000
    if million_remain == 0:
      return self.numberToWords(million) + " Million"
    return self.numberToWords(million) + " Million " + self.numberToWords(million_remain)

  billion = num // 1000000000
  billion_remain = num % 1000000000
  if billion_remain == 0:
    return self.numberToWords(billion) + " Billion"
  return self.numberToWords(billion) + " Billion " + self.numberToWords(billion_remain)
```
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn number_to_words(num: i32) -> String {
        let numbers: [&str; 20] = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                                    "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"];
        let ten_numbers: [&str; 10] = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"];
        if num == 0 {
            return "Zero".to_string();
        }
        if num < 1000 {
            let hundred = num / 100;
            let result = if hundred == 0 {"".to_string()} else {format!("{} Hundred", numbers[hundred as usize])};
            let remain = num % 100;
            if remain == 0 {
                return result;
            }
            if remain <= 19 {
                if result.len() == 0 {
                    return format!("{}", numbers[remain as usize]);
                } else {
                    return format!("{} {}", result, numbers[remain as usize]);
                }
            }
            let ten = (remain / 10) as usize;
            let one = (remain % 10) as usize;
            let mut items: Vec<String> = vec![ten_numbers[ten].to_string()];
            if one > 0 {
                items.push(numbers[one].to_string()); 
            }
            if result.len() > 0 {
                items.insert(0, result);
            }
            let result: String = items.join(" ");
            return result;
        }
        if num < 1000000 {
            let thousand = Solution::number_to_words(num / 1000);
            if num % 1000 == 0 {
                return format!("{} Thousand", thousand);
            }
            let remain = Solution::number_to_words(num % 1000);
            return format!("{} Thousand {}", thousand, remain);
        }
        if num < 1000000000 {
            let million = Solution::number_to_words(num / 1000000);
            if num % 1000000 == 0 {
                return format!("{} Million", million);
            }
            let remain = Solution::number_to_words(num % 1000000);
            return format!("{} Million {}", million, remain);
        }
        let billion = Solution::number_to_words(num / 1000000000);
        if num % 1000000000 == 0 {
            return format!("{} Billion", billion);
        }
        let remain = Solution::number_to_words(num % 1000000000);
        return format!("{} Billion {}", billion, remain);
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_273() {
        //2,147,483,648
        //1,234,567,891
        //1,234,567
        //12,345
        
        assert_eq!(Solution::number_to_words(1000010), "One Million Ten".to_string());
        assert_eq!(Solution::number_to_words(1000), "One Thousand".to_string());
        assert_eq!(Solution::number_to_words(20), "Twenty".to_string());
        assert_eq!(Solution::number_to_words(0), "Zero".to_string());
        assert_eq!(Solution::number_to_words(123), "One Hundred Twenty Three".to_string());
        assert_eq!(Solution::number_to_words(12345), "Twelve Thousand Three Hundred Forty Five".to_string());
        assert_eq!(Solution::number_to_words(1234567), "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven".to_string());
        assert_eq!(Solution::number_to_words(1234567891), "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One".to_string());
    }
}

```

---
title: 2034. stock price fluctuation
date: '2022-09-05'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 2034 stock price fluctuation
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={2034}/>

You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.



Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.



Design an algorithm that:



Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.

Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.

Finds the maximum price the stock has been based on the current records.

Finds the minimum price the stock has been based on the current records.

Implement the StockPrice class:



StockPrice() Initializes the object with no price records.

void update(int timestamp, int price) Updates the price of the stock at the given timestamp.

int current() Returns the latest price of the stock.

int maximum() Returns the maximum price of the stock.

int minimum() Returns the minimum price of the stock.

 



 > Example 1:



 > Input

 > ["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]

 > [[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]

 > Output

 > [null, null, null, 5, 10, null, 5, null, 2]



 > Explanation

 > StockPrice stockPrice <TeX>=</TeX> new StockPrice();

 > stockPrice.update(1, 10); // Timestamps are [1] with corresponding prices [10].

 > stockPrice.update(2, 5);  // Timestamps are [1,2] with corresponding prices [10,5].

 > stockPrice.current();     // return 5, the latest timestamp is 2 with the price being 5.

 > stockPrice.maximum();     // return 10, the maximum price is 10 at timestamp 1.

 > stockPrice.update(1, 3);  // The previous timestamp 1 had the wrong price, so it is updated to 3.

 >                           // Timestamps are [1,2] with corresponding prices [3,5].

 > stockPrice.maximum();     // return 5, the maximum price is 5 after the correction.

 > stockPrice.update(4, 2);  // Timestamps are [1,2,4] with corresponding prices [3,5,2].

 > stockPrice.minimum();     // return 2, the minimum price is 2 at timestamp 4.

 



**Constraints:**



 > 1 <TeX>\leq</TeX> timestamp, price <TeX>\leq</TeX> 109

 > At most 105 calls will be made in total to update, current, maximum, and minimum.

 > current, maximum, and minimum will be called only after update has been called at least once.


## Solution
### Rust
```rust
pub struct Solution {}

use std::collections::HashMap;
use std::collections::BinaryHeap;

struct StockPrice {
    stock_prices: HashMap<i32, i32>,
    current: i32,
    max_heap: BinaryHeap<(i32, i32)>, // price, timestamp value
    min_heap: BinaryHeap<(i32, i32)>, // price, timestamp value
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl StockPrice {

    fn new() -> Self {
        let stock_prices: HashMap<i32, i32> = HashMap::new();
        let current: i32 = i32::MIN;
        let max_heap: BinaryHeap<(i32, i32)> = BinaryHeap::new();
        let min_heap: BinaryHeap<(i32, i32)> = BinaryHeap::new();
        Self { stock_prices, current, max_heap, min_heap }
    }
    
    fn update(&mut self, timestamp: i32, price: i32) {
        self.max_heap.push((price, timestamp));
        self.min_heap.push((-price, timestamp));
        self.stock_prices.insert(timestamp, price);
        if timestamp > self.current {
            self.current = timestamp;
        }
    }
    
    fn current(&self) -> i32 {
        self.stock_prices[&self.current]
    }
    
    fn maximum(&mut self) -> i32 {
        let (mut price, mut timestamp) = self.max_heap.peek().unwrap();
        while price != self.stock_prices[&timestamp] {
            self.max_heap.pop().unwrap();
            let item = self.max_heap.peek().unwrap();
            price = item.0;
            timestamp = item.1;
        }
        price
    }
    
    fn minimum(&mut self) -> i32 {
        let (mut price, mut timestamp) = self.min_heap.peek().unwrap();
        while -price != self.stock_prices[&timestamp] {
            self.min_heap.pop().unwrap();
            let item = self.min_heap.peek().unwrap();
            price = item.0;
            timestamp = item.1;
        }
        -price
    }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * let obj = StockPrice::new();
 * obj.update(timestamp, price);
 * let ret_2: i32 = obj.current();
 * let ret_3: i32 = obj.maximum();
 * let ret_4: i32 = obj.minimum();
 */

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_2096() {
        let mut obj = StockPrice::new();
        obj.update(1, 10);
        obj.update(2, 5);
        assert_eq!(obj.current(), 5);
        assert_eq!(obj.maximum(), 10);
        assert_eq!(obj.minimum(), 5);
    }
}

```

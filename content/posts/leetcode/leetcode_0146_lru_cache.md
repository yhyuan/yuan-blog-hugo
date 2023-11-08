---
title: 146. lru cache
date: '2021-09-18'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 0146 lru cache
---

 

  Design a data structure that follows the constraints of a [Least Recently Used (LRU) cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU).

  Implement the LRUCache class:

  

  	LRUCache(int capacity) Initialize the LRU cache with positive size capacity.

  	int get(int key) Return the value of the key if the key exists, otherwise return -1.

  	void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

  

  The functions get and put must each run in O(1) average time complexity.

   

 >   Example 1:

  

 >   Input

 >   ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]

 >   [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

 >   Output

 >   [null, null, null, 1, null, -1, null, -1, 3, 4]

 ```
    Explanation

    LRUCache lRUCache = new LRUCache(2);

    lRUCache.put(1, 1); // cache is {1=1}

    lRUCache.put(2, 2); // cache is {1=1, 2=2}

    lRUCache.get(1);    // return 1

    lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}

    lRUCache.get(2);    // returns -1 (not found)

    lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}

    lRUCache.get(1);    // return -1 (not found)

    lRUCache.get(3);    // return 3

    lRUCache.get(4);    // return 4

 ```
  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> capacity <TeX>\leq</TeX> 3000

 >   	0 <TeX>\leq</TeX> key <TeX>\leq</TeX> 10^4

 >   	0 <TeX>\leq</TeX> value <TeX>\leq</TeX> 10^5

 >   	At most 2  10^5 calls will be made to get and put.


## Solution
We will use double linked List to solve this problem. We will store key and value in the double linked List and meanwhile we will use a hashmap to store the relationship between key and double linked list node. 

get can be easily implemented by using hashmap. Meanwhile, we will have to remove the related node and insert to the head of list. The time complexity is O(1).

put can be implemented by two cases.

If the key has been found in the hashmap, we need to find the node, update its value, remove it from the list, and insert it to the head.

If the key can not be found in the hashmap, we will create a new node and insert it to the head if the capacity has not been reached. If the capacity has been reached, we will have to remove the head node of list.


### Python
```python
class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None
        
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def addFirst(self, node):
        if self.size == 0:
            self.head = node
            self.tail = node
            self.size = 1
            return
        node.next = self.head
        self.head.prev = node
        self.head = self.head.prev
        self.size += 1
        return
    
    def removeLast(self):
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return
        node = self.tail
        self.tail = self.tail.prev
        node.prev = None
        self.tail.next = None
        self.size -= 1
        return

    def removeFirst(self):
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return
        node = self.head
        self.head = self.head.next
        node.next = None
        self.head.prev = None
        self.size -= 1
        return 
        
    def remove(self, node):
        if node == self.head:
            self.removeFirst()
            return
        if node == self.tail:
            self.removeLast()
            return
        preNode = node.prev
        nextNode = node.next
        preNode.next = nextNode
        nextNode.prev = preNode
        self.size -= 1
        return

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.cache = DoubleLinkedList()

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.cache.remove(self.hashmap[key])
            self.cache.addFirst(self.hashmap[key])
            return self.hashmap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.cache.remove(self.hashmap[key])
            self.hashmap[key].val = value
            self.cache.addFirst(self.hashmap[key])
            return
        if self.capacity == self.cache.size:
            removeKey = self.cache.tail.key
            self.cache.removeLast()
            del self.hashmap[removeKey]
        new_node = Node(key, value)
        self.hashmap[key] = new_node
        self.cache.addFirst(new_node)
        return
```

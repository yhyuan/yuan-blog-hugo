---
title: 138. Copy List with Random Pointer
date: '2021-09-13'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 0138. Copy List with Random Pointer
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={138}/>
 
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val

random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.

 > Example 1:

 > Input: head <TeX>=</TeX> [[7,null],[13,0],[11,4],[10,2],[1,0]]
 > Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

 > Example 2:

 > Input: head <TeX>=</TeX> [[1,1],[2,1]]
 > Output: [[1,1],[2,1]]

 > Example 3:

 > Input: head <TeX>=</TeX> [[3,null],[3,0],[3,null]]
 > Output: [[3,null],[3,0],[3,null]]

**Constraints:**

 > 0 <TeX>\leq</TeX> n <TeX>\leq</TeX> 1000

 > -104 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 104

Node.random is null or is pointing to some node in the linked list.


## Solution
Build a hashmap to record the relationship between node and index. 

Copy the original linked list and also put the nodes in an array. 

Copy random pointer. Find the index firstly, then use index to find the nodes in the array we found in 2.

### Python
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        p = head
        count = 0
        hashmap = {}
        while p is not None:
            hashmap[p] = count
            p = p.next
            count += 1
        
        dummy = Node(0)
        dummy_p = dummy
        nodes = []
        p = head
        while p is not None:
            newNode = Node(p.val)
            nodes.append(newNode)
            dummy_p.next = newNode
            dummy_p = dummy_p.next
            p = p.next
        
        p = head
        dummy_p = dummy.next
        while p is not None:
            if p.random is not None:
                dummy_p.random = nodes[hashmap[p.random]]
            p = p.next
            dummy_p = dummy_p.next
        return dummy.next

```

---
title: 1628. Design an Expression Tree With Evaluate Function
date: '2022-08-26'
tags: ['leetcode', 'python', 'hard']
draft: false
description: Solution for leetcode 1628. Design an Expression Tree With Evaluate Function
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1828}/>
 
Given the postfix tokens of an arithmetic expression, build and return the binary expression tree that represents this expression.

Postfix notation is a notation for writing arithmetic expressions in which the operands (numbers) appear before their operators. For example, the postfix tokens of the expression 4*(5-(7+2)) are represented in the array postfix <TeX>=</TeX> ["4","5","7","2","+","-","*"].

The class Node is an interface you should use to implement the binary expression tree. The returned tree will be tested using the evaluate function, which is supposed to evaluate the tree's value. You should not remove the Node class; however, you can modify it as you wish, and you can define other classes to implement it if needed.

A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (numbers), and internal nodes (nodes with two children) correspond to the operators '+' (addition), '-' (subtraction), '*' (multiplication), and '/' (division).

It's guaranteed that no subtree will yield a value that exceeds 109 in absolute value, and all the operations are valid (i.e., no division by zero).

Follow up: Could you design the expression tree such that it is more modular? For example, is your design able to support additional operators without making changes to your existing evaluate implementation?

 > Example 1:

 > Input: s <TeX>=</TeX> ["3","4","+","2","*","7","/"]
 > Output: 2
 > Explanation: this expression evaluates to the above binary tree with expression ((3+4)*2)/7) <TeX>=</TeX> 14/7 <TeX>=</TeX> 2.

 > Example 2:

 > Input: s <TeX>=</TeX> ["4","5","2","7","+","-","*"]
 > Output: -16
 > Explanation: this expression evaluates to the above binary tree with expression 4*(5-(2+7)) <TeX>=</TeX> 4*(-4) <TeX>=</TeX> -16.

**Constraints:**

 > 1 <TeX>\leq</TeX> s.length < 100

 > s.length is odd.

 > s consists of numbers and the characters '+', '-', '*', and '/'.

 > If s[i] is a number, its integer representation is no more than 105.

 > It is guaranteed that s is a valid expression.

 > The absolute value of the result and intermediate values will not exceed 109.

It is guaranteed that no expression will include division by zero.


## Solution
We can use a stack to analyze the postfix string and generate a tree and use recursion to evaluate. 
### Python
```python
import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    def __init__(self, char):
        self.char = char
        self.left = None
        self.right = None
        
    #@abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        if self.right is None and self.left is None:
            return int(self.char)
        left = self.left.evaluate()
        right = self.right.evaluate()
        if self.char == "+":
            return left + right
        elif self.char == "-":
            return left - right
        elif self.char == "*":
            return left * right
        elif self.char == "/":
            return left // right
        return None


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        n = len(postfix)
        for i in range(n):
            if postfix[i] in ["+", "-", "*", "/"]:
                node = Node(postfix[i])
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
            else:
                stack.append(Node(postfix[i]))
        return stack.pop()		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""

```

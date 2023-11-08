---
title: 1597. Build Binary Expression Tree From Infix Expression
date: '2022-07-27'
tags: ['leetcode', 'python']
draft: false
description: Solution for leetcode 1597. Build Binary Expression Tree From Infix Expression
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1597}/>
 
A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (numbers), and internal nodes (nodes with 2 children) correspond to the operators '+' (addition), '-' (subtraction), '*' (multiplication), and '/' (division).

For each internal node with operator o, the infix expression it represents is (A o B), where A is the expression the left subtree represents and B is the expression the right subtree represents.

You are given a string s, an infix expression containing operands, the operators described above, and parentheses '(' and ')'.

Return any valid binary expression tree, whose in-order traversal reproduces s after omitting the parenthesis from it.

Please note that order of operations applies in s. That is, expressions in parentheses are evaluated first, and multiplication and division happen before addition and subtraction.

Operands must also appear in the same order in both s and the in-order traversal of the tree.

 

Example 1:


Input: s = "3*4-2*5"

Output: [-,*,*,3,4,2,5]

Explanation: The tree above is the only valid tree whose inorder traversal produces s.

Example 2:


Input: s = "2-3/(5*2)+1"

Output: [+,-,1,2,/,null,null,null,null,3,*,null,null,5,2]

Explanation: The inorder traversal of the tree above is 2-3/5*2+1 which is the same as s without the parenthesis. The tree also produces the correct result and its operands are in the same order as they appear in s.

The tree below is also a valid binary expression tree with the same inorder traversal as s, but it not a valid answer because it does not evaluate to the same value.

The third tree below is also not valid. Although it produces the same result and is equivalent to the above trees, its inorder traversal does not produce s and its operands are not in the same order as s.

Example 3:

Input: s = "1+2+3+4+5"

Output: [+,+,5,+,4,null,null,+,3,null,null,1,2]

Explanation: The tree [+,+,5,+,+,null,null,1,2,3,4] is also one of many other valid trees.
 

**Constraints:**

1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 100

s consists of digits and the characters '+', '-', '*', and '/'.

Operands in s are exactly 1 digit.

It is guaranteed that s is a valid expression.


## Solution
The key is to use shunting yard algorithm to analyze the input string: an infix notation string and convert to a postfix notation string which can be easy converted to a tree. Let's take the following expression as an example.

(A+B)*C - (D+E)/(F+G) => (((A+B)*C) - ((D+E)/(F+G))) => AB+C*DE+FG+/-

We notice that the relative orders of A,B,C,D,E,F,G do not change when we convert the infix notation string to postfix notation string. The only thing we need to do is to adjust the positions of operators. 

A * B + C * D

i = 0, output A

i=1, push * to stack. stack = [*]

i=2, output B

i=3, compare '+' with stack top '*' since '*' is prior to '+', we need to pop and output '*' and push '+' stack = [+]

i=4 output C

i=5 compare '*' with the stack top '+' since '*' is prior to '+', we will to push '*' to stack. now stack = [+, *]

i=6 output D

now we reach the end of loop. We start to pop the operator out of stack. we will output * and +. So finally, we will get AB*CD*+

### Python
```python
# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expTree(self, s: str) -> 'Node':
        precede = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3}
        op_stack = []
        postfix = ""
        for i in range(len(s)):
            if s[i] >= '0' and s[i] <= '9':
                postfix += s[i]
            elif s[i] == '(':
                op_stack.append(s[i])
            elif s[i] in ['+', '-', '*', '/']:
                # key: pop until the top of stack is less than the current operator. 
                while len(op_stack) > 0 and precede[op_stack[-1]] >= precede[s[i]]:
                    op = op_stack.pop()
                    postfix += op                  
                op_stack.append(s[i])
            elif s[i] == ')':
                while op_stack[len(op_stack) - 1] != '(':
                    op = op_stack.pop()
                    postfix += op
                op_stack.pop()
        while len(op_stack) > 0:
            op = op_stack.pop()
            postfix += op

        node_stack = []
        for i in range(len(postfix)):
            if postfix[i] >= '0' and postfix[i] <= '9':
                node_stack.append(Node(postfix[i]))
            else:
                node = Node(postfix[i])
                rightNode = node_stack.pop()
                leftNode = node_stack.pop()
                node.left = leftNode
                node.right = rightNode
                node_stack.append(node)
        return node_stack.pop()
```

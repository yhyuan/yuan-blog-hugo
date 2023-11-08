---
title: 895. Maximum Frequency Stack
date: '2022-06-04'
tags: ['leetcode', 'python', 'hard']
draft: false
description: Solution for leetcode 0895. Maximum Frequency Stack
---

 
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.

void push(int val) pushes an integer val onto the top of the stack.

int pop() removes and returns the most frequent element in the stack.

If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

 > Example 1:

 > Input
 > ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
 > [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
 > Output

 > [null, null, null, null, null, null, null, 5, 7, 5, 4]

 > Explanation
```
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
```

**Constraints:**

 > 0 <TeX>\leq</TeX> val <TeX>\leq</TeX> 109

 > At most 2 * 104 calls will be made to push and pop.

 > It is guaranteed that there will be at least one element in the stack before calling pop.


## Solution
Design a list to store a series of stacks. If number i has a frequency of freq, then stackOfStack[freq], stackOfStack[freq - 1], stackOfStack[freq - 2] ... stackOfStack[1] all contains i. 

When a number is pushed, we calculate its frequency and check whether stackOfStack can contain it or not. If not, we will add empty list firstly. Then, the number is pushed to the stackOfStack[freq].

When a number is pop, we will check the last stack stackOfStack[maxFreq] and pop a value out. If the last stack is empty, we will remove it firstly until we reach a non-empty stack. The value pop out will be the result.

### Python
```python
class FreqStack:

    def __init__(self):
        self.stackOfStack = [[], []]
        self.freq = {}
        
    def push(self, val: int) -> None:
        if not val in self.freq:
            self.freq[val] = 1
            self.stackOfStack[1].append(val)
            return        
        self.freq[val] += 1
        for i in range(len(self.stackOfStack), self.freq[val] + 1):
            self.stackOfStack.append([])
        self.stackOfStack[self.freq[val]].append(val)        
        return

    def pop(self) -> int:
        while len(self.stackOfStack[-1]) == 0:
            self.stackOfStack.pop()
        ans = self.stackOfStack[-1].pop()
        self.freq[ans] -= 1
        if self.freq[ans] == 0:
            del self.freq[ans]
        return ans


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
```

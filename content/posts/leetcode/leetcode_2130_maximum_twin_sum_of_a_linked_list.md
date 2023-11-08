---
title: 2130. Maximum Twin Sum of a Linked List
date: '2022-09-09'
tags: ['leetcode', 'python']
draft: false
description: Solution for leetcode 2130. Maximum Twin Sum of a Linked List
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={2130}/>

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <TeX>\leq</TeX> i <TeX>\leq</TeX> (n / 2) - 1.

For example, if n <TeX>=</TeX> 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n <TeX>=</TeX> 4.

The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 > Example 1:

 > Input: head <TeX>=</TeX> [5,4,2,1]
 > Output: 6
 > Explanation:
 > Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum <TeX>=</TeX> 6.
 > There are no other nodes with twins in the linked list.
 > Thus, the maximum twin sum of the linked list is 6. 

 > Example 2:

 > Input: head <TeX>=</TeX> [4,2,2,3]
 > Output: 7
 > Explanation:
 > The nodes with twins present in this linked list are:
 > - Node 0 is the twin of node 3 having a twin sum of 4 + 3 <TeX>=</TeX> 7.
 > - Node 1 is the twin of node 2 having a twin sum of 2 + 2 <TeX>=</TeX> 4.
 > Thus, the maximum twin sum of the linked list is max(7, 4) <TeX>=</TeX> 7. 

 > Example 3:

 > Input: head <TeX>=</TeX> [1,100000]
 > Output: 100001
 > Explanation:
 > There is only one node with a twin in the linked list having twin sum of 1 + 100000 <TeX>=</TeX> 100001.

**Constraints:**

 > The number of nodes in the list is an even integer in the range [2, 105].

 > 1 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 105

## Solution
Store the data in an array and calculate with array. The time complexity is O(N) and the space complexity is O(N)
```python
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        p = head
        nums = []
        while p is not None:
            nums.append(p.val)
            p = p.next
        n = len(nums)
        ans = 0
        for i in range(n // 2):
            ans = max(ans, nums[i] + nums[n - 1 - i])
        return ans
```
If we need to limit the space complexity to O(1), we use the following steps to solve it. 

find the mid point and cut it from mid. Now we have to two linked lists with same size. 

We reverse the second one and traverse with the first one and calculate the sum. The max of the sum will be our results. 

We reverse the second one again and put it to the end of the first one

### Python
```python
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def calculateSize(head):
            p = head
            count = 0
            while p is not None:
                count += 1
                p = p.next
            return count
        def reverse(head):
            if head is None or head.next is None:
                return head
            p = head.next
            head.next = None
            while p is not None:
                q = p.next
                p.next = head
                head = p
                p = q
            return head
        count = calculateSize(head)
        last = head
        i = 0
        while last is not None:
            i += 1
            if i == count // 2:
                second = last.next
                last.next = None
                break
            last = last.next
        
        second = reverse(second)
        p1 = head
        p2 = second
        ans = 0
        while p1 is not None and p2 is not None:
            ans = max(ans, p1.val + p2.val)
            p1 = p1.next
            p2 = p2.next
        second = reverse(second)
        last.next = second

        return ans
```

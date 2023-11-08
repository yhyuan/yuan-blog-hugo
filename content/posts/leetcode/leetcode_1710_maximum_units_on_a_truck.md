---
title: 1710. Maximum Units on a Truck
date: '2022-08-24'
tags: ['leetcode', 'python', 'hard']
draft: false
description: Solution for leetcode 1710. Maximum Units on a Truck
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1710}/>
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] <TeX>=</TeX> [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.

numberOfUnitsPerBoxi is the number of units in each box of the type i.

You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

> Example 1:

> Input: boxTypes <TeX>=</TeX> [[1,3],[2,2],[3,1]], truckSize <TeX>=</TeX> 4
> Output: 8
> Explanation: There are:
> - 1 box of the first type that contains 3 units.
> - 2 boxes of the second type that contain 2 units each.
> - 3 boxes of the third type that contain 1 unit each.
> You can take all the boxes of the first and second types, and one box of the third type.
> The total number of units will be <TeX>=</TeX> (1 * 3) + (2 * 2) + (1 * 1) <TeX>=</TeX> 8.

> Example 2:

> Input: boxTypes <TeX>=</TeX> [[5,10],[2,5],[4,7],[3,9]], truckSize <TeX>=</TeX> 10
> Output: 91

**Constraints:**

> 1 <TeX>\leq</TeX> boxTypes.length <TeX>\leq</TeX> 1000

> 1 <TeX>\leq</TeX> numberOfBoxesi, numberOfUnitsPerBoxi <TeX>\leq</TeX> 1000

> 1 <TeX>\leq</TeX> truckSize <TeX>\leq</TeX> 106


## Solution
We sort the data with units per box and use greedy approach to pick the largest record until we filled our truck. 

### Python
```python
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # [5, 10], [3, 9], [2, 7] = 50 + 27 + 14 = 77 + 14 = 91
        records = []
        n = len(boxTypes)
        for i in range(n):
            records.append((boxTypes[i][1], boxTypes[i][0]))
        records.sort()
        records.reverse()
        #print(records)
        n = len(records)
        ans = 0
        for i in range(n):
            (unitsPerBox, boxes) = records[i]
            if truckSize > boxes:
                ans += boxes * unitsPerBox
                truckSize -= boxes
            else:
                ans += truckSize * unitsPerBox
                return ans
        return ans

```

# [Chocolate Distribution Problem](https://www.geeksforgeeks.org/chocolate-distribution-problem/)

## Problem Statement
Given an array `arr[]` of `N` integers where each value represents the number of chocolates in a packet.  
You are also given an integer `M`, the number of students.  
**Distribute M packets such that:**  
> Each student gets exactly one packet.
> The difference between the maximum and minimum chocolates among those `M` packets is minimized  

**Goal:** Minimize `max - min` among any `M` packets.  
**Example**
```python
Input: arr[] = {7, 3, 2, 4, 9, 12, 56}, m = 3 
Output: 2 
Explanation: If we distribute chocolate packets {3, 2, 4}, we will get the minimum difference, that is 2. 
```
```python
Input: arr[] = {7, 3, 2, 4, 9, 12, 56}, m = 5 
Output: 7
Explanation: If we distribute chocolate packets {3, 2, 4, 9, 7}, we will get the minimum difference, that is 9 – 2 = 7. 
```


## Possible Solutions – Brute Force to Optimized
## 1) Brute Force Approach – Generate All Combinations (Time: O(N^M) or worse, space: O(1))  
> Generate all combinations of size M from array arr[].  
> For each combination, calculate max - min.  
> Return the minimum difference.

```python
from itertools import combinations

def minDifferenceBruteForce(arr, m):
    if m == 0 or len(arr) < m: return 0
    
    min_diff = float('inf')
    for comb in combinations(arr, m):
        diff = max(comb) - min(comb)
        min_diff = min(min_diff, diff)
    return min_diff
```
## 2) Optimized - Sorting + Sliding Window (O(N log N) (due to sorting) time, O(1) space)
> **Idea Behind This Approach:**  
> आपल्याला `M` students ना chocolate packets द्यायचे आहेत.  
> पण असा सेट निवडायचा आहे की जिथे `max - min` म्हणजेच फरक सर्वात कमी होईल.  
> Sorting केल्यास, consecutive elements मध्येच हा फरक minimum मिळतो!  

**Step-by-step:**  
Sort the array.  
For every window of size `M`, calculate `arr[i + M - 1] - arr[i]`.  
Return the minimum difference found.  

```python
if m == 0 or len(arr) < m: return 0
arr.sort()
min_diff = float('inf')

for i in range(len(arr) - m + 1):
  diff = arr[i + m - 1] - arr[i]
  min_diff = min(min_diff, diff)
return min_diff
```



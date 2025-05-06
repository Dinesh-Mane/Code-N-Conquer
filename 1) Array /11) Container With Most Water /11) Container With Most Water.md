# [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/)

## Problem Statement
You are given an integer array height of length n.  
There are n vertical lines such that the two endpoints of the `i-th` line are at `(i, 0)` and `(i, height[i])`.  
Find two lines that, together with the x-axis, form a container such that the container contains the most water.  
Return the maximum amount of water a container can store.  

**Constraints:**  
Only one valid pair will exist.  
You can't use the same element twice (i.e., don’t reuse index).  
Return the indices, not the values.  

**Example**
```python
Input: prices = [7,1,5,3,6,4]
Output: 7

Explanation: 
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: Lines at index 1 and 8 (height=8 and 7) give area = 7 * (8 - 1) = 49
```
```python
Input: height = [1,1]
Output: 1
```
## Possible Solutions – Brute Force to Optimized
## 1) Brute Force Approach – Try all combinations ( Time: O(2^n) — very slow, Space: O(n))  
Idea: Try all possible buy/sell combinations recursively.  

```python
def helper(i, holding):
  if i == len(prices): return 0
  profit = helper(i + 1, holding)  # Choice 1: Do nothing
  if holding: profit = max(profit, prices[i] + helper(i + 1, False))  # Choice 2: Sell today
  else: profit = max(profit, -prices[i] + helper(i + 1, True))  # Choice 3: Buy today
  return profit
return helper(0, False)
```
## 2) Peak-Valley Approach (O(n) time, O(1) space)  
**Logic:**  
Find every increasing segment: buy at valley, sell at peak.  
Add profit of each such transaction.  
```python
i = 0
profit = 0
while i < len(prices) - 1:
  while i < len(prices)-1 and prices[i] >= prices[i+1]: i += 1
  buy = prices[i]
  while i < len(prices)-1 and prices[i] <= prices[i+1]: i += 1
  sell = prices[i]
  profit += sell - buy
return profit
```

## 3) Optimized - Greedy Solution (O(n) time, O(1) space)  
**Idea:** जेव्हा price increase होतं (i.e. prices[i+1] > prices[i]) तेव्हा आपण profit कमवू शकतो. म्हणून जिथे जिथे increase आहे तिथे तितका profit add करा.  
> We don't need to track exact buy/sell days. Just add all upward differences

```python
profit = 0
for i in range(1, len(prices)):
  if prices[i] > prices[i - 1]: profit += prices[i] - prices[i - 1]
return profit
```


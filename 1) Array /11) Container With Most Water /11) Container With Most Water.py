class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(1, len(height)):
                curr_area = min(height[i],height[j]) * (j-i)
                max_area = max(max_area, curr_area)
        return max_area

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        max_area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                max_area = max(max_area, min(height[i], height[j]) * (j-i))
        '''
        max_area = 0
        i, j = 0, len(height) - 1
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area

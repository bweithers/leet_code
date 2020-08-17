class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left_bound , right_bound = 0, len(height) - 1
        while left_bound < right_bound:
            area = max(area, min(height[left_bound],height[right_bound]) * (right_bound - left_bound))
            if height[left_bound] < height[right_bound]:
                left_bound += 1
            else:
                right_bound -= 1
        return area
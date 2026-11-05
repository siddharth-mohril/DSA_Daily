class Solution:
    def maxArea(self, height: list[int]) -> int:
        maximum = 0
        L = 0
        R = len(height) - 1
        while L < R:
            area = min(height[L],height[R]) * (R-L)
            if area > maximum:
                maximum = area 
            if height [L] > height[R]:
                R -= 1
            else :
                L += 1

        return maximum 

        
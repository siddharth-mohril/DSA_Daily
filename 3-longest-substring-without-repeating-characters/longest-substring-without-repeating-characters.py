class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        L = 0
        check = set()

        for R in range(len(s)):
            while s[R] in check:
                check.remove(s[L])
                L += 1
            check.add(s[R])
            max_length = max(max_length, R-L+1)
        return max_length
        
        
            



        
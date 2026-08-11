class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        freq = {}
        max_freq = 0
        max_length = 0


        for R in range(len(s)):
            freq[s[R]] = freq.get(s[R],0) + 1
            max_freq = max(max_freq, freq[s[R]])
            while R-L+1 - max_freq > k:
                freq[s[L]] -= 1
                L += 1
            max_length = max(max_length, R-L+1)
                
        return max_length
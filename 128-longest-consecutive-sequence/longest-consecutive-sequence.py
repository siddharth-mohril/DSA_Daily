class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hashset = set(nums)
        
        longest = 0
        for i in hashset :
            
            if i - 1 not in hashset:
                length = 1
                current = i

                while current + 1 in hashset:
                    length += 1
                    current += 1 
                    
                if length > longest:
                    longest = length

        return longest


        
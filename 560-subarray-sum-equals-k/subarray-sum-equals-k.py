class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        
        hashmap = {0:1}
        prefix = 0
        count = 0
        for i in range(len(nums)):
            prefix += nums[i]
            count += hashmap.get(prefix - k, 0)
            hashmap[prefix] = hashmap.get(prefix,0) + 1
        return count


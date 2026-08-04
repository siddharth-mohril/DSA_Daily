class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            # hashmap[nums[i]] = hashmap.get(nums[i],0) + 1
            complement = target - nums[i]
            if complement in hashmap:
                return [i,hashmap[complement]]
            hashmap[nums[i]] = i



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        count = 0
        res = 0
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i],0) + 1
        for number,frequency in hashmap.items():
            if count < frequency :
                count = frequency
                res = number
        return res

        
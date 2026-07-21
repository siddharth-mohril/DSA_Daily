class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            current_number = nums[i]
            compliment = target - nums[i] 

            if compliment in hashmap:
                return(hashmap[compliment], i)
            hashmap[current_number] = i


        
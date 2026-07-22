class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i],0) + 1

        sorted_keys = sorted(hashmap, key=hashmap.get, reverse=True)

        return sorted_keys[:k]


        
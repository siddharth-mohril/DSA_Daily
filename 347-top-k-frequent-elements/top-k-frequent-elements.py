class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1
        
        pairs = sorted(hashmap.items(), key = lambda x: x[1], reverse = True) 

        result = []
        for i in range(0,k):
            result.append(pairs[i][0])
        return result

            
        

        
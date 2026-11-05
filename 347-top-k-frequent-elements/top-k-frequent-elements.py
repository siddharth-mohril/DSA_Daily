class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}
        answer = []

        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1
        
        final = sorted(hashmap.items(), key = lambda x : x[1], reverse = True )

        for i in range(0,k):
            answer.append(final[i][0])

        return answer

        
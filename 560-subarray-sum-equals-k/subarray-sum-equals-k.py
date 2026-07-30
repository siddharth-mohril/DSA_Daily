class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_map = {0: 1} 

        for num in nums:
            current_sum += num
            

            diff = current_sum - k
            

            count += prefix_map.get(diff, 0)
            

            prefix_map[current_sum] = 1 + prefix_map.get(current_sum, 0)
            
        return count
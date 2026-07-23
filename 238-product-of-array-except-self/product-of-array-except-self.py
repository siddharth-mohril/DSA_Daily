class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        print(res)
        
        # Pass 1: Calculate prefix products (left-to-right)
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

            
        # Pass 2: Multiply by suffix products (right-to-left)
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix  # Multiply current result by the postfix product
            postfix *= nums[i] # Update postfix product for the next element
            
        return res
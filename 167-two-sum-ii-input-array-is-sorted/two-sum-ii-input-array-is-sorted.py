class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        L = 0
        R = len(numbers) - 1
        while L < R:
            summ = numbers[L] + numbers[R]
            if summ < target:
                L += 1
            elif summ > target:
                R -= 1
            elif summ == target:
                return [L+1,R+1]
        return False


            
        
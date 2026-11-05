class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        listf = []
        numss = sorted(nums)

        for i in range(0,len(nums)):

            if i > 0 and numss[i] == numss[i-1]:
                continue

            L = i + 1
            R = len(nums) - 1
            

            while L < R  :
                summ = numss[L] + numss[R]
                target = 0 - (numss[i])

                if summ < target :
                    L += 1
                elif summ > target:
                    R -= 1

                elif summ == target:
                    listf.append([numss[i],numss[L],numss[R]])
                    L += 1
                    R -= 1

                    while L < R and numss[L] == numss[L - 1]:
                        L += 1
                    while L < R and numss[R] == numss[R + 1]:
                        R -= 1

        return listf


        
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        numss = sorted(nums)
        final = []
        for i in range(len(numss)):
            if i > 0 and numss[i] == numss[i-1]:
                continue

            L = i+1
            R = (len(numss)-1)
            
            while L < R:

                sum = numss[i] + numss[L] + numss[R]

                if sum > 0 :
                    R -= 1
                elif sum < 0:
                    L += 1
                else:
                    final.append([numss[i],numss[L],numss[R]])
                    L += 1
                    R -= 1
                    while L < R and numss[L] == numss[L - 1]:
                        L += 1


        return final
                    

                
        
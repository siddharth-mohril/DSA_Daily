class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        cs1 = {} #counts1 count hashmap for s1
        for i in range(len(s1)):
            cs1[s1[i]] = cs1.get(s1[i], 0) + 1
        
        L = 0
        cs2 = {}
        for R in range(len(s2)):

            cs2[s2[R]] = cs2.get(s2[R],0) + 1

            

            while R-L+1 > len(s1):
                cs2[s2[L]] -= 1
                if cs2[s2[L]] == 0:
                    cs2.pop(s2[L])
                L += 1

            if cs1 == cs2:
                return True
            

        return False

            


        
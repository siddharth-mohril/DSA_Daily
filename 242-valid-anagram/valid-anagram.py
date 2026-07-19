class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = {}
        countT = {} 
        
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            

            countS[char_s] = countS.get(char_s, 0) + 1
            countT[char_t] = countT.get(char_t, 0) + 1
            

        if countS == countT : 
            return True
        else:
            return False
            

        return countS == countT
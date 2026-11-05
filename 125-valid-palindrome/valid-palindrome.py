class Solution:
    def isPalindrome(self, s: str) -> bool:
        stringfinal = ""
        
        for i in s:
            if i.isalnum() :
                stringfinal += i.lower()

        L = 0
        R = len(stringfinal) - 1 

        while L < R:
            if stringfinal[L] == stringfinal[R] :
                L += 1
                R -= 1
            else:
                return False

        return True
        



        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = "".join(char.lower() for char in s if char.isalnum())
        R = len(clean_str) - 1 
        L = 0
        list1= list(clean_str)
        while R > L:
            if list1[R] == list1[L]:
                R -= 1
                L += 1
            else:
                return False
        return True

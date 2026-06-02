class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        shortest = min(strs, key=len)
        string = ""
        match = True
        if len(shortest) == 0:
            return string

        for i in range(len(shortest)):
            for word in strs:
                if word[i] != strs[0][i]:
                    match = False
                    break
            if match :
                string += strs[0][i]
        return string

        
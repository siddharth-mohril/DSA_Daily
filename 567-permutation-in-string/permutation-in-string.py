class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        hashmap1 = {}
        hashmap2 = {}

        L = 0

        if len(s1)> len(s2):
            return False

        for R in range(len(s1)):
            hashmap1[s1[R]] = hashmap1.get(s1[R],0) + 1
            hashmap2[s2[R]] = hashmap2.get(s2[R],0) + 1

        if hashmap1 == hashmap2:
            return True
        
        for R in range(len(s1),len(s2)):
            hashmap2[s2[R]] = hashmap2.get(s2[R],0) + 1

            hashmap2[s2[L]] -= 1
            if hashmap2[s2[L]] == 0 :
                del hashmap2[s2[L]]
            L += 1

            if hashmap1 == hashmap2 :
                return True

        return False


        # for i in range(len(s1)):
        #     hashmap1[s1[i]]= hashmap1.get(s1[i],0)+1

        # for i in range(len(s2)):
        #     hashmap2[s2[i]]= hashmap2.get(s2[i],0)+1

        # for i,r in hashmap2.items():
        #     if i in hashmap1.keys():
        #         print(i,r)



                
        
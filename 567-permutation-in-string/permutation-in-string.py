class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        # 1. Populate initial frequencies for first window
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1

        # 2. Count initial matches out of 26
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1

        # 3. Slide window across s2
        L = 0
        for R in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # --- Process Right Character (Adding s2[R]) ---
            r_idx = ord(s2[R]) - ord("a")
            if s1_count[r_idx] == s2_count[r_idx]:
                matches -= 1  # Existing match is about to break
            s2_count[r_idx] += 1
            if s1_count[r_idx] == s2_count[r_idx]:
                matches += 1  # New match formed

            # --- Process Left Character (Removing s2[L]) ---
            l_idx = ord(s2[L]) - ord("a")
            if s1_count[l_idx] == s2_count[l_idx]:
                matches -= 1  # Existing match is about to break
            s2_count[l_idx] -= 1
            if s1_count[l_idx] == s2_count[l_idx]:
                matches += 1  # New match formed

            L += 1

        return matches == 26

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        if k > len(s):
            return []

        need = [0] * 26  # letter counts of p
        window = [0] * 26  # letter counts of the current window
        for c in p:
            need[ord(c) - ord('a')] += 1

        res = []
        for i, c in enumerate(s):
            window[ord(c) - ord('a')] += 1  # new letter enters on the right
            if i >= k:
                window[ord(s[i - k]) - ord('a')] -= 1 # old letter leaves on the left
            if window == need:
                res.append(i - k + 1)  # window ends at i, so it starts at i - k + 1
        return res

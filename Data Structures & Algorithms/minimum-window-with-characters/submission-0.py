class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}

        # count characters in t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            # check if this char satisfies requirement
            if c in countT and window[c] == countT[c]:
                have += 1

            # shrink window
            while have == need:
                # update result
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                # remove left char
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1

                left += 1   # VERY IMPORTANT

        left, right = res
        return s[left:right+1] if resLen != float("inf") else ""
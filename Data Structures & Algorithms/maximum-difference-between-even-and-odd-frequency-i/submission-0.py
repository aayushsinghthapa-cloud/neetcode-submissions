class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for k in s:
            freq[k] = freq.get(k, 0) + 1
        
        even = []
        odd = []

        for val in freq.values():
            if val % 2 == 0:
                even.append(val)
            else:
                odd.append(val)
            
        return max(odd) - min(even)
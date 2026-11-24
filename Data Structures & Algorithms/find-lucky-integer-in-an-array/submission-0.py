class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        lucky = []

        for k, v in freq.items():
            if k == v:
                lucky.append(k)

        if lucky:
            return max(lucky)
        else:
            return -1
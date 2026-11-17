class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        freq = [0] * (n*n + 1)

        for row in grid:
            for num in row:
                freq[num] += 1

        ans = [0,0]

        for i in range (1, n*n + 1):
            if freq[i] == 2:
                ans[0] = i
            elif freq[i] == 0:
                ans[1] = i
        return ans
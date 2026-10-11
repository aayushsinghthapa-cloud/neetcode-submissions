class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for r in range(numRows):
            row = [1] * (r + 1)
            for j in range(1,r):
                row [j] = res[r - 1] [j - 1] + res[r - 1] [j]
            res.append(row)
        return res
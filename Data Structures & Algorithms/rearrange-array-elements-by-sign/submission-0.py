class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)

        res = []
        for k in range(len(nums) // 2):
            res.append(pos[k])     # kth positive
            res.append(neg[k])     # paired with the kth negative
        return res
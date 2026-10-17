class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        pow2 = [1] * n

        for k in range(1,n):
            pow2[k] = pow2[k - 1] * 2 % MOD

        l, r = 0, n - 1
        count = 0
        while l <= r:
            if nums[l] + nums[r] <= target:
                count = (count + pow2[r - l]) % MOD
                l += 1
            else:
                r -= 1
        return count


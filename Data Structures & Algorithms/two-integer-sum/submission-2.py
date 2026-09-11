class Solution:
    def twoSum(self, nums, target):
        complement = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in complement:
                return [complement[needed], i]
            else:
                complement[nums[i]] = i
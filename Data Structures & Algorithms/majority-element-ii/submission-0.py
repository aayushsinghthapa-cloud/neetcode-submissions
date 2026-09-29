class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        req = len(nums) // 3 #required frequency

        # Getting the frequency of all the elements in the array
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        return [key for key, value in freq.items() if value > req]
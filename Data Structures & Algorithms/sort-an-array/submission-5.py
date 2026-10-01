class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort_inplace(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                left, right = arr[:mid], arr[mid:]
                merge_sort_inplace(left)
                merge_sort_inplace(right)

                i = j = k = 0
                while i < len(left) and j < len(right):
                    if left[i] <= right[j]:
                        arr[k] = left[i]; i += 1
                    else:
                        arr[k] = right[j]; j += 1
                    k += 1
                while i < len(left):
                    arr[k] = left[i]; i += 1; k += 1
                while j < len(right):
                    arr[k] = right[j]; j += 1; k += 1

        merge_sort_inplace(nums)
        return nums
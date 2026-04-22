class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse_range(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        n = len(nums)
        k = k%n
        reverse_range(nums, 0, n-1)
        reverse_range(nums, 0, k-1)
        reverse_range(nums, k, n-1)

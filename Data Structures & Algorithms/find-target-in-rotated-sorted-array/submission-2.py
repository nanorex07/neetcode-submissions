class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 1:
            return 0 if nums[0]==target else -1
        if len(nums) == 2:
            return 0 if nums[0]==target else (1 if nums[1]==target else -1)
        

        l, h = 0, len(nums)-1

        while h > l:
            mid = (h+l)//2
            
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                h = mid

        peak = l
        l = 0
        h = peak-1
        while h >= l:
            mid = (h+l)//2
            if nums[mid]==target:
                return mid
            if nums[mid] > target:
                h = mid-1
            else:
                l = mid+1
        
        l = peak
        h = len(nums)-1
        while h >= l:
            mid = (h+l)//2
            if nums[mid]==target:
                return mid
            if nums[mid] > target:
                h = mid-1
            else:
                l = mid+1
        

        return -1



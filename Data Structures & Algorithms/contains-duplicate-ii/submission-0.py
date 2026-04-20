from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_table = defaultdict(lambda: False)

        for i in range(min(len(nums), k+1)):
            if hash_table[nums[i]]:
                return True
            hash_table[nums[i]] = True
        
        for i in range(k+1, len(nums)):
            hash_table[nums[i-k-1]] = False
            if hash_table[nums[i]]:
                return True
            hash_table[nums[i]] = True
        
        return False


        
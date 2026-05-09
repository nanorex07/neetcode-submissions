class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        item_a = -1
        item_ac = 0
        item_b = -1
        item_bc = 0


        for i in range(0, len(nums)):
            if nums[i] == item_a:
                item_ac+=1
                continue
            
            elif nums[i] == item_b:
                item_bc+=1
            
            elif item_ac == 0:
                item_a = nums[i]
                item_ac += 1

            elif item_bc == 0:
                item_b = nums[i]
                item_bc += 1
            else:
                item_ac -= 1
                item_bc -= 1

        item_ac, item_bc = 0, 0
        for num in nums:
            item_ac += (num==item_a)
            item_bc += (num==item_b)
        
        res = []
        if item_ac > len(nums)//3:
            res.append(item_a)
        if item_bc > len(nums)//3:
            res.append(item_b)

        return res
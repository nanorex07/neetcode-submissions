class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost_a, cost_b, cost_c = 0, 0, 0
        for i in range(2, len(cost)+1):
            cost_c = min(cost_a+cost[i-1], cost_b+cost[i-2])
            cost_b, cost_a = cost_a, cost_c
            print(cost_b)
        return cost_c
 

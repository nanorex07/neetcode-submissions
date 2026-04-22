class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()

        i, j = 0, len(people)-1
        take = 0
        while i < j:
            if people[i]+people[j] <= limit:
                take+=1
                i+=1
                j-=1
            else:
                take+=1
                j-=1

        if i == j:
            take+=1
        return take


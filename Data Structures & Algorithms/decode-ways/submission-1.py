class Solution:
    def numDecodings(self, s: str) -> int:
        
        sol = [0]*(len(s)+1)
        if int(s[0]) > 0:
            sol[1] = 1
        else:
            return 0
        sol[0] = 1
        
        for i in range(1, len(s)):
            if s[i] == '0' and s[i-1] == '0':
                return 0

            if s[i-1] == '0':
                sol[i+1] = sol[i]
                continue
                
            incPrev = s[i-1]+s[i]
            if s[i] == '0':
                if int(incPrev) <= 26:
                    sol[i+1] = sol[i-1]
                else:
                    return 0
                continue
            
            sol[i+1] = sol[i]
            
            if int(incPrev) <= 26:
                sol[i+1] += sol[i-1]

            print(sol)
        return sol[len(s)]

        # 3 0 1


            
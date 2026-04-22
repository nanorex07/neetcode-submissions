class Solution:
    def minWindow(self, s: str, t: str) -> str:


        hasht = [0]*128
        hashs = [0]*128
        for ch in t:
            hasht[ord(ch)]+=1

        i = 0
        minl = len(s)
        ans = ""

        for j in range(len(s)):
            hashs[ord(s[j])] += 1
            while all(hashs[x]>=hasht[x] for x in range(128)) and i <= j:
                if j-i+1 <= minl:
                    minl = j-i+1
                    ans = s[i:j+1]
                hashs[ord(s[i])]-=1
                i+=1

        return ans
        
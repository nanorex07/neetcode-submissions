from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = defaultdict(int)
        i, ans = 0, 0
        for j in range(len(s)):
            freq[s[j]]+=1
            while freq and sum(freq.values()) - max(freq.values()) > k and i < j:
                freq[s[i]] -= 1
                i+=1
            ans = max(ans, j-i+1)
        return ans

        # i = 0, j = 3
        # A: 3
        # B: 1
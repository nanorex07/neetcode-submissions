class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = set()
        ans = 0
        i = 0
        for j in range(len(s)):
            if s[j] not in store:
                store.add(s[j])
                ans = max(j-i+1, ans)
                continue

            while s[i] != s[j] and i < j:
                store.remove(s[i])
                i+=1
            store.remove(s[i])
            i+=1
            store.add(s[j])
            ans = max(j-i+1, ans)
        return ans;

        #  bca
        # abcabcbb

class Solution:
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList = set(wordList)

        if endWord not in wordList:
            return 0

        q = deque([beginWord])
        ans = 1

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                print(node)
                for i in range(len(node)):
                    for ch in self.ALPHABET:
                        new_n = f"{node[:i]}{ch}{node[i+1:]}"
                        if new_n == endWord:
                            return ans+1
                        if new_n in wordList:
                            q.append(new_n)
                            wordList.remove(new_n)
            ans+=1
        
        return 0

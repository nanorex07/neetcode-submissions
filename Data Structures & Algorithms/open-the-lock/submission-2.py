class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        

        deadends = set(deadends)
        
        if '0000' in deadends:
            return -1
        vis = set()
        q = deque([([0,0,0,0], 0)])
        ans = float("inf")


        while q:
            cur, dist = q.popleft()
            for ind in range(4):
                incs = [v for v in cur]
                incs[ind] = (incs[ind]+1)%10
                ins = ''.join(map(str, incs))
                if ins == target:
                    ans = min(ans, dist+1)
                elif ins not in vis and ins not in deadends:
                    q.append((incs, dist+1))
                    vis.add(ins)

                dncs = [v for v in cur]
                dncs[ind] = (dncs[ind]-1)%10
                dns = ''.join(map(str, dncs))
                if dns == target:
                    ans = min(ans, dist+1)
                elif dns not in vis and dns not in deadends:
                    q.append((dncs, dist+1))
                    vis.add(dns)
        
        return ans if ans < float("inf") else -1
                
                
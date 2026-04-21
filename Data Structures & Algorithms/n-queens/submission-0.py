class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        sol: List[List[str]] = []
        posDia, negDia, colset = set(), set(), set()
        running = [["."]*n for _ in range(n)]

        def solve(row: int):
            if row == n:
                sol.append([''.join(i) for i in running])
                return

            for col in range(n):
                if col in colset or row+col in posDia or row-col in negDia:
                    continue

                running[row][col] = 'Q'
                colset.add(col)
                posDia.add(row+col)
                negDia.add(row-col)

                solve(row+1)

                running[row][col] = '.'
                colset.remove(col)
                posDia.remove(row+col)
                negDia.remove(row-col)
        
        solve(0)
        return sol
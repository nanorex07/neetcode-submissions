class DSU:
    def __init__(self, n: int):
        self.parent = [i for i in range(n+1)]
        self.comp_size = [1]*(n+1)

    def find(self, i: int) -> int:
        curr = i
        while self.parent[curr] != curr:
            curr = self.parent[curr]
        return curr

    def getSize(self, i: int) -> int:
        return self.comp_size[i]
    
    def unite(self, i: int, j: int) -> bool:
        parent_i = self.find(i)
        parent_j = self.find(j)
        if parent_i == parent_j:
            return False
        if self.getSize(parent_i) >= self.getSize(parent_j):
            self.parent[parent_j] = parent_i
            self.comp_size[parent_i] += self.comp_size[parent_j]
        else:
            self.parent[parent_i] = parent_j
            self.comp_size[parent_j] += self.comp_size[parent_i]
        
        return True

    def log(self):
        print("Parents", self.parent)
        print("Sizes", self.comp_size)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))

        for u,v in edges:
            if dsu.unite(u, v):
                continue
            return [u, v]
        return []
        




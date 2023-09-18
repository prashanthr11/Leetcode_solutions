class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ln = list(range(len(mat)))
        return sorted(ln, key=lambda x: sum(mat[x]))[:k]
    
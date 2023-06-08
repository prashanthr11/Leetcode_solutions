class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return self.naive(grid)
    
    
    def naive(self, grid):
        return sum([1 if j <= -1 else 0 for i in grid for j in i])
    
    
    def optimise(self, grid):
        n, m = len(grid), len(grid[0])
        cnt = 0
        
        def get_idx(lst, key=-1):
            low, high = 0, len(lst) - 1
            
            while low < high:
                mid = (low + high) // 2
                
                if lst[mid] > key:
                    low = mid + 1
                elif lst[mid] < key:
                    high = mid
                    
        
        for i in range(n):
            idx = get_idx(grid[i])
            print(idx)
            cnt += (m - idx)
            
        return cnt
    
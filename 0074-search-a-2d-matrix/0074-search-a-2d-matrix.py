class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        
        low, high = 0, (n * m) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            r, c = mid // m, mid % m
            
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False
    
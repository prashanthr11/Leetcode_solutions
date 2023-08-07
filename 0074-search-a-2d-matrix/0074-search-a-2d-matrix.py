class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.approach2(matrix, target)
    
    def approach1(self, matrix, target):
        '''
        Time Complexity: O(log(m * n))
        Space Complexity: O(1)
        '''
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
    
    
    def approach2(self, matrix, target):
        '''
        Time Complexity: O(log(m) + log(n))
        Space Complexity: O(1)
        '''
        n, m = len(matrix), len(matrix[0])
        
        low, high = 0, n - 1
        
        while low < high:
            mid = low + (high - low) // 2
            
            if matrix[mid][-1] < target:
                low = mid + 1
            else:
                high = mid
        
        low2, high2 = 0, m - 1
        while low2 <= high2:
            mid = low2 + (high2 - low2) // 2
            
            if matrix[low][mid] == target:
                return True
            elif matrix[low][mid] < target:
                low2 = mid + 1
            else:
                high2 = mid - 1
                
        return False
    
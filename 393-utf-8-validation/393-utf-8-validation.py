class Solution:
    def figure_out_byte(self, n):
        '''
        Time Complexity: O(Log N)
        Space Complexity: O(1)
        '''
        i = 7
        while i:
            if n & (1 << i):
                i -= 1
            else:
                break
                
        if i == 7:
            return 1
        
        if i <= 5:
            return 7 - i
        
        return 0
            
        
    def validUtf8(self, data: List[int]) -> bool:
        '''
        Time Complexity: O(N*Log N)
        Space Complexity: O(1)
        '''
        i, ln = 0, len(data)
        
        while i < ln:
            bytes = self.figure_out_byte(data[i])
            
            if 1 <= bytes <= 4 and self.valid_bytes(bytes, data[i + 1: i + bytes]):
                i += bytes
            else:
                return False
            
        return True
    
    def valid_bytes(self, bytes, l):
        '''
        Time Complexity: O(1)
        Space Complexity: O(1)
        '''
        if bytes == 1:
            return True
        
        if not len(l):
            return False
        
        for i in l:
            
            if i & (1 << 7) and i & (1 << 6) == 0:
                continue
            else:
                return False
            
        return True
    
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        mask = 0
        maxi = 0
        
        for i in range(31, -1, -1):
            mask = mask | (1 << i)
            st = set()
            for j in nums:
                st.add(j & mask)
                
            tmp = maxi | (1 << i)
            
            for i in st:
                if i ^ tmp in st:
                    maxi = tmp
                    break
                    
            
        return maxi
    
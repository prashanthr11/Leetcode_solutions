class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:    
        '''
        Time Complexity: O(N*M)
        Space Complexity: O(1)
        '''
        
        max_wealth = 0
        
        for account in accounts:
            col_sum = sum(account)
            max_wealth = max_wealth if max_wealth > col_sum else col_sum
                
        return max_wealth
    
    
        '''
        # One liner
        
        Time Complexity: O(N*M)
        Space Complexity: O(N)
        '''
        
        return max([sum(account) for account in accounts])
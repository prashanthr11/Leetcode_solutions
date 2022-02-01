class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        mini = prices[0]
        maxi = 0
        
        for i in prices:
            if i < mini:
                mini = i
                
            res = i - mini
            if maxi < res:
                maxi = res
            
        return maxi
    
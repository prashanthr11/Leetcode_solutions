class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        '''
        Time Complexity: O(N logN)
        Space Complexity: O(1)
        '''
        costs.sort()
        cnt = 0
        
        for cost in costs:
            if cost <= coins:
                coins -= cost
                cnt += 1
            else:
                break
                
        return cnt
    
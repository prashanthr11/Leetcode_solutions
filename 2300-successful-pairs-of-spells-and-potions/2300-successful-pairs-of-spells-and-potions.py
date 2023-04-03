class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        '''
        Time Complexity: O(N logN)
        Space Complexity: O(1)
        '''
        potions.sort()
        ln = len(spells)
        ln_potions = len(potions)
        ret = [0] * ln
        
        for i in range(ln):
            ret[i] = ln_potions - self.find_ele(potions, math.ceil(success/spells[i]))
            
        return ret
    
    def find_ele(self, lst, val):
        low, high = 0, len(lst)
        
        while low < high:
            mid = (low + high) // 2
            
            if lst[mid] < val:
                low = mid + 1
            else:
                high = mid
                
        return low

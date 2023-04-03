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
            ret[i] = ln_potions - bisect.bisect_left(potions, math.ceil(success/spells[i]))
            
        return ret
    
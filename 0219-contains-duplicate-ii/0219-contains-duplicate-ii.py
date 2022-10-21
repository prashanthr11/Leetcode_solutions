class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        d = {}
        
        for i, a in enumerate(nums):
            if a in d:
                if i - d[a] <= k:
                    return True
                
            d[a] = i
            
        return False
    
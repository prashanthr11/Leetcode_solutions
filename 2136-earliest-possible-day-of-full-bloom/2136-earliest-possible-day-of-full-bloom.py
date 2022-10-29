class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        '''
        Time Complexity: O(N logN)
        Space Complexity: O(N)
        '''
        curr = maxi = 0
        lst = range(len(plantTime))
        lst = sorted(lst, key=lambda x: -growTime[x])
        
        for i in lst:
            curr += plantTime[i]
            maxi = max(maxi, curr + growTime[i])
            
        return maxi
    
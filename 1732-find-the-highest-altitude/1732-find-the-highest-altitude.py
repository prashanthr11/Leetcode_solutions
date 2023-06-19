class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        i, n = 1, len(gain)
        sumi = gain[0]
        maxi = max(0, sumi)
        
        while i < n:
            sumi += gain[i]
            maxi = max(maxi, sumi)
            i += 1
            
        return maxi
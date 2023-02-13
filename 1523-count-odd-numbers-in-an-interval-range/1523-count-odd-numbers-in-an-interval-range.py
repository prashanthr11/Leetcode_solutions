class Solution:
    def countOdds(self, low: int, high: int) -> int:
        end = high // 2
        end += high & 1
        
        # end = math.ceil(high / 2)
        
        start = low // 2
        
        return end - start
    
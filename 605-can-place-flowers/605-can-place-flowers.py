class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i, ln, cnt = 0, len(flowerbed), 0
        
        while i < ln:
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == ln - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                cnt += 1
                i += 1
                
            if cnt >= n:
                return True
            
            i += 1
            
        return False
    
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        '''
        Time complexity: O(N)
        Space complexity: O(N)
        '''
        lst = [0] + flowerbed + [0]
        cnt = 0
        
        for i in range(1, len(lst) - 1):
            if lst[i] == lst[i - 1] == lst[i + 1] == 0:
                lst[i] = 1
                cnt += 1
                
        return cnt >= n
    
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        cnt = 0
        
        while target != 1:
            if maxDoubles == 0:
                cnt += target - 1
                break
                
            if target & 1 == 0:
                target >>= 1
                maxDoubles -= 1
            else:
                target -= 1
                
            cnt += 1
            
        return cnt
    
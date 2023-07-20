class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        stk = []
        
        for i in asteroids:
            if i >= 0:
                stk.append(i)
                continue
                
            while stk and stk[-1] < abs(i):
                stk.pop()

            flag = False
            if stk and stk[-1] == abs(i):
                flag = True
                stk.pop()
                
            if len(stk) == 0 and flag == False:
                res.append(i)
                
        return res + stk
    
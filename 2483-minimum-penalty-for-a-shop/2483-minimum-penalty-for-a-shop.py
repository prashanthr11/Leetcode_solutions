class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        cnt = customers.count('Y')
        mini = cnt
        ret = 0
        
        for i in range(n):
            if customers[i] == "Y":
                cnt -= 1
            else:
                cnt += 1
                
            if mini > cnt:
                mini = cnt
                ret = i + 1
        
        return ret

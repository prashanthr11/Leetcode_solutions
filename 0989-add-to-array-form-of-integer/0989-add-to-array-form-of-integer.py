class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return self.optimise(num, k)
        
    def naive(self, num, k):
        ln = len(num)
        ret = 0
        for i in range(ln):
            ret += num[i] * 10**(ln - i - 1)
            
        ret += k
        ans = deque()
        
        while ret:
            ans.appendleft(ret % 10)
            ret //= 10
            
        return ans
    
    def optimise(self, num, k):
        def get_digits_count(n):
            cnt = 0
            while n:
                cnt += 1
                n //= 10
                
            return cnt
        
        ln = len(num)
        carry = 0
        maxi = max(ln, get_digits_count(k))
        ret = [0] * (maxi + 1)
        pos = maxi
        ln -= 1
        
        while ln >= 0 and k:
            sumi = num[ln] + (k % 10) + carry
            ret[pos] = sumi % 10
            carry = sumi // 10
            
            ln -= 1
            k //= 10
            pos -= 1
            
        if k == 0 and ln != -1:
            while ln >= 0:
                sumi = num[ln] + carry
                ret[pos] = sumi % 10
                carry = sumi // 10
                
                ln -= 1
                pos -= 1
                
        if ln == -1 and k != 0:
            while k:
                sumi = (k % 10) + carry
                ret[pos] = sumi % 10
                carry = sumi // 10
                
                k //= 10
                pos -= 1
                
        if carry:
            ret[pos] = carry
            
        return ret if ret[0] else ret[1:]
    
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxi = -1
        ret = ""
        
        for i in range(2, len(num)):
            if num[i - 2] == num[i - 1] == num[i]:
                maxi = max(maxi, ord(num[i]) - ord('0'))
            
        return str(maxi)*3 if maxi >= 0 else ret
    
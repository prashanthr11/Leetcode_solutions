class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        
        for i in range(len(digits) - 1, -1, -1):
            sumi = digits[i] + carry
            
            digits[i] = sumi % 10
            carry = sumi // 10
            
            if carry == 0:
                break
                
        if carry:
            return [carry] + digits
        
        return digits
    
                
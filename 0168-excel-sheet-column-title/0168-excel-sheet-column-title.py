class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ret = ""
        
        while columnNumber:
            columnNumber -= 1
            ret += chr(ord('A') + (columnNumber % 26))
            columnNumber //= 26
            
        return ret[::-1]
    
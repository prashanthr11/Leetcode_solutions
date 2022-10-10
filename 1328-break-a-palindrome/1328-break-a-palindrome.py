class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        ln = len(palindrome)
        i = 0
        
        if ln == 1:
            return ""
        
        while i < ln and palindrome[i] == "a":
            i += 1
            
        if i == ln:
            return palindrome[:-1] + "b"
        else:
            mid = ln // 2
            if i == mid:
                j = ln - 1
                while i < j and palindrome[j] == "a":
                    j -= 1
                    
                if i == j:
                    return palindrome[:-1] + "b"
                
            return palindrome[:i] + "a" + palindrome[i + 1:]
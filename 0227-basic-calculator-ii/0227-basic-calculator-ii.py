class Solution:
    def calculate(self, s: str) -> int:
        return self.optimise(s)
    
    
    def optimise(self, s):
        ret = 0
        last_number = 0 # 5
        current_number = 0
        operation = "+"
        
        for i in range(len(s)):
                
            if s[i].isdigit():
                current_number = current_number * 10 + ord(s[i]) - ord('0')
                
            if (not s[i].isdigit() and s[i] != " ") or (i == len(s) - 1):
                if operation == "+" or operation == "-":
                    ret += last_number
                    last_number = current_number if operation == '+' else -current_number
                elif operation == "*":
                    last_number = last_number * current_number
                elif operation == "/":
                    last_number = int(last_number / current_number)
                
                operation = s[i]
                current_number = 0
                
        return ret + last_number
    
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = list()
        
        def solve(x, y, op):
            x, y = int(x), int(y)
            
            if op == "+":
                ret = x + y
            elif op == "-":
                ret = x - y
            elif op == "*":
                ret = x * y
            else:
                ret = int(x / y)
                
            return str(ret)
        
        for i in tokens:
            if i in "+-*/":
                a = stk.pop()
                b = stk.pop()
                stk.append(solve(b, a, i))
            else:
                stk.append(i)
                
        return int(stk.pop())
    
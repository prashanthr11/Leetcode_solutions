class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        
        d = {}
        d['2'] = ['a', 'b', 'c']
        d['3'] = ['d', 'e', 'f']
        d['4'] = ['g', 'h', 'i']
        d['5'] = ['j', 'k', 'l']
        d['6'] = ['m', 'n', 'o']
        d['7'] = ['p', 'q', 'r', 's']
        d['8'] = ['t', 'u', 'v']
        d['9'] = ['w', 'x', 'y', 'z']
        ret = []
        lst = []
        ln = len(digits)
        
        def solve(idx):
            nonlocal lst
            
            if idx >= ln:
                if len(lst) == ln:
                    ret.append(''.join(lst))
                return
            
            for i in range(idx, ln):
                for j in d[digits[i]]:
                    lst.append(j)
                    solve(i + 1)
                    lst.pop()
        
        solve(0)
        return ret
    
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        '''
        Time Complexity: O((M + N)*2^N)
        Space Complexity: O(N)
        '''
        l = [i for i in arr if len(i) == len(set(i))]
        return self.solve(l, 0, len(l), "")
    
    def solve(self, l, i, ln, lst):
        
        if i >= ln:
            return len(lst)
        
        maxi = 0
        tmp_str = lst + l[i]
        if len(lst) + len(l[i]) == len(set(tmp_str)):
            maxi = self.solve(l, i + 1, ln, tmp_str)
        
        maxi = max(maxi, self.solve(l, i + 1, ln, lst))
        return maxi
    
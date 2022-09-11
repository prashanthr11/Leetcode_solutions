from bisect import bisect

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        return self.optimise(properties)
    
    
    def optimise(self, properties):
        '''
        Time Complexity: O(N Log N)
        Space Complexity: O(1)
        '''
        ret = 0
        properties.sort(key=lambda x: (x[0], -x[1]))
        mini = properties[-1][1]
        
        for x, y in properties[::-1]:
            if y < mini:
                ret += 1
                
            mini = max(mini, y)
            
        return ret
    
        
    def naive(self, properties):
        '''
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        '''
        ln = len(properties)
        cnt = 0
        
        for i in range(ln):
            flag = False
            for j in range(ln):
                if properties[i][0] < properties[j][0] and properties[i][1] < properties[j][1]:
                    flag = True
                    break
                    
            if flag:
                cnt += 1
                    
        return cnt
    
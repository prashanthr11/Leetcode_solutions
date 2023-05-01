class Solution:
    def average(self, salary: List[int]) -> float:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        mini, maxi = salary[0], salary[0]
        sumi = 0
        
        for i in salary:
            sumi += i
            mini = min(mini, i)
            maxi = max(maxi, i)
            
        return (sumi - maxi - mini) / (len(salary) - 2)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        st = set()
        ln = len(nums)
        
        sumi = 0
        for i in nums:
            if i in st:
                repeated = i
            
            st.add(i)
            sumi += i
            
        req = ln * (ln + 1) // 2
        return [repeated, req - sumi + repeated]
    
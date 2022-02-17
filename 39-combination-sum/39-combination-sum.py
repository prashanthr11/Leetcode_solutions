class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.naive(candidates, target)
    
    
    def naive(self, nums, target):
        self.ans = []
        self.solve(nums, target, 0, [])
        return self.ans
    
    def solve(self, nums, target, sumi, lst):
        # print(lst, sumi)
        if target < sumi:
            return
        
        if target == sumi:
            tmp = sorted(lst)
            if tmp not in self.ans:
                self.ans.append(tmp)
            return
        
        for i in range(len(nums)):
            if sumi + nums[i] <= target:
                self.solve(nums, target, sumi + nums[i], lst + [nums[i]])
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            idx = bisect.bisect_left(numbers, target - numbers[i], i + 1, len(numbers))
            
            if idx < len(numbers) and numbers[i] + numbers[idx] == target:
                return [i + 1, idx + 1]
            
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        visited = [False] * n
        cnt = 0
        
        dq = deque([0])
        
        while dq:
            cnt += 1
            
            for i in range(len(dq)):
                current_idx = dq.popleft()

                if visited[current_idx]:
                    continue

                visited[current_idx] = True
                
                if current_idx == n - 1:
                    return cnt - 1
                
                for j in range(1, nums[current_idx] + 1):
                    if current_idx + j < n and not visited[current_idx + j]:
                        dq.append(current_idx + j)
                        
        return cnt
    
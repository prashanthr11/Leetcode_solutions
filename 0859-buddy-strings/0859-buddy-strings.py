class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        ln1, ln2 = len(s), len(goal)
        cnt = 0
        is_done = False
        
        if ln1 != ln2:
            return False
        
        if s == goal:
            freq = [0] * 26
            
            for i in range(ln1):
                freq[ord(s[i]) - ord('a')] += 1
                if freq[ord(s[i]) - ord('a')] > 1:
                    return True
                
            return False
        else:
            for i in range(ln1):
                if s[i] != goal[i]:
                    if cnt == 0:
                        need = goal[i]
                        swap = s[i]
                        cnt += 1
                    elif cnt == 1:
                        if is_done == False and goal[i] == swap and s[i] == need:
                            is_done = True
                        else:
                            cnt += 1
                            break
                    else:
                        break

            return (cnt == 1) and is_done == True

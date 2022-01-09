class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        if 'L' not in instructions and 'R' not in instructions:
            return False
        
        if 'G' not in instructions:
            return True
        
        moves = []
        present = [0, 0]
        direction = 'N'
        i = 0
        ln = len(instructions)
        
        while i < ln:
            print(present, direction)
            moves.append(present.copy())
            
            if instructions[i] != 'G':
                if instructions[i] == 'L':
                    i, l_cnt = self.moving(instructions, 'L', i, ln)
                    direction = self.get_direction(direction, l_cnt, 'L')
                    continue

                if instructions[i] == 'R':
                    i, r_cnt = self.moving(instructions, 'R', i, ln)
                    direction = self.get_direction(direction, r_cnt, 'R')
            else:        
                if direction == 'N':
                    present[1] += 1
                elif direction == 'S':
                    present[1] -= 1
                elif direction == 'W':
                    present[0] -= 1
                else:
                    present[0] += 1

                i += 1
                    
        print(moves)
        return present == [0, 0] or direction != 'N'
                    
    def get_direction(self, present_direction, turns, pos):
        s = 'NWSE' if pos == 'L' else 'NESW'
        idx = s.index(present_direction)
        return s[(idx + turns) % 4]
        
    def moving(self, instructions, direction, i, n):
        cnt = 0
        while i < n:
            if instructions[i] == direction:
                cnt += 1
                i += 1
            else:
                break
            
        return i, cnt
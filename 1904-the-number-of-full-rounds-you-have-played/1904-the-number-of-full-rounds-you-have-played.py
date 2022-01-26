class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        login_hour, login_min = map(int, loginTime.split(':'))
        logout_hour, logout_min = map(int, logoutTime.split(':'))
            
        if login_hour > logout_hour or (login_hour == logout_hour \
                                        and login_min > logout_min):
            logout_hour += 24
            
        ret = 0
        if login_hour == logout_hour and logout_min > login_min:
            game_starts_min = ceil(login_min / 15) * 15
            game_ends_min = floor(logout_min / 15) * 15
            
            return len(range(game_starts_min, game_ends_min, 15))
            
        login_min = ceil(login_min / 15) * 15
        logout_min = floor(logout_min / 15) * 15
        
        if login_min == 60:
            login_hour += 1
            login_min = 0
            
        game_starts = login_hour * 100 + login_min
        game_ends = logout_hour * 100 + logout_min
        
        while True:
            # print(game_starts, game_ends)
            if self.check(game_starts, game_ends):
                break
                
            ret += 1
            hrs = game_starts // 100
            mins = game_starts % 100
            mins += 15
            if mins >= 60:
                hrs += 1
                mins %= 60
                
            game_starts = (hrs * 100) + mins
                
        return ret
    
    
    def check(self, start_time, end_time):
        
        start_hrs = start_time // 100
        start_mins = start_time % 100
        end_hrs = end_time // 100
        end_mins = end_time % 100
        
        return start_hrs == end_hrs and start_mins == end_mins
    
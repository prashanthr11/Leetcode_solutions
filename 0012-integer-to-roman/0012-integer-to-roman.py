from bisect import bisect

class Solution:
    def intToRoman(self, num: int) -> str:
        return self.method_2(num)

    def method_2(self, num):
        '''
        Time Complexity: O(1)
        Space Complexity: O(1)
        '''
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        
        return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]
    
        
    def method_1(self, num):
        '''
        Time Complexity: O(Log Log N) -> Log N for binary search and Log N for creating roman numeral for each digit
        Space Complexity: Not sure! coz it is dependent on each digit. Eg: 7 vs 8 vs 9
        '''
        mapping = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }
        
        keys = [1, 5, 10, 50, 100, 500, 1000]
        ret = []
        
        while num:
            if num == 4:
                ret.append("IV")
                break

            if num == 9:
                ret.append("IX")
                break
            
            if 40 <= num <= 49:
                ret.append("XL")
                num %= 10
                continue
            
            if 90 <= num <= 99:
                ret.append("XC")
                num %= 10
                continue
                
            if 400 <= num <= 499:
                ret.append("CD")
                num %= 100
                continue
            
            if 900 <= num <= 999:
                ret.append("CM")
                num %= 100
                continue
                
            idx = bisect(keys, num)
            max_currency = keys[idx - 1]
            symbol = mapping[max_currency]
            ret.append(symbol)
            num -= max_currency
            
        return "".join(ret)
    
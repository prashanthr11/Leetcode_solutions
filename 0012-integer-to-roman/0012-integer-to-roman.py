from bisect import bisect

class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }
        
        keys = list(mapping.keys())
        ret = ""
        
        while num:
            if num == 4:
                ret += "IV"
                break

            if num == 9:
                ret += "IX"
                break
            
            if 40 <= num <= 49:
                ret += "XL"
                num %= 10
                continue
            
            if 90 <= num <= 99:
                ret += "XC"
                num %= 10
                continue
                
            if 400 <= num <= 499:
                ret += "CD"
                num %= 100
                continue
            
            if 900 <= num <= 999:
                ret += "CM"
                num %= 100
                continue
                
            idx = bisect(keys, num)
            max_currency = keys[idx - 1]
            symbol = mapping[max_currency]
            ret += symbol
            num -= max_currency
            
        return ret
    
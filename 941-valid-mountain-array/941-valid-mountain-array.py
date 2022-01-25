class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 1
        ln = len(arr)
        
        if ln <= 2:
            return False
        
        while i < ln and arr[i] > arr[i - 1]:
            i += 1
            
        if i == 1:
            if arr[i] < arr[i - 1]:
                return False
            
        if i == ln:
            return False
        
        while i < ln and arr[i] < arr[i - 1]:
            i += 1
            
        return True if i == ln else False
    
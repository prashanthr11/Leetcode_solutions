from collections import defaultdict as dt

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dt(lambda :-1)
        

    def put(self, key: int, val: int) -> None:
        """
        value will always be non-negative.
        """
        self.d[key] = val
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        tmp = self.d[key]
        if tmp != -1:
            return tmp
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.d[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
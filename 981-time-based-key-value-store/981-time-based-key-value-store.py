class TimeMap:

    def __init__(self):
        self.d = defaultdict(deque)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.d[key]
        if len(lst) == 0:
            return ""
        
        idx = bisect.bisect_left(lst, (timestamp, chr(127)))
        return lst[idx - 1][1] if idx else ""
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
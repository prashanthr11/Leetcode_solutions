class StockPrice:

    def __init__(self):
        self.d = dict()
        self.mini = []
        self.maxi = []
        self.latest = 0

    def update(self, timestamp: int, price: int) -> None:
        self.latest = max(self.latest, timestamp)
        heapq.heappush(self.mini, (price, timestamp))
        heapq.heappush(self.maxi, (-price, timestamp))
        
        if timestamp in self.d:
            self.d[timestamp] = price
        else:
            self.d[timestamp] = self.d.get(timestamp, 0) + price

    def current(self) -> int:
        return self.d[self.latest]

    def maximum(self) -> int:
        while True:
            top = self.maxi[0]
            if self.d[top[1]] == -top[0]:
                return -top[0]
            heapq.heappop(self.maxi)

    def minimum(self) -> int:
        while True:
            top = self.mini[0]
            if self.d[top[1]] == top[0]:
                return top[0]
            heapq.heappop(self.mini)


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        '''
        Time Complexity: O(1)
        Space Complexity: O(N)
        '''
        cost = 1
        while self.prices and self.prices[-1][0] <= price:
            cost += self.prices[-1][1]
            self.prices.pop()
            
        self.prices.append((price, cost))
        return cost


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
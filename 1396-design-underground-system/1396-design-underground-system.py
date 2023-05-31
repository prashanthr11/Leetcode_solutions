class UndergroundSystem:

    def __init__(self):
        self.travelling = set()
        self.from_loc = defaultdict(list)
        self.travels = defaultdict(int)
        self.travel_counts = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.travelling:
            self.travelling.add(id)
            self.from_loc[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.travelling:
            from_, start_time = self.from_loc[id]
            del self.from_loc[id]
            self.travels[(from_, stationName)] += t - start_time
            self.travel_counts[(from_, stationName)] += 1
            self.travelling.remove(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # lst = self.travels[(startStation, endStation)]
        # return sum(lst)/len(lst)
        
        loc = (startStation, endStation)
        return self.travels[loc] / self.travel_counts[loc]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
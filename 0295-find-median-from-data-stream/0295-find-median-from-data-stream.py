from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.lst = SortedList()

    def addNum(self, num: int) -> None:
        self.lst.add(num)

    def findMedian(self) -> float:
        ln = len(self.lst)
        
        if ln % 2:
            return self.lst[ln // 2]
        else:
            return (self.lst[ln // 2] + self.lst[(ln - 1) // 2]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
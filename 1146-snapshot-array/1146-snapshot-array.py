class SnapshotArray:

    def __init__(self, length: int):
        self.cnt = 0
        self.lst = [[[0, 0]] for i in range(length)]

    def set(self, index: int, val: int) -> None:
        if self.lst[index][-1][0] == self.cnt:
            self.lst[index][-1][1] = val
        else:
            self.lst[index].append([self.cnt, val])

    def snap(self) -> int:
        self.cnt += 1
        return self.cnt - 1

    def get(self, index: int, snap_id: int) -> int:
        idx = bisect.bisect_right(self.lst[index], [snap_id, 10**9])
        return self.lst[index][idx - 1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
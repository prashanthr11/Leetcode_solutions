class MyHashSet:

    def __init__(self):
        self.st = [0] * ((10**6) + 1)

    def add(self, key: int) -> None:
        if self.st[key] == 0:
            self.st[key] = 1

    def remove(self, key: int) -> None:
        if self.st[key]:
            self.st[key] -= 1

    def contains(self, key: int) -> bool:
        return self.st[key] == 1


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
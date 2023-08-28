class MyStack:

    def __init__(self):
        self.stk = []
        self.ln = 0

    def push(self, x: int) -> None:
        self.stk.append(x)
        self.ln += 1

    def pop(self) -> int:
        last_item = -1
        if self.ln > 0:
            self.ln -= 1
            last_item = self.stk.pop()
            
        return last_item

    def top(self) -> int:
        return self.stk[self.ln - 1] if self.ln > 0 else -1

    def empty(self) -> bool:
        return self.ln == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
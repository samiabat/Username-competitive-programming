class MinStack:

    def __init__(self):
        self.l = []

    def push(self, val: int) -> None:
        self.l.append(val)

    def pop(self) -> None:
        self.l.pop()
        

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return min(self.l)

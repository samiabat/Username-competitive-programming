class MyQueue:

    def __init__(self):
        self.l = []

    def push(self, x: int) -> None:
        self.l.append(x)

    def pop(self) -> int:
        f = self.l[0]
        self.l = self.l[1:]
        return f

    def peek(self) -> int:
        return self.l[0]
        

    def empty(self) -> bool:
        return len(self.l) == 0

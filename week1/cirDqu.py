class MyCircularDeque:

    def __init__(self, k: int):
        self.l = []
        self.k = k

    def insertFront(self, value: int) -> bool:
        
        s = "N"
        if len(self.l)<self.k:
            self.l.insert(0, value)
            s = "Y"
        return s == "Y"
        

    def insertLast(self, value: int) -> bool:
        s = "N"
        if len(self.l)<self.k:
            self.l.append(value)
            s = "Y"
        return s == "Y"
        

    def deleteFront(self) -> bool:
        s = "N"
        if len(self.l)>=1:
            self.l = self.l[1:]
            s = "T"
        return s == "T"
        

    def deleteLast(self) -> bool:
        s = "n"
        if len(self.l)>=1:
            self.l.pop()
            s = "T"
        return s == "T"
        

    def getFront(self) -> int:
        if len(self.l) == 0:
            return -1
        return self.l[0]

    def getRear(self) -> int:
        if len(self.l) == 0:
            return -1
        return self.l[-1]

    def isEmpty(self) -> bool:
        return len(self.l) == 0
        

    def isFull(self) -> bool:
        return len(self.l) == self.k
        
class RecentCounter:

    def __init__(self):
        self.request = []

    def ping(self, t: int) -> int:
        self.request.append(t)
        i = 0
        self.request[0]
        while (self.request[i])<(t-3000):
            i+=1
        self.request = self.request[i:]
        return len(self.request)
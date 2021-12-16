class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = []
        for pair in points:
            d.append((pair[0])**2+(pair[1])**2)
        c = 0
        a= []
        for i in range(k):
            c = d.index(min(d))
            a.append(c)
            d[c] = max(d) + 1
        l = []
        for i in a:
            l.append(points[i])
        return l
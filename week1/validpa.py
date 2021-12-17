class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(":")","{":"}", "[":"]"}
        b = []
        for i in s:
            if i in dic:
                b.append(i)
            else:
                if len(b) > 0 and (b[-1] in dic )and (dic[b[-1]] == i):
                    b.pop()
                else:
                    b.append(i)
        return len(b) == 0
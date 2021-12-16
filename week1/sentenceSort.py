class Solution:
    def sortSentence(self, s: str) -> str:
        a = s.split()
        c = ["0"]*len(a)
        for i in a:
            c[int(i[-1])-1] = i[:-1]
        fin = ""
        for i in c:
            fin = fin + i + " "
        return fin.rstrip()
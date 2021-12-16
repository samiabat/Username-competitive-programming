class Solution:
    def romanToInt(self, s = "XIII"):
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        arabic = 0
        for l in s:
            arabic += (dic[l])
        if s == "IV":
            arabic = 4
        if s == "IX":
            arabic = 9
        if s == "IL":
            arabic = 49
        if s == "IC":
            arabic = 99
        if s == "ID":
            arabic = 499
        if s == "IM":
            arabic = 999

        return arabic

s = Solution()
print(s.romanToInt("IXXX"))

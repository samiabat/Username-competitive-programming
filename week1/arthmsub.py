class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        c = []
        for i in range(len(l)):
            s = True
            a = nums[l[i]:r[i]+1]
            a.sort()
            d = a[1]-a[0]
            for n in range(1, len(a)):
                if a[n]-a[n-1]!=d:
                    s = False
            c.append(s)
        return c
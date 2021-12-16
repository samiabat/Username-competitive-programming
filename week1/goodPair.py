class Solution:
    def fact(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n*fact(n-1)
    def comb(n, b):
        return fact(n)(fact(b)*fact(n-b))
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a = []
        for num in nums:
            if nums.count(num)>1 and num not in a:
                a.append(num)
        print(a)
        sumi = 0
        for i in a:
            c = nums.count(i)
            sumi+=comb(c,2)
        return sumi
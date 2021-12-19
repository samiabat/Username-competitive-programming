class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dic = {}
        for i in range(len(arr)):
            if arr[i] in dic:
                dic[arr[i]] += 1
            else:
                dic[arr[i]] = 1
        l = []
        for key in dic:
            l.append(dic[key])
        l = sorted(l)[::-1]
        c = 0
        tot = 0
        for i in l:
            c+=1
            tot+=i
            if tot>=len(arr)//2:
                break
                
        return c
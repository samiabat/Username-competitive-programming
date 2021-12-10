#User function Template for python3

class Solution: 
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            minind = i
            for j in range(i+1, len(arr)):
                if arr[j]<arr[minind]:
                    minind = j
            arr[i], arr[minind] = arr[minind], arr[i]
        return arr
A = [10, 15, 21, 12, 31]
s  = Solution()
print(s.selectionSort(A, 5))
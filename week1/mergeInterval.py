class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # first let me sort it based on its 
        for i in range(len(intervals)):
            for j in range(i):
                if intervals[i][0]<intervals[j][0]:
                    intervals[i],intervals[j] = intervals[j],intervals[i]
        for i in range(len(intervals)):
            for j in range(i):
                if intervals[i][0]==intervals[j][0] and intervals[i][1]<intervals[j][1]:
                    intervals[i],intervals[j] = intervals[j],intervals[i]
        print(intervals)
        val = []
        i = 1
        val.append(intervals[i-1]) #  [[1,3]]
        while(i<len(intervals)):
            M = "F"
            print("val",val)
            if val[-1][1]>=intervals[i][0] and val[-1][1]<=intervals[i][1]:
                print(True)
                val[-1][1] = intervals[i][1]
                M = "T"
                i+=1
            elif val[-1][1]>intervals[i][1]:
                M = "T"
                i+=1
            if M == "F":
                val.append(intervals[i]) #  [[1,3]]
                i+=1
                
        return val
class Solution(object):
    def targetIndices(self, nums, target):
        for i in range(len(nums)):
            minind = i
            for j in range(i+1, len(nums)):
                if nums[j]<nums[minind]:
                    minind = j
                    
            nums[i], nums[minind] = nums[minind], nums[i]
        
        a = []
        for i in range(len(nums)):
            if nums[i] == target:
                a.append(i)
                
        return a
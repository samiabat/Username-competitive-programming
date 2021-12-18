class Solution:
    def rearrangeArray(self, nums):
        s = []
        nums.sort()
        if len(nums)==0 or len(nums) == 1 or len(nums) == 2:
            return nums
        s.append(nums[0])
        for i in range(1, len(nums)-1):
            if (len(s) >= 2) and ((s[-2]+nums[i]) == (2*s[-1])):
                nums[i+1], nums[i] = nums[i], nums[i+1]
            elif len(s) <=2:
                pass
            s.append(nums[i])
        s.append(nums[-1])
        if s[-3]+s[-1] == 2*s[-2]:
            s[-1],s[0] = s[0], s[-1]
        if s[0]+s[2] == 2*s[1]:
            s[0],s[1] = s[1],s[0]
        return s
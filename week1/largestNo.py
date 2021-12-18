class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums.sort()
        nums = nums[::-1]
        print(nums)
        n = len(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if int(nums[i]+nums[j])<int(nums[j]+nums[i]):
                    nums[i],nums[j] = nums[j],nums[i]
        s = ""
        for i in nums:
            s+=i
        if len(s)>0:
            if s[0] == "0":
                return "0"
        return s
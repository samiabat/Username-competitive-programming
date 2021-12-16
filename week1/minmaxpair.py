class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        a = []
        for i in range(len(nums)//2):
            num = 0
            num = nums[i]+nums[-1-i]
            a.append(num)
        return max(a)
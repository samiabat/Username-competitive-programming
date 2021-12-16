class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        c = sorted(nums)
        d = []
        for i in range(len(nums)):
            v = c.index(nums[i])
            d.append(v)
        return d
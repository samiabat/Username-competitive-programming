class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val = []
        for i in range(len(nums)):
            if nums[i] not in val:
                val.append(nums[i])
        t = len(val)
        n = []
        print(val)
        for i in val:
            n.append(nums.count(i))
        c = []
        for i in range(k):
            index = n.index(max(n))
            c.append(val[index])
            n.pop(index)
            val.pop(index)
        return c
            
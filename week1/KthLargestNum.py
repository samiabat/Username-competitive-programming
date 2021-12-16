class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        c = []
        for a in nums:
            c.append(int(a))
            
        
        c.sort()
        
        return str(c[::-1][k-1])
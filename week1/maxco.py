class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)[::-1]
        # 1 2 2 4 7 8 
        tot = 0
        i = 1
        count = 0
        while count<len(piles)//3:
            tot+=piles[i]
            i = i+2
            count+=1
        return tot
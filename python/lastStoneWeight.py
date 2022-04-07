class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) >= 2:
            stones.sort()
            stones[-1] -= stones.pop(-2)
        return stones[0] 
        
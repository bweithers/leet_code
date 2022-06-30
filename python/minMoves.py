class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        target = sorted(nums)[len(nums)//2]
        return sum([abs(target-x) for x in nums])
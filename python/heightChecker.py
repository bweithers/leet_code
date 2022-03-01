class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s = sorted(heights)
        r = 0
        for x1,x2 in zip(s,heights): r+= x1!=x2
        return r
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d = {i+1: False for i in range(len(nums))}
        for x in nums: 
            d[x] = True
        out=[]
        for x in d:
            if not d[x]: 
                out.append(x)
        return out
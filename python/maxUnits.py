class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        s = sorted(boxTypes, key = lambda x: -x[1])
        ans = 0
        
        for x in s:
            ans += x[1] * min(x[0],truckSize)
            truckSize -= x[0]
            if truckSize <=0: return ans
                
        return ans
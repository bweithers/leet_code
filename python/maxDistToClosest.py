class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        md = 0
        lp = 0
        left = -1
        # if the best spot is on the far left, the md is the first '1' we find
        # if the best spot is somewhere in the middle, the md is the distance between the two people //2
        # if the best spot is on the far right, the md is len(seats) - the last '1' we find - 1
        
        for i,x in enumerate(seats):
            #print(i,lp,md)  
            
            if x:
                if left == -1:
                    left = i
                md = max(md, (i-lp)//2)
                lp = i
        
        # check right side
        md = max(md, len(seats)-lp-1)
        # check left side
        md = max(md, left)
        return md
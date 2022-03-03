# [1,2,3,4,5]
# 123, 234, 345, 1234, 2345, 12345  6
# 123, 234, 1234, 345, 2345, 12345  6
# for every ele that we add onto a sequence, we get size new subarrays where size is the number of previous equal slices
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3: return 0
        i, r, size, diff = 0,0,0,0
        
        while i < len(nums)-2:
            diff = nums[i+1] - nums[i]
            size = 3
            
            # count the running subarrays differently
            while nums[i+2] - nums[i+1] == diff:
                r+=size-2
                size+=1
                i+=1
                if i+2 >= len(nums):
                    break
                continue
            i+=1
                
        return r
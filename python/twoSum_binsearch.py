class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def bin_search(a,t):
            l,r = 0, len(a)-1
            while l <= r:
                mid = (l + r)//2
                if a[mid]==t: 
                    return mid
                if t > a[mid]:
                    l = mid+1
                elif t < a[mid]:
                    r = mid-1
            return -1
        
        for i,x in enumerate(numbers):
            out = bin_search(numbers[i+1:],target-x)
            if out != -1:
                return [i+1, out+i+2]
    
        return []
            
            
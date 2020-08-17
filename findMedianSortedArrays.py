def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        i,j = 0,0
        if (n % 2) == 1:
            if not nums1:
                return nums2[n//2]
            elif not nums2:
                return nums1[n//2]
            for k in range( (n // 2) ):
                if i == len(nums1):
                    j+= 1
                    continue
                elif j == len(nums2):
                    i += 1
                    continue
                if nums1[i] < nums2[j]:
                    i += 1
                else:
                    j += 1
            if i == len(nums1):
                return nums2[j]
            elif j == len(nums2):
                return nums1[i]
            else:    
                return min(nums1[i], nums2[j])
            return None
        else:
            if not nums1:
                return (nums2[n//2 - 1] + nums2[n//2]) / 2 
            elif not nums2:
                return (nums1[n//2 - 1] + nums1[n//2]) / 2 
            for k in range( (n // 2) - 1 ):
                if i == len(nums1):
                    j+= 1
                    continue
                elif j == len(nums2):
                    i += 1
                    continue
                if nums1[i] < nums2[j]:
                    i += 1
                else:
                    j += 1
            if i == len(nums1):
                cands = [nums2[j], nums2[j+1]]
            elif i+1 == len(nums1) and j+1 == len(nums2):
                cands = [nums1[i], nums2[j]]
            elif i+1 == len(nums1):
                cands = [nums1[i], nums2[j], nums2[j+1]]
            elif j == len(nums2):
                cands = [nums1[i], nums1[i+1]]
            elif j+1 == len(nums2):
                cands = [nums1[i], nums1[i+1], nums2[j]]
            else:           
                cands = [nums1[i], nums1[i+1], nums2[j], nums2[j+1]]
            cands.sort()
            return (sum(cands[0:2]) / 2)
        return None
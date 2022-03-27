
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i,x in enumerate(mat): heappush(heap, tuple((sum(x),i,x)))
        return [x[1] for x in nsmallest(k,heap)]
        
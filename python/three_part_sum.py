    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s=0
        sm=sum(A)//3
        c=0
        for i,x in enumerate(A[:-1]):
            s += x
            if s == sm:
                s = 0
                c += 1
                if c == 2:
                    return True
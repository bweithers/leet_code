 # d = {1:True, 2: True, 3: False, 4: True}
    def isPowerOfTwo(self, n: int) -> bool:
        # if n in self.d: 
        #     return self.d[n]
        # if (n*10)%10: 
        #     self.d[n] = False
        #     return False
        # else: 
        #     return self.isPowerOfTwo(n/2)
        return sum([int(x) for x in bin(n) if x!='b'])==1 if n >= 0 else False 
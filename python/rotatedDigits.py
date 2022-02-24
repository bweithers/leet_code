class Solution:
    def rotatedDigits(self, n: int) -> int:
        # we get a 'good' number if it has a 2 or 5 and no 347
        # 1-10 is 4
        # every 10 after that is 
        r = 0
        for i in range(n+1):
            good = False
            for c in str(i):
                if c in '2569':
                    good=True
                if c in '347':
                    good=False
                    break
            r+=good
        return r
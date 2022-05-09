class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        out = ['']
        d = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        for c in digits:
            n = []
            while out:
                o = out.pop()
                for x in d[c]:
                    n.append(o + x) 
            out = n
        
        return out
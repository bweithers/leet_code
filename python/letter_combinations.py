class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        prev = [""]
        for d in digits:
            prev = self.f(prev, int(d))
        return prev
            
    def f(self, prev: str, digit: int) -> List[str]:
        letters = {2: 'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        new = []
        for c in letters[digit]:
            for s in prev:
                new.append(s + c)
        #print(new)
        return new
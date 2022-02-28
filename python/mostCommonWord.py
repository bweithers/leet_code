class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        d = {}
        
        punc = "!?',;."
        for p in punc:
            paragraph = paragraph.replace(p,' ')
        paragraph = paragraph.lower()
        
        for w in paragraph.split():
            if w in banned: continue
            if w not in d:
                d[w] = 1
            else:
                d[w]+=1
        
        return sorted(d, key = lambda x: -d[x])[0]
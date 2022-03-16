class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # if s is to be divided by t it must start with t
        def strdiv(s,t):
            if s == t: return True
            if len(s) < len(t): return False
            if s[:len(t)]!=t: return False
            return strdiv(s[len(t):],t)
        
        
        # is there a case where the next letter is not the same but there is still some t?
        curr_max = ""
        for i,x in enumerate(str1):
            if i == len(str2): 
                break
            if str1[i] != str2[i]: return ""
            # print(i,x)
            if strdiv(str1,str1[:i+1]) and strdiv(str2,str1[:i+1]): 
                curr_max = str1[:i+1]
        
        return curr_max
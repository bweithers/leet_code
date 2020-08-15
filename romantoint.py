def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"I": 1, "V":5, "X":10, "L":50,"C":100,"D":500,"M":1000}
        x = 0
        for i,c in enumerate(s):
            if i == len(s) - 1:
                x += dic[c]
                continue
            if dic[s[i]] < dic[s[i+1]]:
                x -= dic[s[i]]
                continue
            else:
                x += dic[c]
        return x
        

class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if str == "":
            return 0      
        retval = ""
        sign = ""
        if str[0] == '+':
            sign = '+'
            str = str[1:]
        elif str[0] == '-':
            sign = '-'
            str = str[1:]
        for c in str:
            if c in string.digits:
                retval += c
            else:
                break
        if retval == "":
            return 0
        retval = int(sign + retval)
        if retval > 2147483647 :
            retval = 2147483647
        elif retval < -2147483648:
            retval = -2147483648
        return retval
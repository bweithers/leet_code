class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        for j in range(len(typed)):
            # good letter!
            if i < len(name) and name[i] == typed[j]:
                i += 1
            # we are not on a repeat letter
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        # check that we got to the end of name
        return i == len(name)
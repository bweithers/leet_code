    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        pattern = strs[0]
        for x in strs[1:]:
            if not x:
                return ""
            if len(x) > len(pattern):
                for i,c in enumerate(x):
                    try:
                        if c != pattern[i]:
                            pattern = pattern[:i]
                            if not pattern:
                                return ""
                            break
                    except IndexError:
                        pattenr = pattern[:i]
            else:
                # print('in else')
                for i,c in enumerate(pattern):
                    try:
                        if c != x[i]:
                            pattern = x[:i]
                            if not pattern:
                                return ""
                            break
                    except IndexError:
                        pattern = x[:i]
        return pattern
                
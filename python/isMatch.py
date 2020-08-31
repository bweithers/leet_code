def isMatch(s: str, p: str) -> bool:
    i = j = 0
    while j < len(p):
        if p[j] == '*':
            # Not sure if the first char of the pattern can be a star, or what happens then
            # but it said it was an invalid test case so i will remove the try catch here for clutter's sake
            prev = p[j-1]
            while i < len(s) and s[i] == prev:
                i += 1  
            # this case is whack af
            if prev == '.':
                # If we can find ANY point in the string after our '.*' 
                # such that the remaining pattern and string are a match
                # we can return True.

                # If we can't find any point in the remaining string such that the remaining pattern
                # is a match, we are forced to return False
                while not self.isMatch(s[i:],p[j:]):
                    i += 1
                    if i == len(s):
                        return False
                return True         
        # Dot
        elif p[j] == '.':
            # Handle stars in the star case.. '.*' God help us
            try:
                if p[j+1] == '*':
                    continue
            except IndexError:
                break
            i += 1
        # Single letter case
        else:
            # Handle all stars in star case
            try:
                if p[j+1] == '*':
                    continue
            except IndexError:
                break
            # If single letters don't match, we are done
            if p[j] != s[i]:
                return False
            # We have moved farther into the string, the single letters matched.
            else:
                i += 1
        j += 1
	print(j)
    # If we have run through the whole pattern and we are done with the String
    # then the regex has succeeded
    if i == len(s): return True
    # If we finished the pattern but not the string we haven't found a match
    else: return False
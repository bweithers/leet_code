class Solution:
    def longestPalindrome(self, s: str) -> str:
        # what is the longest palendrome STARTING at every i?
        
        # brute force, go through all possible follow-up substrings at every i, On**2
        # if len(s) <= 1: return s
        # s = list(s)
        # m = s[0]
        # for i,c in enumerate(s):
        #     for j,d in enumerate(s[i:]):
        #         # print(''.join(s[i:i+j+1]), ''.join(reversed(s[i:i+j+1])))
        #         if ''.join(s[i:i+j+1]) == ''.join(reversed(s[i:i+j+1])):
        #             if j >= len(m):
        #                 m = s[i:i+j+1]
        # return ''.join(m)
        
        # two pointer? if there is a palendrome between the two pointers we are good..
        # something like merge sort? start in the middle and keep breaking out into smaller pieces but as soon as we find a palendrome we can stop
        # guaranteed to be the biggest since we go from biggest to smallest
        # can't split in two, what if s[:-1] is a palendrome
        
        # any 'even' palendrome has a repeat of each letter
        # any 'odd' palendrome has a repeat of each letter except the center (maybe)
        # if we know that we do not have duplicates for each non-center letter in a slice, we can ignore that slice
        # aha! to have any palendrome of length 5, the inner 3 must first be a palendrome
        # to have any palendrome of length 4, the inner two must first be a palendrome
        
        m = ''
        for i,c in enumerate(s):
            # odd checking
            os = 0
            # expand outward while things are equal to each other
            while i+os < len(s) and i-os >= 0 and s[i+os] == s[i-os]:
                os += 1
            # we found the spot where things are not equal, backtrack for recording purposes
            os -= 1
            if os*2+1 > len(m):
                m = s[i-os:i+os+1]
            
            # even checking
            if i+1 < len(s) and s[i] == s[i+1]:
                os = 0
                while i+1+os < len(s) and i-os >= 0 and s[i+os+1] == s[i-os]:
                    os +=1
                os -= 1
                
                if os*2+2 > len(m):
                    m = s[i-os:i+os+2]
            
            
        return m
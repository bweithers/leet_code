class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        elif len(s) == 2 and s[1] != s[0]:
            return s[0]
        ans = s[0]
        for i,c in enumerate(s):
            left_bound = right_bound = i
            temp = c
            while s[left_bound] == s[right_bound]:
                left_bound -= 1
                right_bound += 1
                if left_bound < 0 or right_bound >= len(s):
                    break
                if s[left_bound] == s[right_bound]:
                    temp = s[left_bound] + temp
                    temp += s[right_bound]
                    if len(temp) > len(ans):
                        ans = temp 
                        #print(f'Changed max palindrome staring from index {i}')
        for i,c in enumerate(s[:-1]):
            left_bound , right_bound = i , i + 1
            temp = ""
            while s[left_bound] == s[right_bound]:
                temp = s[left_bound] + temp
                temp += s[right_bound]
                if len(temp) > len(ans):
                    ans = temp 
                    #print(f'Changed max palindrome staring from index {i}')
                left_bound -= 1
                right_bound += 1
                if left_bound < 0 or right_bound >= len(s):
                    break

  
        return ans
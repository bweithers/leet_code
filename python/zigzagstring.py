class Solution:
    # O(n), is there O(1)?
    def convert(self, s: str, numRows: int) -> str:      
        # Cheeky edge cases
        if not s:
            return ""
        if numRows == 1:
            return s
        ans = ''
        direction = 'DOWN'
        # Setup empty rows to be filled later
        rows = {i: "" for i in range(numRows)}
        row_num = 0
        
        for i,c in enumerate(s):
            # Add in new characters one at a time
            rows[row_num] += c
            if direction == 'DOWN':
                row_num += 1
                if row_num == numRows - 1:
                    direction = 'UP'
            elif direction == 'UP':
                row_num -= 1
                if row_num == 0:
                    direction = 'DOWN'
        
        for i in range(numRows):
            ans += rows[i]
        return ans
            
        
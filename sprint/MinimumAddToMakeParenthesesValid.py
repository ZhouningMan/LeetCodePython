class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        total = 0
        open_parentheses = 0
        for c in S:
            if open_parentheses == 0 and c == ')':
                total += 1
            elif c == '(':
                open_parentheses += 1
            else:
                open_parentheses -= 1
        return total + open_parentheses

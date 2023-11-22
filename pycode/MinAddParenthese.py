'''
LC 921
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.
'''

class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return True
        num_ops = 0
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            else: ## ')'
                if not stack: # no remainning left parent
                    num_ops += 1
                elif stack[-1] == '(':
                    stack.pop()
        num_ops += len(stack)
        return num_ops

S = Solution()
print(S.minAddToMakeValid('())'))
print(S.minAddToMakeValid('((('))
print(S.minAddToMakeValid(')))'))
print(S.minAddToMakeValid(')())'))
print(S.minAddToMakeValid('(())'))
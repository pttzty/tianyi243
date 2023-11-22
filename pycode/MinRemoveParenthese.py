'''
LC 1249
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
'''

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        
        stack = []
        index_remove = set()
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if not stack:
                    index_remove.add(i)
                else:
                    stack.pop()
            else:
                continue
        if len(stack) > 0:
            for i in stack:
                index_remove.add(i)
        return "".join([s[i] for i in range(len(s)) if i not in index_remove])

S = Solution()
print(S.minRemoveToMakeValid("lee(t(c)o)de)"))
print(S.minRemoveToMakeValid("a)b(c)d"))
print(S.minRemoveToMakeValid("))(("))
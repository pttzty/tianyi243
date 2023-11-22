'''
LC1759 - Count Number of Homogenous Substrings
Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.
A string is homogenous if all the characters of the string are the same.
A substring is a contiguous sequence of characters within a string
'''

'''
Thoughts: it's just a math problem :)
'''

def count_sum(repeat_len):
    return repeat_len * (1+repeat_len) / 2

class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        repeat_len = 1
        prev_char = s[0]
        result = 0
        if len(s) == 1:
            return 1
        for i in range(1,len(s)):
            if s[i] != prev_char:
                result += count_sum(repeat_len)
                repeat_len = 1
                prev_char = s[i]
            else:
                repeat_len += 1
            if i == len(s) - 1:
                result += count_sum(repeat_len)
        return int(result) % (10**9 + 7)

if __name__ == "__main__":
    S = Solution()
    s = "abbcccaa"
    print(S.countHomogenous(s))
    s = "xy"
    print(S.countHomogenous(s))
    s = "zzzzz"
    print(S.countHomogenous(s))
        
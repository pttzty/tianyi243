'''
LC 151. Reverse Words in a String
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
'''

'''
Thoughts: to have a constance space, we need to deploy a two pointer solution, but python string is not mutable, let's just do regular o(n) space
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])

if __name__ == "__main__":
    S = Solution()
    s = "the sky is blue"
    print(S.reverseWords(s))
    s = "  hello world  "
    print(S.reverseWords(s))
    s = "a good   example"
    print(S.reverseWords(s))
        
'''
LC 2405 Optimal Partition of String
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.

 

Example 1:

Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
Example 2:

Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").
'''

class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr_set = set()
        curr_ops = 1
        for k in s:
            if k not in curr_set:
                curr_set.add(k)
            else:
                curr_ops += 1
                curr_set = set()
                curr_set.add(k)
        return curr_ops

if __name__ == "__main__":
    S = Solution()
    print(S.partitionString("abacaba"))
    print(S.partitionString("ssssss"))
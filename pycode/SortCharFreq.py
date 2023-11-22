'''
LC 451
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.
'''

from collections import defaultdict
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count_dict = defaultdict(int)
        for k in s:
            count_dict[k] += 1
        
        bucket = [[] for _ in range(len(s)+1)]

        for k in count_dict:
            bucket[count_dict[k]].append(k)
        
        result = ''
        for i in range(len(bucket)-1,0,-1):
            if not bucket[i]:
                continue
            else:
                for k in bucket[i]:
                    result = result + k * i
        return result

S = Solution()
print(S.frequencySort('tree'))
print(S.frequencySort('cccaaa'))
print(S.frequencySort('eeeee'))
'''
LC 17
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''
class Solution(object):
    def recur(self, base_str, remain_digits):
        if len(remain_digits) == 1:
            res = [base_str + c for c in self.map[remain_digits[0]]]
            self.output += res
            return
        else:
            for c in self.map[remain_digits[0]]:
                self.recur(base_str+c,remain_digits[1:])

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.map = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],
        }
        self.output = []
        if not digits:
            return []
        
        self.recur(base_str='',remain_digits=digits)
        return self.output


S = Solution()
print(S.letterCombinations('239'))
print(S.letterCombinations('2'))
print(S.letterCombinations(''))
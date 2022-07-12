class Solution:

    # 条件检查的字符串的前后仅需倒叙先后还是 要再 并且要在条件的最前开始否则也会出去 ！
    def lengthOfLastWord(self, s: str) -> int:
        # string can be reversed traverse
        i, leng = 0, 0
        rev_s = s[::-1]
        while rev_s[i] == ' ':
            i += 1
        # 这里条件的先后不一样
        while i <= len(rev_s)-1 and rev_s[i] != ' ':
            leng += 1
            i += 1
        return leng
            
        
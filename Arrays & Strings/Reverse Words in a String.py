class Solution(object):
    def reverseWords(self, s):
        words=s.split()
        reversed=words[::-1]
        return ' '.join(reversed)

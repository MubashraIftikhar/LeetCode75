class Solution(object):
    def gcdOfStrings(self, str1, str2):
        j = 1
        answer = ""

        while j <= len(str2):
            key = str2[:j]
            j += 1

            if str1 == key * (len(str1) // len(key)) and str2 == key * (len(str2) // len(key)):

                answer = key

        return answer


        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        n=len(candies)
        answer=[False]*n
        for i in range(n):
            if candies[i]+extraCandies >= max(candies):
                answer[i]=True
            else:
                answer[i]=False
        return answer

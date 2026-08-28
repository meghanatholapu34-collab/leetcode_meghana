class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        maxi=max(candies)
        for i in range(len(candies)):
            candies[i]=candies[i]+extraCandies
            if candies[i]>=maxi:
                result.append(True)
            else:
                result.append(False)

        return result 

        
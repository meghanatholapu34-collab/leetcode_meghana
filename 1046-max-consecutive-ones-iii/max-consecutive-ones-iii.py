class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        maxl=0
        n=len(nums)
        zeroes=0
        for r in range(0,n):
            
            if nums[r]==0:
                zeroes+=1
            while zeroes>k:
                if nums[l]==0:
                    zeroes-=1
                l+=1
            maxl = max(maxl, r - l + 1)
        return maxl


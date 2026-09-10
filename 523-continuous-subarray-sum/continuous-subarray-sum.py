class Solution(object):
    def checkSubarraySum(self, nums, k):
        ps=0
        hm={0:-1}
        for i,num in enumerate(nums):
            ps+=num
            r=ps%k
            if r in hm:
                if i-hm[r]>=2:
                    return True
            else:
                hm[r]=i
        return False







        
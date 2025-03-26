class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return {i,j}
        return {}
        # d={}
        # for i in range(n):
        #     r=target-nums[i]
        #     if r in d:
        #         return{d[r],i}
        #     d[num[i]]=i
        # return {}


        
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm={}
        max_ = None
        curr_lead = 0
        for n in nums:
            if n not in hm:
                hm[n]=1
            else:
                hm[n]+=1
        for key, val in hm.items():
            if val>curr_lead:
                max_ = key
                curr_lead = val
        return max_
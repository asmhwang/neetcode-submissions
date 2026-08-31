class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_val={}
        for index, num in enumerate(nums):
            c = target - num
            if c in hash_val:
                return [hash_val[c],index]
            hash_val[num]=index
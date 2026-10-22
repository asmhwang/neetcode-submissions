class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_val={}
        for key, val in enumerate(nums):
            search = target - val
            if search in hash_val:
                return [hash_val[search], key]
            hash_val[val] = key
            
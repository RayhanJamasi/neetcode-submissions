class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        verifySet = set(nums)
        if len(verifySet) == len(nums):
            return False
        else:
            return True
        
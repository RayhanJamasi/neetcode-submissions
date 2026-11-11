class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_dict = {}

        for i in range(len(nums)):
            nums_dict[nums[i]] = i
        
        for i in range(len(nums)):  
            needed_value = target - nums[i]

            if needed_value in nums_dict and nums_dict[needed_value] != i:

                if (i < nums_dict.get(needed_value)):
                    return [i, nums_dict.get(needed_value)]
                
                return [nums_dict.get(needed_value), i]


        
        
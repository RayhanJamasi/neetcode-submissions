class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}
        needed_value = 0

        for i in range(len(nums)):

            hash_map[nums[i]] = i

        for i in range(len(nums)):
            needed_value = target - nums[i]

            if (hash_map.get(needed_value, -1) != -1 and 
                hash_map[needed_value] != i):

                return_index = hash_map[needed_value]
                if return_index > i:
                    return_list = [i, return_index]
                else:
                    return_list = [return_indedx, i]

                return return_list



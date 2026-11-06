class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}

        for i in range(len(nums)):
            curr = nums[i]
            if target - curr in dct:
                return [dct[target - curr], i]
            
            dct [curr] = i
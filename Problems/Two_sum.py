class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        o = {}
        for i in range(len(nums)):
            if nums[i] in o:
                return [i, o[nums[i]]]
            o[target - nums[i]] = i

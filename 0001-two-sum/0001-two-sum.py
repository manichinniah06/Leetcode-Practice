class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            temp_target = target - nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == temp_target:
                    return [i,j]
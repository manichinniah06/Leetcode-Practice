class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return_arr = []
        for i in range(len(nums)):
            return_arr.append(sum(nums[:i+1]))
        return return_arr
        
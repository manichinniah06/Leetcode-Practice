class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return_arr = nums + nums[::-1]
        return return_arr
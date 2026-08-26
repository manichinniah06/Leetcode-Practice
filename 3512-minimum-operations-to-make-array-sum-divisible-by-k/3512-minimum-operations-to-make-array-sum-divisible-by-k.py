class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total_sum = sum(nums)
        mod_value = total_sum % k
        return mod_value

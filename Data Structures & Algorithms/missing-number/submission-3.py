class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        actual_sum = (n * (n+1)) // 2
        missing_number = actual_sum - total_sum 
        return missing_number
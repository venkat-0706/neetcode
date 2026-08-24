class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor1 = xor2 = 0 
        for i in range(len(nums)):
            xor2 = xor2 ^ nums[i]
            xor1 = xor1 ^(i+1)
        return xor1^xor2
        
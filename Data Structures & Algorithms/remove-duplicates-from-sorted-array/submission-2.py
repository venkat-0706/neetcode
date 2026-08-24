class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        for i in range(1, len(nums)-1+1):
            if nums[i] != nums[i-1]:
                nums[index] = nums[i]
                index = index + 1 
        return index
        
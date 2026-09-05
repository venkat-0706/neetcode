class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        repeatedNumber = nums[0]

        for i in range(n):
            indexToNavigate = abs(nums[i])

            if nums[indexToNavigate] < 0:
                repeatedNumber = indexToNavigate
                break
            
            nums[indexToNavigate] = -nums[indexToNavigate]
        
        return repeatedNumber
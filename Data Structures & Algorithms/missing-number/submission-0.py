class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n+1):
            flag = 0
            for j in range(n):
                if nums[j] == i :
                    flag = 1 
                    break 
            if flag == 0 : 
                return i  
        
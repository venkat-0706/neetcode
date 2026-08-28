class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0 :
            return 0 
        dp =[0]*n 
        max_left = 0 
        for i in range(n) : 
            max_left =  max(max_left , height[i])
            dp[i] = max_left 
        max_right = 0 
        for i in range(n-1,-1,-1):
            max_right =  max(max_right , height[i])
            dp[i] = min(dp[i], max_right)
        return sum(dp[i] - height[i] for i in range(n)) 

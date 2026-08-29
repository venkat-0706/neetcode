class Solution:
    def findSumOfSquares(self, num: int) -> int:
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total

    def isHappy(self, n: int) -> bool:
        slow, fast = n, n

        while True:

            slow = self.findSumOfSquares(slow)
            fast = self.findSumOfSquares(self.findSumOfSquares(fast))

            if slow == fast:
                return slow == 1
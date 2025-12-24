class Solution:
    def mirrorDistance(self, n: int) -> int:
        num = abs(n)
        reversed_num = 0

        while num != 0:
            digit = num % 10
            reversed_num = (reversed_num * 10) + digit
            num //= 10

        return abs(n - reversed_num)
        
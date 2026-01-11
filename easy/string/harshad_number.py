class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        n = sum(int(n) for n in str(x))

        if x % n == 0:
            return n
        else:
            return - 1
            
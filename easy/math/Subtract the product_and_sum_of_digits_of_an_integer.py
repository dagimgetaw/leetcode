class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num = str(n)
        total_sum, total_product = 0, 1

        for n in num:
            total_sum += int(n)
            total_product *= int(n)

        return total_product - total_sum

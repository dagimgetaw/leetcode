class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        val = 0
        for symbol in operations:
            if symbol == "--X" or symbol == "X--":
                val -= 1
            else:
                val += 1

        return val
        
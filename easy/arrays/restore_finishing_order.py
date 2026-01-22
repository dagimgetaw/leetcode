class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        arr = []
        for n in order:
            if n in friends:
                arr.append(n)

        return arr
        
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        answer1 = 0
        answer2 = 0
        
        for n in nums1:
            if n in set2:
                answer1 += 1
                
        for n in nums2:
            if n in set1:
                answer2 += 1
                
        return [answer1, answer2]

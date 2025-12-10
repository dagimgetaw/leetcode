class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
                  
        sorted_items_by_value = sorted(hashmap.items(), key=lambda item: item[1])[::-1]
        
        arr = []
        for i in range(k):
            arr.append(sorted_items_by_value[i][0])
        
        return arr
        
    
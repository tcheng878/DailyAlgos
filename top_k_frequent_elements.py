class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == len(nums):
            return nums
        
        count = Counter(nums)
        keys = count.keys()
        keys.sort(key = lambda x: count[x], reverse = True)
        return keys[:k]
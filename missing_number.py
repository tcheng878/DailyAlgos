class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 and nums[0] == 0:
            return 1
        elif len(nums) == 1 and nums[0] == 1:
            return 0
        elif 0 not in nums:
            return 0
        
        Sum = 0
        for i in nums:
            Sum += i
        
        total = 0
        Max = max(nums)
        for i in range(Max + 1):
            total += i
            
        if Sum == total:
            return Max + 1
        return total - Sum
        
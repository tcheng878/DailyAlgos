class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        small=1
        large=1
        maxi=float('-inf')
        for i in range(len(nums)):
            small = min(nums[i],small*nums[i],large*nums[i])
            large = max(nums[i],small*nums[i],large*nums[i])
            maxi = max(maxi,small,large)
        return maxi
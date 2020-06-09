class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        dic = {0:1}
        summ = 0
        for n in nums:
            summ += n
            diff = summ - k
            if diff in dic:
                res += dic[diff]
            if summ in dic:
                dic[summ] += 1
            else:
                dic[summ] = 1
        return res
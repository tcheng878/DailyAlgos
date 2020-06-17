class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        output = [0] * (num + 1) 
        for i in range(num + 1):
            output[i] = (str(bin(i)).count("1"))
        return output
            
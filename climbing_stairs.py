class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dic = {}
        def climb(intt, dic):
            var1 = var2 = 0
            if intt == 1:
                return 1
            elif intt == 2:
                return 2
            if (intt - 1) in dic: var1 = dic[intt - 1]
            else:
                var1 = climb(intt - 1, dic)
                dic[intt - 1] = var1
            if (intt - 2) in dic: var2 = dic[intt - 2]
            else:
                var2 = climb(intt - 2, dic)
                dic[intt - 2] = var2
            return var1 + var2
            
        temp = climb(n, dic)
        print(dic)
        return temp
    
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        pastnums = {}
        new = 0
        
        while(n != 1):
            if n in pastnums:
                return False
            pastnums[n] = 0
            strn = str(n)
            for i in range(len(strn)):
                new += int(strn[i]) ** 2
            n = new
            new = 0
            
        return True
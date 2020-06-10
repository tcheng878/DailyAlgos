class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        
        for i in range(1, n + 1, 1):
            strout = ""
            if i % 3 == 0:
                strout += "Fizz"
            if i % 5 == 0:
                strout += "Buzz"
            if strout == "":
                strout += str(i)
            output.append(strout)
        
        return output
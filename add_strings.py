class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "":
            return num2
        elif num2 == "":
            return num1
        elif num1 == "" and num2 == "":
            return ""
        
        pon1 = len(num1)-1
        pon2 = len(num2)-1
        carry = 0
        output = []
        temp = 0
        
        while(pon1 >= 0 or pon2 >= 0):
            if(pon1 < 0):
                temp = int(num2[pon2]) + carry  
            elif(pon2 < 0):
                temp = int(num1[pon1]) + carry
            else:
                temp = int(num1[pon1]) + int(num2[pon2]) + carry
            
            val = temp % 10
            carry = temp / 10
            output.append(val)
            pon1 -= 1
            pon2 -= 1
            
        if carry == 1:
            output.append(1)
            
        output = output[::-1]
        strout = ""
        
        for i in output:
            strout += str(i)
        
        return strout
        
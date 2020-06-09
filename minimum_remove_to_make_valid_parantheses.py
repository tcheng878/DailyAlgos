class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = 0
        balance = 0
        l = []
        r = []
        
        for i in s:
            if i == "(":
                balance += 1
                l.append(par(count, balance, i))
            elif i == ")":
                balance -= 1
                if(balance < 0):
                    s = s[:count] + s[count+1:]
                    count -= 1
                    balance += 1
                else:
                    r.append(par(count, balance, i))
            count += 1
            
        if balance > 0:
            for i in range(0, balance, 1):
                try:
                    s = s[:l[len(l) - i - 1].count] + s[l[len(l) - i - 1].count+1:]
                except:
                    s = s[:l[len(l) - i - 1].count]
                    
        elif balance < 0:
            for i in range(0, -balance, 1):
                s = s[:r[i].count] + s[r[i].count+1:]
                
        return s
            
class par(object):
    def __init__(self, count, balance, val):
        self.count = count
        self.balance = balance
        self.val = val
            
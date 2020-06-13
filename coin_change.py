class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        def recurse(value, count):
            minn = -1
            if value == amount:
                return count
            elif value > amount:
                return -1
            else:
                for i in coins:
                    value += i
                    count += 1
                    temp = recurse(value, count)
                    if (temp < minn or minn == -1) and temp != -1:
                        minn = temp
                    value -= i
                    count -= 1
                return minn
        
        if len(coins) > 0:
            output = recurse(0, 0)
        return output
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lis = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.lis) == 0 or num >= self.lis[-1]:
            self.lis.append(num)
        elif num < self.lis[0]:
            self.lis.insert(0, num)
        else: 
            for i in range(len(self.lis)):
                if num >= self.lis[i] and num <= self.lis[i + 1]:
                    self.lis.insert(i + 1, num) 

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.lis) == 0:
            return 0
        rem = len(self.lis) % 2
        rempoint = len(self.lis) / 2
        if rem == 0:
            return ((self.lis[rempoint] + self.lis[rempoint - 1]) * 0.5)
        else:
            return self.lis[rempoint]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
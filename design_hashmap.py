class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lis = []

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        temp = [key, value]
        flag = False
        for i in range(len(self.lis)):
            if self.lis[i][0] == temp[0]:
                self.lis[i][1] = temp[1]
                flag = True
                break
        if flag == False:
            self.lis.append(temp)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        for i in range(len(self.lis)):
            if self.lis[i][0] == key:
                return self.lis[i][1]
            
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        for i in range(len(self.lis)):
            if self.lis[i][0] == key:
                self.lis.pop(i)
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
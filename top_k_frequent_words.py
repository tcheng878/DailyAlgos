class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        
        """
        dic = {}
        for i in words:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        candidates = dic.keys()
        candidates.sort(key = lambda w: (-dic[w], w))
        return candidates[:k]
        
       

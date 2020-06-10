class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        if len(words) == 1:
            return True
        
        dic = {}
        for i in range(len(order)):
            dic[order[i]] = i
            
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            loc1 = 0
            loc2 = 0
            
            while(loc1 < len(word1) and loc2 < len(word2)):
                if dic[word1[loc1]] > dic[word2[loc2]]:
                    return False
                elif dic[word1[loc1]] == dic[word2[loc2]]:
                    loc1 += 1
                    loc2 += 1
                else:
                    break
            if loc1 < len(word1) and not(loc2 < len(word2)):
                return False
        
        return True
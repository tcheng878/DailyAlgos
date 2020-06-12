class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()
        paragraph = re.sub(r'[^\w\s]',' ',paragraph)
        arr = paragraph.split(" ")
        
        words = {}
        for i in arr:
            if i in words:
                words[i] += 1
            else:
                words[i] = 1
        words[" "] = 0
        words[""] = 0
                
        for i in banned:
            if i in words:
                words[i] = 0
        
        return max(words, key = words.get)
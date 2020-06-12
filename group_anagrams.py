class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        words = {}
        output, out = [], []
        flag = True
        
        while len(strs) != 0:
            currentword = strs.pop(0)
            out.append(currentword)
            words["length"] = len(currentword)
            for i in range(len(currentword)):
                if currentword[i] in words:
                    words[currentword[i]] += 1
                else:
                    words[currentword[i]] = 1
                    
            strclone = strs[:]
            for i in range(len(strclone)):
                wordsclone = words.copy()
                if wordsclone["length"] != len(strclone[i]):
                    break
                for j in range(len(strclone[i])):
                    if strclone[i][j] not in words:
                        flag = False
                        break
                    else:
                        wordsclone[strclone[i][j]] -= 1
                        if wordsclone[strclone[i][j]] < 0:
                            flag = False
                            break
                if flag:
                    out.append(strclone[i])
                    strs.pop(i)
                flag = True
            output.append(out)
            out = []
            words = {}
               
        return output
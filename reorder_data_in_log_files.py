class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        strtemp, alpha, count, output, let, dig = "abcdefghijklmnopqrstuvwxyz", {}, 0, [] * len(logs), [], []
        for i in strtemp:
            alpha[i] = count
            count += 1
            
        count = 0
        for i in logs:
            if i[:2] == "dig":
                if len(let) == 0:
                    let.append(logs[count])
                else:
                    for j in range(len(let)):
                        loc1, loc2, len1, len2 = 5, 5, len(i), len(let[j]) 
                        flag = False
                        while(loc1 < len1 and loc2 < len2):
                            if i[loc1] == let[j][loc2]:
                                loc1 += 1
                                loc2 += 1
                            elif alpha[i[loc1]] < alpha[let[j][loc2]]:
                                flag = True
                                break
                            else:
                                break
                        if loc1 >= len1 and loc2 < len2:
                            flag = True;
                        elif loc1 >= len1 and loc2 >= len2:
                            if(i[3] <= let[j][3]):
                                flag = True;
                        if flag:
                            let.insert[j, logs[count]]
                                    
            elif i[:2] == "let":
                dig.append(logs[count])
            count += 1
            
            count = 0
            for i in let:
                output[count] = i
                count += 1
            for i in dig:
                output[count] = i
                count += 1
                
            return output
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        distances = []
        disbuilder = [0] * 2
        
        for i in points:
            disbuilder[0] = (i[0] * i[0])+(i[1] * i[1])
            disbuilder[1] = [i[0],i[1]]
            if len(distances) == 0:
                distances.append(copy.copy(disbuilder))
            else:
                for i in range(len(distances)):
                    if distances[i][0] > disbuilder[0]:
                        distances.insert(i, copy.copy(disbuilder))
                        break
                    if i == len(distances) - 1:
                        distances.append(copy.copy(disbuilder))
                        break
        
        output = [0] * K
        for i in range(K):
            output[i] = distances[i][1]
            
        return output
       
            
        
        
            
       
            
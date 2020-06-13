class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        flag = False
        loc = 0
        temp = 0
        maxx = 0
        
        for i in range(len(nums) - 1, 0,-1):
            if nums[i] > nums[i - 1]:
                loc = i - 1
                maxx = nums[i - 1]
                flag = True
                break
            else:
                loc = i -1
             
        print(flag)
        if flag == False:
            
            nums.reverse()
            
        else:
            for i in range(len(nums) - 1, 0,-1):
                if nums[i] > maxx:
                    temp = i
                    break
            nums[loc], nums[temp] = nums[temp], nums[loc]

            for i in range(0, (len(nums) - 1 - loc) / 2, 1):
                nums[loc + 1 + i], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[loc + 1 + i]
        
                
            
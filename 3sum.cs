public class Solution {
    public IList<IList<int>> ThreeSum(int[] nums) {
        IList<IList<int>> output = new List<IList<int>>();
        Array.Sort(nums);
        int r = 0;
        int l = 0;
        int i = 0;
        
        while(i < nums.Length - 2){
            l = i + 1;
            r = nums.Length - 1;
            
            while(l < r){
                int calc = nums[i] + nums[l] + nums[r];
                if(calc == 0){
                    IList<int> temp = new List<int>(){nums[i],nums[r],nums[l]};
                    output.Add(temp);
                    while(nums[l] == nums[l + 1]){
                        l++;
                        if(l == nums.Length - 1){
                            break;
                        }
                    }
                    l++;
                    while(nums[r] == nums[r - 1]){
                        r--;
                        if(r == 0){
                            break;
                        }
                    }
                    r--;
                }
                else if(calc > 0){
                    while(nums[r] == nums[r - 1]){
                        r--;
                        if(r == 0){
                            break;
                        }
                    }
                    r--;
                }
                else{ // < 0
                    while(nums[l] == nums[l + 1]){
                        l++;
                        if(l == nums.Length - 1){
                            break;
                        }
                    }
                    l++;
                }
            }
            
            while(nums[i] == nums[i+1]){
                i++;
                if(i == nums.Length - 1){
                            break;
                        }
            }
            i++;
        }
        return output;
        
        
    }
}
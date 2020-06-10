public class Solution {
    public bool IsValid(string s) {
        int par = 0;
        int curl = 0;
        int brak = 0;
        List<int> rec = new List<int>();
        
        if(s == "")
            return true;
        
        for(int i = 0; i < s.Length; i++){
            if(s[i] == '('){
                par++;
                rec.Insert(0, 1);
            }
            else if(s[i] == ')'){
                if(par == 0)
                    return false;
                par--;
                if(rec[0] == 1){
                    rec.RemoveAt(0);
                }
                else
                    return false;
            }
            else if(s[i] == '{'){
                curl++;
                rec.Insert(0, 2);
            }
            else if(s[i] == '}'){
                if(curl == 0)
                    return false;
                curl--;
                if(rec[0] == 2){
                    rec.RemoveAt(0);
                }
                else
                    return false;
            }
            else if(s[i] == '['){
                brak++;   
                rec.Insert(0, 3);
            }
            else if(s[i] == ']'){
                if(brak == 0)
                    return false;
                brak--;
                if(rec[0] == 3){
                    rec.RemoveAt(0);
                }
                else
                    return false;
            }
            // Console.WriteLine(rec[0]);
        }
        if(par != 0 || curl != 0 || brak != 0){
            return false;
        }
        return true;
    }
}
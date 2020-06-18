/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode MergeKLists(ListNode[] lists) {
        ListNode output = new ListNode();
        ListNode runner = new ListNode();
        ListNode input = new ListNode();
        bool flag = false;
        
        // if(lists.Length == 0){
        //     return null;
        // }
        // if(lists.Length == 1 && lists[0] == null){
        //     return null;
        // }
        
        for(int i = 0; i < lists.Length; i++){
            runner = output;
            input = lists[i];
            
            while(input != null){
                if(flag == false){
                    output.val = input.val;
                    input = input.next;
                    flag = true;
                }
                else{
                    if(runner.next != null && input.val >= runner.val){
                        if(runner.next.val >= input.val){
                            ListNode temp = new ListNode(input.val, runner.next);
                            runner.next = temp;
                            input = input.next;
                        }
                        else{
                            runner = runner.next;
                        }
                        // Console.WriteLine("1");
                    }
                    else if(input.val >= runner.val && runner.next == null){
                        runner.next = new ListNode(input.val);
                        input = input.next;
                        // Console.WriteLine("2");
                    }
                    else if(input.val > runner.val){
                        runner = runner.next;
                        // Console.WriteLine("3");
                    }
                    else if(input.val < runner.val){
                        ListNode temp = new ListNode(input.val, output);
                        output = temp;
                        runner = output;
                        input = input.next;
                        // Console.WriteLine("4");
                    }
                }
            }
        }
        if(flag == false)
            return null;
        return output;
    }
}
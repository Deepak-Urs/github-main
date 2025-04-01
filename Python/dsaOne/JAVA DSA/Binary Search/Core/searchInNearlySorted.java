public class searchInNearlySorted {
    public static int searchNearlySorted(int[] nums, int tgt) {
      int st = 0;
      int en = nums.length - 1;

      while(st <= en) {
          int m = st + (en-st)/2;
    
          if(tgt == nums[m]) {
            return m;
          }
          else if(st <= m-1 && tgt == nums[m-1]) {
            return m-1;
          }
          else if(m+1 <= en && tgt == nums[m+1]) {
            return m+1;
          }
          else if(tgt < nums[m]) {
            en = m - 2;
          }
          else {
            st = m + 2;
          }
        }
    
        return -1;
    }

    public static void main(String[] args) {
        int[] nums = {5,10,30,20,40};
        int tgt = 5;
        System.out.println(searchNearlySorted(nums, tgt));
    }
}

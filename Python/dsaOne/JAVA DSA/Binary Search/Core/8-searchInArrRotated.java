public class searchInArrRotated {
    public static int numTimesArrRotated(int[] nums) {
        int st = 0;
        int en = nums.length-1;
        int l = en + 1;

        while(st <= en) {
            int m = st + (en-st)/2;
            int next = (m+l-1)%l;
            int prev = (m+1)%l;

            if(nums[m] <= nums[prev] && nums[m] <= nums[next]) return m;
            else if(nums[en] < nums[m]) st = m + 1;
            else en = m - 1;
        }

        return -1;
    }

    public static int searchArrRotated(int[] nums, int tgt, int st, int en) {
        while(st <= en) {
            int m = st + (en-st)/2;
      
            if(tgt == nums[m]) {
              return m;
            }
            else if(tgt < nums[m]) {
              en = m - 1;
            }
            else if(tgt > nums[m]) {
              st = m + 1;
            }
          }
      
          return -1;
    }

    public static void main(String[] args) {
        int[] nums = {11,12,14,15,16,3,7,8,9};
        int tgt = 7;
        int pt = numTimesArrRotated(nums);
        int s1 = searchArrRotated(nums, tgt, 0, pt-1);
        int s2 = searchArrRotated(nums, tgt, pt, nums.length-1);

        if(s1 == -1 && s2 == -1) System.out.println("-1");
        else if(s1 == -1 && s2 !=-1) System.out.println(s2);
        else System.out.println(s1);
    }
}

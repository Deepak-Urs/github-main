public class numberOfTimesArrRotated {
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

    public static void main(String[] args) {
        int[] nums = {11,12,14,15,16,3,7,8,9};
        System.out.println(numTimesArrRotated(nums));
    }
}

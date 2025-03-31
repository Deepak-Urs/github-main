/*
 * Click `Run` to execute the snippet below!
 */

 import java.io.*;
 import java.util.*;
 
 /*
  * To execute Java, please define "static void main" on a class
  * named Solution.
  *
  * If you need more classes, simply define them inline.
  */
 
 class Solution {
   public static int revBinarySearch(int[] nums, int tgt) {
     int st = 0;
     int en = nums.length-1;
 
     while(st <= en) {
       int m = st + (en-st)/2;
 
       if(tgt == nums[m]) {
         return m;
       }
       else if(tgt < nums[m]) {
         st = m + 1;
       }
       else if(tgt > nums[m]) {
         en = m - 1;
       }
     }
 
     return -1;
   }
 
   public static void main(String[] args) {
     int[] nums = new int[]{6,5,4,3,2,1};
     // int[] nums = new int[]{6,5,4,3,2,1};
     int tgt = 3;
 
     System.out.println(revBinarySearch(nums, tgt));
   }
 }
 
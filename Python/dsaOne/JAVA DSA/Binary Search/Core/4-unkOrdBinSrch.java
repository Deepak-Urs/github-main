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
   public static int unkOrdBinSearch(int[] nums, int tgt) {
     int st = 0;
     int en = nums.length-1;
     boolean isAsc = false;
 
     if(nums[0] < nums[1] && nums[nums.length-2] < nums[nums.length-1]) {
       isAsc = true;
     }
 
     while(st <= en){
       int m = st + (en-st)/2;
 
       if(tgt == nums[m]) {
         return m;
       }
       else if(tgt < nums[m]) {
         if(isAsc) {
           en = m - 1;
         }
         else {
           st = m + 1;
         }
       }
       else {
         if(isAsc) {
           st = m + 1;
         }
         else {
           en = m - 1;
         }
       }
     }
 
     return -1;
 
   }
 
   public static void main(String[] args) {
     // int[] nums = new int[]{6,5,4,3,2,1};
     int[] nums = new int[]{1,2,3,4,5,6};
     int tgt = 33;
 
     // System.out.println(revBinarySearch(nums, tgt));
     System.out.println(unkOrdBinSearch(nums, tgt));
     
   }
 }
 
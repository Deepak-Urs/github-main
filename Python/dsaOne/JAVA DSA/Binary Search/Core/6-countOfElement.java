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
   public static void firstOccAndLastOcc(int[] nums, int tgt) {
     int st = 0;
     int en = nums.length-1;
     int fRes = -1;
     
 
     // first-occurence
     while(st <= en){
       int m = st + (en-st)/2;
 
       if(tgt == nums[m]) {
         fRes = m;
         en = m - 1;
       }
       else if(tgt < nums[m]) {
         en = m - 1;
       }
       else {
         st = m + 1;
       }
     }
     // System.out.println("First Occurance of " +tgt+ "is at index " +res);
 
     st = 0;
     en = nums.length-1;
     int lRes = -1;
 
     // last-occurence
     while(st <= en){
       int m = st + (en-st)/2;
 
       if(tgt == nums[m]) {
         lRes = m;
         st = m + 1;
       }
       else if(tgt < nums[m]) {
         en = m - 1;
       }
       else {
         st = m + 1;
       }
     }
     // System.out.println("First Occurance of " +tgt+ "is at index " +res);
 
     System.out.println("The count of the value " +tgt+ " is " +(lRes-fRes+1) );
     
 
   }
 
   public static void main(String[] args) {
     // int[] nums = new int[]{6,5,4,3,2,1};
     int[] nums = new int[]{1,2,3,4,4,4,4,5,6};
     int tgt = 4;
 
     // System.out.println(revBinarySearch(nums, tgt));
     firstOccAndLastOcc(nums, tgt);
     
   }
 }
 
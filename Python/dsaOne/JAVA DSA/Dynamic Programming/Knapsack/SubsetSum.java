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
   public static boolean subsetSum(int[] Wt, int W, int n, boolean[][] T) {
 
     for (int i = 1; i < n + 1; i++) {
         for (int j = 1; j < W + 1; j++) {
             if (Wt[i - 1] <= j) {
                 // Check if we can form the sum either by not including the current item
                 // or by including the current item (using items 0 to i-1)
                 T[i][j] = T[i - 1][j] || T[i - 1][j - Wt[i - 1]];
             } else {
                 T[i][j] = T[i - 1][j];
             }
         }
     }
     return T[n][W];
 }
 
 
   public static void main(String[] args) {
     int[] Wt = {1, 3, 4, 5};
     // int[] Vl = {2, 7, 5, 7};
     int W = 12;
     int n = Wt.length;
 
     boolean[][] T = new boolean[n+1][W+1];
     for(int ix = 0; ix < n+1; ix++) {
       for(int jx = 0; jx < W+1; jx++) {
         if(ix == 0) {
           T[ix][jx] = false;
         }
         else if(jx == 0) {
           T[ix][jx] = true;
         }
       }
     }
 
     System.out.println(subsetSum(Wt, W, n, T));
   }
 }
 
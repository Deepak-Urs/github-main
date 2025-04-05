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
   public static int ZOKPTabulation(int[] Wt, int[] Vl, int W, int n, int[][] T) {
     if(n == 0 || W == 0) {
       return 0;
     }
 
     for(int i = 1; i < n+1; i++) {
       for(int j = 1; j < W+1; j++) {
         if(Wt[i-1] <= j) {
           T[i][j] = Math.max(Vl[i-1]+T[i-1][j-Wt[i-1]], T[i-1][j]);
         }
         else if(Wt[i-1] > j) {
           T[i][j] = T[i-1][j];
         }
       }
     }
 
     return T[n][W];
   }
 
 
   public static void main(String[] args) {
     int[] Wt = {1, 3, 4, 5};
     int[] Vl = {2, 7, 5, 7};
     int W = 10;
     int n = Wt.length;
 
     int[][] T = new int[Wt.length+1][W+1];
     for(int ix = 0; ix < n+1; ix++) {
       for(int jx = 0; jx < W+1; jx++) {
         if(ix == 0 || jx == 0) {
           T[ix][jx] = 0;
         }
       }
     }
 
     System.out.println(ZOKPTabulation(Wt, Vl, W, n, T));
   }
 }
 
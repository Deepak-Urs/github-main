//package JAVA DSA.Dynamic Programming.Knapsack;

public class ZOKnapsack {
    
    public static int solveKnapsack(int[] wt, int[] val, int W, int n, int V) {
        if(W == 0 || n == 0) {
            return 0;
        }

        if(wt[n-1] <= W) {
            V = Math.max(val[n-1]+solveKnapsack(wt, val, W-wt[n-1], n-1, V), solveKnapsack(wt, val, W, n-1, V));
        }
        else if(wt[n-1] > W) {
            V = solveKnapsack(wt, val, W, n-1, V);
        }

        return V;
    }

    public static void main(String[] args) {
        int wt[] = {1,3,4,5};
        int val[] = {2,4,5,7};
        int W = 10;
        int V = 0;

        System.out.println(solveKnapsack(wt, val, W, wt.length, V));
    }
}

public class ZOKPMemoization {

    public static int solveKnapsack(int[] wt, int[] val, int W, int n, int[][] mn) {
        if (n == 0 || W == 0) {
            return 0;
        }

        if (mn[n][W] != -1) {  // ✅ Corrected index from [n-1][W] to [n][W]
            return mn[n][W];
        }

        if (wt[n - 1] <= W) {
            mn[n][W] = Math.max(
                val[n - 1] + solveKnapsack(wt, val, W - wt[n - 1], n - 1, mn),
                solveKnapsack(wt, val, W, n - 1, mn)
            );
        } else {
            mn[n][W] = solveKnapsack(wt, val, W, n - 1, mn);
        }

        return mn[n][W];
    }

    public static void main(String[] args) {
        int[] wt = {1, 3, 4, 5};
        int[] val = {2, 4, 5, 7};
        int W = 10;

        // ✅ Memoization table should be [n+1][W+1]
        int[][] mn = new int[wt.length + 1][W + 1];

        for (int i = 0; i <= wt.length; i++) {
            for (int j = 0; j <= W; j++) {
                mn[i][j] = -1;
            }
        }

        System.out.println(solveKnapsack(wt, val, W, wt.length, mn));
    }
}

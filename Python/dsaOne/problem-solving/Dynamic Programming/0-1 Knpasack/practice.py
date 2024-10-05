## Zero One Knapsack (Basic Recursion way)
#def z_o_knapsack(Wt, Vl, W, n):
#    # v = 0

#    if W == 0 or n == 0:
#        return 0
    
#    if Wt[n-1] <= W:
#        return max((Vl[n-1] + z_o_knapsack(Wt, Vl, W-Wt[n-1], n-1)), z_o_knapsack(Wt, Vl, W, n-1) )

#    elif Wt[n-1] > W:
#        return z_o_knapsack(Wt, Vl, W, n-1)
    
#    # return v


#Wt = [1,3,4,5]
#Vl = [2,4,5,7]
#W = 10
#n = len(Wt)
#print(z_o_knapsack(Wt, Vl, W, n))
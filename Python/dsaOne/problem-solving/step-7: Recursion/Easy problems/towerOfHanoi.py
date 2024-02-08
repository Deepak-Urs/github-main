#def toh(n):
#    s, h, d = 1,2,3
#    count = 0
#    print("Steps of solving TOH for", n, "discs")
#    solve(n, s, h, d, count)
#    print("Steps of solving TOH for", n, "discs:", count)
#    return 0

#def solve(n, s, h, d, count):
#    if n == 0:
#        return
#    count += 1
#    solve(n-1, s, h, d, count)
#    print("Moving disc", n, "from plate ", s, " to", d)
#    solve(n-1, h, d, s, count)

#print(toh(3))
def TowerOfHanoi(n, from_rod, to_rod, aux_rod): 
    if n == 0: 
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod) 
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod) 
  
  
# Driver code 
N = 3
  
# A, C, B are the name of rods 
TowerOfHanoi(N, 'A', 'C', 'B') 
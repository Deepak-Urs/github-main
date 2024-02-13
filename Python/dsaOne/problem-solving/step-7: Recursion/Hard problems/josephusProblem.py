def solve(v, k, index):
    if len(v) == 1:
        print(v[0])
        return
    
    index = (index+k) % len(v)
    v.pop(index)
    solve(v, k, index)

    return

def main():
    n = int(input("Enter n :\t"))
    k = int(input("Enter k :\t"))
    v = [i for i in range(1, n+1)]
    index = 0
    
    solve(v, k-1, index)

main()
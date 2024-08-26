def print1toN(n):
    #B
    if n == 1:
        print(n)
        return
    #H
    print1toN(n-1)
    #I
    print(n)

print1toN(7)
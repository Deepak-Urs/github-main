def print1toN(i, n):
    if i == n+1:
        return
    print(i)
    print1toN(i+1, n)

print1toN(1, 4)
    
def print1toN(num):
    if num == 1:
        print(1)
        return
    print1toN(num-1)
    print(num)

print1toN(7)
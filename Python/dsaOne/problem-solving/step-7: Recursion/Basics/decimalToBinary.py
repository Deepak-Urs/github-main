def dtb(num):
    if num == 0:
        return 0
    
    return num%2 + 10 * dtb(int(num/2))

print(dtb(10))
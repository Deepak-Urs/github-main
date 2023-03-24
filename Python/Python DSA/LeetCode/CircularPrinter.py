def circularPrinter(str):
    ans = 0
    curr = 0

    for i in range(len(str)):
        k = ord(str[i]) - 97

        a = abs(curr - k)
        b = 26 - abs(curr - k)

        ans += min(a,b)

        curr = k
    
    print(ans)

circularPrinter('zjpc')
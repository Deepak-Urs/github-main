def getMinSum(sec_val, msg):
    li = []

    for x in msg:
        ind = ord(x) - ord("a")
        val = sec_val[ind]
        li.append(val)

    print('li seen', li)
    li.sort()
    

    res = 0
    for i in range(len(li)-1):
        res = res + (li[i+1] - li[i])

    return res

print(getMinSum([1,2,1,3,1,3,5,7,1,1], 'afeb'))

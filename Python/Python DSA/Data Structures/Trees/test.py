def findMaxVal(prices, pos, amount):
    result = []
    for i in range(len(pos)):
        curpos = pos[i] - 1
        curamt = amount[i]
        count = 0
        print(curpos, curamt)
        while(curamt > 0 and curpos < len(prices)):
            if curamt >= prices[curpos]:
                count += 1
                curamt -= prices[curpos]
                curpos += 1
            # print('while-', curamt, curpos)
        result.append(count)
    return result

findMaxVal([1,2,3,4,5], [1,3], [4,14])
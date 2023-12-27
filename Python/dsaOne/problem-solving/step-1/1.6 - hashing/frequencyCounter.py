def frequencyCounter(arr):
    hm = {}
    for i in arr:
        if i in hm:
            hm[i] += 1
        else:
            hm[i] = 1
    
    print(hm)

frequencyCounter([10,5,10,15,10,5])
frequencyCounter([2,2,3,4,4,2])
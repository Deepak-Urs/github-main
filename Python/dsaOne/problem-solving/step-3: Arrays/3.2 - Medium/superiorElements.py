def superiorElements(a):
    # Write your code here.
    l = len(a)-1
    p = a[-1]
    lmx = -1
    
    for i in range(l, -1, -1):
        if a[i] >= p and a[i] > lmx:
            print(a[i])
            lmx = a[i]

#superiorElements([1,2,3,4])
superiorElements([4, 7, 1, 0])
#superiorElements([10, 22, 12, 3, 0, 6])


def binSearch(arr, st, en, t):
    while st <= en:
        m = st + (en-st)//2

        if t == arr[m]:
            return m
        elif t < arr[m]:
            en = m - 1
        else:
            st = m + 1

def findEleInfSortArr(arr, t):
    # assuming we do not know the size of the sorted infinite sized array
    st = 0
    en = 1

    while t >= arr[en]:
        st = en
        en *= 2

    print(binSearch(arr, st, en, t))
    
    # worst case scenario -> value does not exist and we run into infinite computations

# assume arr = [1,2,3,4,5,6,7,8,9,............]
arr = [1,2,3,4,5,6,7,8,9]
findEleInfSortArr(arr, 6)   
            

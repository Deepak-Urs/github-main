## brute force method
#def firstNegNumWindowArr(arr, ws):
#    i = 0
#    j = i

#    for i in range(len(arr)-ws+1):
#        for j in range(i, i+ws):
#            if arr[j] < 0:
#                print(arr[j])
#                break
#            if arr[j] > 0 and j == i+ws-1:
#                print(0)

#firstNegNumWindowArr([12, -1, -7, 8, -15, 30, 16, 28], 3)

def firstNegNumWindowArr(arr, ws):
    i = 0
    j = 0
    size = len(arr)
    nn = []

    while j < size:
        if arr[j] < 0:
            nn.append(arr[j])

        if j-i+1 < ws:
            j += 1

        elif j-i+1 == ws:
            if len(nn) == 0:
                print(0)
            else:
                print(nn[0])            
                if arr[i] == nn[0]:
                    nn.pop(0)
                      
            i += 1
            j += 1

firstNegNumWindowArr([12, -1, -7, 8, -15, 30, 16, 28], 3)
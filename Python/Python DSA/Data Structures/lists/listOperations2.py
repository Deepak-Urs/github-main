# concatenation
a = [1,2,3]
b = [4,5,6]

c = a + b
# print(c)

# replication
ar = [0,1]
ar = ar * 4
# print(a)
# print(len(a))
# print(max(b))
# print(min(a))
# print(sum(ar))
# print('average', sum(b)/len(b))

def avgCal():
    rA = []
    while (True):
        inp = input('Enter a number')
        if inp == 'done': 
            print(calcAvg(rA))
            break
        else:
            rA.append(float(inp))

def calcAvg(arr):
    return 'Average:' + str((sum(arr)/len(arr)))

avgCal()

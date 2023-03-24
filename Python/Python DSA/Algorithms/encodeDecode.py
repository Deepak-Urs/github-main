# class Solution:
def encode(arr):
    idxStr = ""
    for s in arr:
        idxStr += str(len(arr)) + "#" + s
        print('idxStr seen', idxStr)
    return idxStr

def decode(str):
    print('i/p str:', str)
    res, i = [], 0

    while i < len(str):
        j = i
        while str[j] != "#":
            j += 1
        length = int(str[i:j])
        res.append(str[j + 1: j + 1 + length])
        print('res seen after pushing', res)
        i = j + 1 + length
    return res

# inst = Solution()
resStr = encode(['lint','code','love','you'])
print(decode(resStr))
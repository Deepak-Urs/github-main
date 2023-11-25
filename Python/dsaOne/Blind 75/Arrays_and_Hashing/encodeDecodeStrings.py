#https://leetcode.com/problems/encode-and-decode-strings/

#class EncodeDecode:
def encode(sA):
    st = ''
    for i in sA:
        st += str(len(i)) + '#' + i
    return st

def decode(s):
    res = []
    l = 0
    while(l < len(s)-1):
        r = l
        while(s[r] != '#'):
            r += 1
        length = int(s[l:r])
        rs = s[r+1: r+1+length]
        res.append(rs)
        l = r + 1 + length
    return res
    
##ed = EncodeDecode()
#r1 = ed.encode(["Hello","World"])
#print(ed.decode(r1))

r1 = encode(["Hello","World"])
print(decode(r1))
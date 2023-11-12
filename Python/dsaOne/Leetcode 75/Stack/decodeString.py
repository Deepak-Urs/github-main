#https://leetcode.com/problems/decode-string/?envType=study-plan-v2&envId=leetcode-75

def decodeString(s):
    num = 0
    res = ''
    st = []

    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == '[':
            st.append(res)
            st.append(num)
            res = ''
            num = 0
        elif c == ']':
            pnum = st.pop()
            pstr = st.pop()
            res = pstr + pnum*res
        else:
            res += c

    return res

print(decodeString("3[a]2[bc]"))
print(decodeString("3[a2[c]]"))
print(decodeString("2[abc]3[cd]ef"))
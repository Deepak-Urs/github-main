def getJsonDiff(json1, json2):
    l1 = json1.split(",")
    l2 = json2.split(",")

    print('l1 after , split:', l1)
    print('l2 after , split:', l2)

    di1 = {}
    di2 = {}

    for x in l1:
        x = x.replace("{", "")
        val = x.split(":")
        di1[val[0]] = val[1]


    for y in l2:
        y = y.replace('{', "")
        val = y.split(":")
        di2[val[0]] = val[1]

    print('d1 after:', di1)
    print('d2 after:', di2)

    result = []

    for key in di1:
        if key in di2:
            if di1[key] != di2[key]:
                result.append(key[1:len(key)-1])
    
    result.sort()
    return result




json1 = "{'hacker':'rank','input':'output'}"
json2 = "{'hacker':'ranked','input':'wrong'}"
print(getJsonDiff(json1, json2))
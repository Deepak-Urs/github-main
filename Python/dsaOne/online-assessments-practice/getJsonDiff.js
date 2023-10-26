const getJsonDiff = (json1, json2) => {
    l1 = json1.split(",")
    l2 = json2.split(",")

    let myMap1 = new Map()
    let myMap2 = new Map()

    for(let i = 0; i < l1.length; i++) {
        l1[i] = l1[i].replace("{", "")
        let val = l1[i].split(":")
        myMap1.set(val[0], val[1])
    }

    for(let i = 0; i < l2.length; i++) {
        l2[i] = l2[i].replace("{", "")
        let val = l2[i].split(":")
        myMap2.set(val[0], val[1])
    }

    let res = []
    myMap1.forEach((v, k) => {
        if(myMap1.get(k) != myMap2.get(k)) {
            res.push(k.slice(1, k.length-1))
        }
    })

    res.sort((a, b) => a - b)
    return res
}


json1 = "{'hacker':'rank','input':'output'}"
json2 = "{'hacker':'ranked','input':'wrong'}"
console.log(getJsonDiff(json1, json2))
const groupAnagrams = (strings) => {
    let hm = new Map()
    let res = []

    for(let i = 0; i < strings.length; i++) {
        let key = strings[i].split('').sort().join('')
        
        if(hm.has(key)) {
            let temp = hm.get(key)
            temp.push(strings[i])
            hm.set(key, temp)
        }
        else {
            hm.set(key, [strings[i]])
        }
    }

    hm.forEach(function (v,k) {
        res.push(v)
    })

    return res

}


console.log(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
console.log(groupAnagrams([""]))
console.log(groupAnagrams(["a"]))
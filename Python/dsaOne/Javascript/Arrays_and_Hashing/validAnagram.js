//https://leetcode.com/problems/valid-anagram/

const validAnagram = (s, t) => {
    let hm1 = {}
    let hm2 = {}

    for(let i = 0; i < s.length; i++) {
        if(hm1[i] && hm1[i].includes(s[i])){
            hm1[s[i]] += 1
        }
        else {
            hm1[s[i]] = 1
        }
    }

    for(let j = 0; j < t.length; j++) {
        if(hm2[j] && hm2[j].includes(s[j])){
            hm2[t[j]] += 1
        }
        else {
            hm2[t[j]] = 1
        }
    }

    let k1 = Object.keys(hm1)
    let k2 = Object.keys(hm2)

    if(k1.length !== k2.length) {
        return false
    } 
    else {
        for(const k in hm1) {
            if(hm1[k] !== hm2[k]){
                return false
            }
        }
    }

    return true
}

console.log(validAnagram('anagram', 'nagaram'))
console.log(validAnagram('malayalam', 'malayalam'))
console.log(validAnagram('potato', 'tomato'))
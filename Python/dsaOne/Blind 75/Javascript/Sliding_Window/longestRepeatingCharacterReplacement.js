// https://leetcode.com/problems/longest-repeating-character-replacement/description/

const longestRepeatingCharacterReplacement = (s, k) => {
    let myMap = new Map()
    let l = 0
    let res = 0

    for(let r = 0; r < s.length; r++) {
        let len = r - l + 1
        myMap.set(s[r], 1 + (myMap.get(s[r]) || 0))
        
        if(len - Math.max(...myMap.values()) > k) {
            myMap.set(s[l], myMap.get(s[l])-1)
            l++
        }

        len = r - l + 1
        res = Math.max(len, res)
    }

    return res
}

console.log(longestRepeatingCharacterReplacement("ABAB", 2))
console.log(longestRepeatingCharacterReplacement("AABABBA", 1))
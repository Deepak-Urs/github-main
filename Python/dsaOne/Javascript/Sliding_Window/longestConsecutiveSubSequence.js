const longestConsecutiveSequence = (s) => {
    let set = new Set()
    let l = 0
    let maxRes = 0

    for(let r = 0; r < s.length; r++) {
        while(set.has(s[r])) {
            set.delete(s[l])
            l++
        }
        set.add(s[r])
        maxRes = Math.max(maxRes, (r-l)+1)
    }

    return maxRes
}

console.log(longestConsecutiveSequence('abcabcbb'))
console.log(longestConsecutiveSequence('bbbbbb'))
console.log(longestConsecutiveSequence('pwwkepw'))
//https://leetcode.com/problems/valid-palindrome/description/

const validPalindrome = (s) => {
    let strFil = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase()
    let l = 0
    let r = strFil.length - 1

    while(l < r) {
        if(strFil[l] == strFil[r]) {
            l++;
            r--;
        }
        else {
            return false
        }
    }

    return true
}

console.log(validPalindrome("A man, a plan, a canal: Panama"))
console.log(validPalindrome("0P"))
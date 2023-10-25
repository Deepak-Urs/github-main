const validParanthesis = (s) => {
    let stack = []
    const map = {
        '}': '{',
        ')': '(',
        ']': '['
    }

    for(const char of s) {
        const isEndBracket = (char in map)
        if(!isEndBracket) {
            stack.push(char)
            continue
        }

        const isEqual = (stack[stack.length-1] === map[char])
        if(isEqual) {
            stack.pop()
            continue
        }

        return false
    }

    return (stack.length == 0)
}

console.log(validParanthesis('()[]{}'))
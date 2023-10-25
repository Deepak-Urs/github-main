var stack = []
// 1. push operation
stack.push('google')
stack.push('ig')
stack.push('yt')

// 2. pop operation
console.log(stack.pop())
stack.push('amazon')

// 3. shift operation
console.log(stack.shift())

// 4. unshift operation()
console.log(stack.unshift('first company'))
console.log(stack)
class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

class Stack{
    constructor() {
        this.first = null;
        this.last = null;
        this.size = 0;
    }

    push(val) {
         let newNode = new Node(val)

         if(this.size == 0){
            this.first = newNode
            this.last = newNode
         } else{
            let temp = this.first
            this.first = newNode
            this.first.next = temp
        }

        return ++this.size;
    }

    pop() {
        if(!this.size) return null

        let temp = this.first

        if(this.first == this.last) {
            this.last = null
        }
        this.first = this.first.next
        
        --this.size;
        return `popped val--${temp.val}`
    }
}


let stack = new Stack()
stack.push(1)
stack.push(2)
stack.push(3)
console.log(stack.pop())
console.log(stack.pop())
console.log(stack.pop())
console.log(stack.pop())
console.log(stack)


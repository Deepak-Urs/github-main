class Node {
    constructor(val) {
        this.val = val
        this.next = null
    }
}

class SinglyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0
    }

    push(val) {
        let newNode = new Node(val)

        if(this.length == 0) {
            this.head = newNode
            this.tail = newNode
        }
        else {
            this.tail.next = newNode
            this.tail = newNode
        }

        this.length++;

        return this
    }

    traverse() {
        if(this.length == 0) console.log("Linked List Empty!")
        let curr = this.head
        while(curr) {
            console.log(curr)
            curr = curr.next
        }
    }

    pop() {
        if(this.length == 0) {
            return undefined
        }

        let curr = this.head
        while(curr.next.next !== null) {
            curr = curr.next
        }

        curr.next = null
        this.tail = curr
        this.tail.next = null
        this.length--;

        if(this.length == 0) {
            this.head = null;
            this.tail = null;
        }
        return curr
    }

    shift() {
        if(this.length == 0) return undefined

        let curr = this.head
        curr = curr.next;
        this.head = curr;
        this.length--;

        if(this.length == 0) {
            this.head = null;
            this.tail = null;
        }

        return curr
    }

    get(idx) {
        if(idx < 0 || idx > this.length) return undefined

        let curr = this.head
        let c = 0
        while(c !== idx) {
            curr = curr.next
            c++
        }
        return curr
    }

    set(idx, val) {
        let getNode = this.get(idx)

        if(getNode == null || getNode == undefined) {
            return false
        }

        getNode.val = val
        return true
    }

    insert(idx, val) {
        let getNode = this.get(idx-1)

        
        if(getNode) {
            let newNode = new Node(val)
            newNode.next = getNode.next
            getNode.next = newNode
            this.length++
        }
        else {
            return undefined
        }

        if(this.length == 0) {
            this.head = null;
            this.tail = null
        }

        return this
    }

    remove(idx){
        let getNode = this.get(idx-1)
        let delNode;

        if(getNode){
            delNode = getNode.next
            getNode.next = delNode.next
            this.length--
        } else {
            return undefined
        }

        if(this.length == 0) {
            this.head = null;
            this.tail = null
        }

        return delNode
    }

    reverse() {
        var node = this.head
        this.head = this.tail
        this.tail = node
        let next;
        let prev = null;

        console.log('node seen', node)
        //for(let i = 0; i < this.length; i++) {
        //    ne
        //}
    }
    print() {
        let arr = []
        let curr = this.head
        while(curr) {
            arr.push(curr.val)
            curr = curr.next
        }
        console.log(arr)
    }
    reverse() {
        let node = this.head
        this.head = this.tail
        this.tail = node
        let next;
        let prev;

        for(let i = 0; i < this.length; i++) {
            next = node.next
            node.next = prev
            prev = node
            node = next
        }

        return this
    }
}

//let first = new Node('hello')
//first.next = new Node('world!')
//first.next.next = new Node('how')
//first.next.next.next = new Node('are')
//first.next.next.next.next = new Node('you?')


let first = new SinglyLinkedList()
first.push('hello')
first.push('world!')
first.push('how')
first.push('are')
first.push('you?')

//first.pop()
//first.pop()
//first.shift()
//first.shift()
//first.shift()
//first.shift()
first.set(2, 'updated')
console.log(first.get(2))
first.insert(3, 'doing')
first.insert(4, 'four')
first.remove(3)
first.traverse()
//console.log(first)
first.reverse()
first.print()

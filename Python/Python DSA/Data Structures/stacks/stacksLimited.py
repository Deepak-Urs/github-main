class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
    
    # Push
    def push(self,value):
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(value)
            return 'Value added is successful'

    # Pop
    def pop(self):
        if self.isEmpty():
            return 'The stack is empty'
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            return self.list[len(self.list)-1]
    
    def delete(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            self.list = None


newStack = Stack(3)
print(newStack.isEmpty())
print(newStack.isFull())
print(newStack.push(10))
print(newStack.push(20))
print(newStack.push(30))
print('-', newStack.pop())

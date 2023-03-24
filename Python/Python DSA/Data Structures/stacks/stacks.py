# STACKS - using LISTS

class Stack:
    #stack creation
    def __init__(self):
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

    # push
    def push(self, value):
        self.list.append(value)
        return 'Value added successful'

    # pop
    def pop(self):
        if self.isEmpty():
            print("the stack is empty!")
        else:
            return self.list.pop()

    # peek
    def peek(self):
        if self.isEmpty():
            print("the stack is empty")
        else:
            return self.list[len(self.list)-1]
    
    # delete
    def delete(self):
        if self.isEmpty():
            print("the stack is empty")
        else:
            self.list = None

    
newStack = Stack()
print(newStack.isEmpty())

print(newStack.push(1))
print(newStack.push(2))
print(newStack.push(3))
#print(newStack)

#print('-', newStack.pop())


print('peep', newStack.peek())
print(newStack)



    
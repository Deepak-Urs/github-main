class minElementStackWithExtraSpace:
    def __init__(self):
        self.stk = []
        self.minStk = []

    def getMin(self):
        if len(self.minStk) == 0: return -1
        return self.minStk[-1]
    
    def push(self, a):
        self.stk.append(a)
        if len(self.minStk) == 0 or a <= self.minStk[-1]: 
            self.minStk.append(a)
    
    def pop(self):
        if len(self.minStk) == 0: return -1
        popV = self.stk.pop()
        if self.minStk[-1] == popV:
            self.minStk.pop()

mESWES = minElementStackWithExtraSpace()
mESWES.push(18)
mESWES.push(19)
print(mESWES.getMin())
mESWES.push(29)
mESWES.push(15)
print(mESWES.getMin())
mESWES.push(15)
mESWES.pop()
print(mESWES.getMin())


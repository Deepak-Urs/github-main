class minElementStackWithNoExtraSpace:
    def __init__(self) -> None:
        self.stk = []
        self.minVal = -1

    def getMinVal(self):
        if len(self.stk) == 0: return -1
        return self.minVal
    
    def push(self, a):
        if len(self.stk) == 0:
            self.stk.append(a)
            self.minVal = a
        elif len(self.stk) > 0:
            if a >= self.minVal:
                self.stk.append(a)
            elif a < self.minVal:
                self.stk.append(2*a - self.minVal)
                self.minVal = a
    
    def pop(self):
        if len(self.stk) == 0: return -1
        elif len(self.stk) > 0:
            if self.minVal <= self.stk[-1]:
                self.stk.pop()
            elif self.minVal > self.stk[-1]:
                self.minVal = 2*self.minVal - self.stk[-1]
                self.stk.pop()

    def top(self):
        if len(self.stk) == 0: return -1
        elif len(self.stk) > 0:
            if self.stk[-1] >= self.minVal:
                return self.stk[-1]
            else:
                return self.minVal
            
mESWES = minElementStackWithNoExtraSpace()
mESWES.push(18)
mESWES.push(19)
print(mESWES.getMin())
mESWES.push(29)
mESWES.push(15)
print(mESWES.getMin())
mESWES.push(15)
mESWES.pop()
print(mESWES.getMin())
print(mESWES.top())


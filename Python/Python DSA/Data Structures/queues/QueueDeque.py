from collections import deque

customQ = deque(maxlen=3)
print(customQ)

customQ.append(1)
customQ.append(2)
customQ.append(3)
customQ.append(4)
print(customQ)

print(customQ.popleft())
print(customQ)

print(customQ.clear())
print(customQ)
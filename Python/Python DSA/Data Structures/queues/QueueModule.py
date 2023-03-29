import queue as q

customQM = q.Queue(maxsize=3)
print(customQM.empty())
customQM.put(1)
customQM.put(2)
customQM.put(3)
print(customQM.qsize())
print(customQM.full())
print(customQM.get())
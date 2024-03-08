import queue

L = queue.Queue(maxsize=5)

L.put(5)

print(L.qsize())

L.put(1)
L.put(7)
L.put(9)
L.put(4)

print(L.qsize())

print(L.full())

print(L.get())
print(L.get())
print(L.get())

print(L.full())
print(L.qsize())

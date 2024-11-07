#priority queue
import queue
q = queue.PriorityQueue()
q.put(10)
q.put(60)
q.put(36)
print("item in priority order:")
while not q.empty():
   print(q.get())
#queue using modules
import collections
queue = collections.deque()
queue.append(10)
queue.append(50)
queue.append(70)
print(queue)
queue.popleft()
print(queue)
#insert left
queue.appendleft(60)
queue.appendleft(80)
queue.appendleft(30)
print(queue)
queue.pop()
print(queue)




#stack using deque
import collections
stack = collections.deque()
stack.append(10)
stack.append(63)
stack.append(56)
print (stack)
if not stack:
    print("stack is empty")
else:
    stack.pop()
    print(stack)





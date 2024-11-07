queue =[]
def enqueue():
    el = int(input("Enter your element"))
    queue.append(el)
    print(queue)
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        queue.pop(0)
def show():
    print(queue)

while True:
    print("select the option 1.push 2.pop 3.show 4.quit")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        show()
    elif choice == 4:
        break
    else:
        print("Enter the correct option")


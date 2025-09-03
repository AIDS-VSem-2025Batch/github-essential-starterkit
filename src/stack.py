class Stack:
    def __init__(self):
        self.item=[]
    def push(self,item):
        self.item.append(item)
    def pop(self):
        return self.item.pop() if self.item else None

stck=[]
obj=Stack()
obj.push(3)
obj.push(4)
print("popped "+str(obj.pop())+" from stack")


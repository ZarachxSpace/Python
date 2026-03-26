class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")


    def peek(self):
        if len(self.stack) > 0:
            stack_peek = self.stack[-1]
        else: 
            raise IndexError("Stack is empty")
        
        return stack_peek

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return(len(self.stack))




s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.peek())    # 30
print(s.pop())     # 30
print(s.pop())     # 20
print(s.size())    # 1
print(s.is_empty()) # False
print(s.pop())     # 10
print(s.is_empty()) # True

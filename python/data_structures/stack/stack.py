class Stack(object):
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    # Printing stack
    def __str__(self):
        return ' '.join([str(i) for i in self.stack])

    # Push element to stack
    def push(self, data):
        if len(self.stack) >= self.limit:
            print('Stack Overflow')
        else:
            self.stack.append(data)

    # Remove topmost element
    def pop(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack.pop()

    # Get top-most element
    def peek(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack[len(self.stack) - 1]

    def isEmpty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)


stack = Stack()
for i in range(10):
    stack.push(i)
print(stack)
# Remove top element
stack.pop()
print(stack)
# Get the top element
print(stack.peek())
print(stack.isEmpty())
print(stack.size())

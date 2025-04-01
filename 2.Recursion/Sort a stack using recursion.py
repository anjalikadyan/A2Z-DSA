class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)

def sorted_insert(stack, element):
    if stack.is_empty() or element > stack.peek():
        stack.push(element)
    else:
        temp = stack.pop()
        sorted_insert(stack, element)
        stack.push(temp)

def sort_stack(stack):
    if not stack.is_empty():
        temp = stack.pop()
        sort_stack(stack)
        sorted_insert(stack, temp)

if __name__ == "__main__":
    s = Stack()
    s.push(3)
    s.push(1)
    s.push(4)
    s.push(2)
    s.push(5)
    
    print("Original Stack:", s)
    sort_stack(s)
    print("Sorted Stack:", s)
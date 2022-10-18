class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, numb):
        self.stack.append(numb)

    def pop(self):
        if self.size() > 0:
            self.stack = self.stack[:-1]

    def top(self):
        answer = None
        if self.size() > 0:
            answer = self.stack[-1]
        return answer

    def size(self):
        return len(self.stack)
    
    def get_stack(self):
        return self.stack
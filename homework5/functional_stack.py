def initialize_stack():
    return []

def push(stack, numb):
    stack.append(numb)
    return stack

def pop(stack):
    stack = stack if size(stack) == 0 else stack[:-1]
    return stack

def top(stack):
    return None if size(stack) == 0 else stack[-1]

def size(stack):
    return len(stack)
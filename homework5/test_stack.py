import pytest
import functional_stack
from oop_stack import Stack


def test_functional_init():
    stack = functional_stack.initialize_stack()
    assert stack == []

def test_functional_push_and_top():
    stack = functional_stack.initialize_stack()
    assert functional_stack.top(stack) is None
    stack = functional_stack.push(stack, 1)
    assert functional_stack.top(stack) == 1
    stack = functional_stack.push(stack, 2)
    assert functional_stack.top(stack) == 2

def test_functional_pop_and_size():
    stack = functional_stack.initialize_stack()
    assert functional_stack.size(stack) == 0
    stack = functional_stack.pop(stack)
    assert functional_stack.size(stack) == 0
    stack = functional_stack.push(stack, 1)
    stack = functional_stack.pop(stack)
    assert functional_stack.size(stack) == 0
    stack = functional_stack.push(stack, 1)
    stack = functional_stack.push(stack, 2)
    assert functional_stack.size(stack) == 2
    stack = functional_stack.pop(stack)
    assert functional_stack.top(stack) == 1
    assert functional_stack.size(stack) == 1
    stack = functional_stack.pop(stack)
    assert functional_stack.size(stack) == 0
    assert stack == []

def test_oop_init():
    stack = Stack()
    assert stack.get_stack() == []

def test_oop_push_and_top():
    stack = Stack()
    assert stack.top() is None
    stack.push(1)
    assert stack.top() == 1
    stack.push(2)
    assert stack.top() == 2

def test_oop_pop_and_size():
    stack = Stack()
    assert stack.size() == 0
    stack.pop()
    assert stack.size() == 0
    stack.push(1)
    stack.pop()
    assert stack.size() == 0
    stack.push(1)
    stack.push(2)
    assert stack.size() == 2
    stack.pop()
    assert stack.top() == 1
    assert stack.size() == 1
    stack.pop()
    assert stack.size() == 0
    assert stack.get_stack() == []

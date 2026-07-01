"""
Write a code for implementing a stack in python that can handle max of 10 elements
"""

class MyStack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.top = 0
        self.stack = [None]*self.capacity

    def push(self, item):
        # check the stack is full or not
        if self.top == self.capacity:
            raise Exception('Stack is full!')
        else:
            self.stack[self.top] = item
            self.top += 1

    def pop(self):
        # check the stack is empty or not
        if self.top == 0:
            raise Exception('Stack is empty!')
        else:
            item = self.stack[self.top-1]
            self.stack[self.top-1] = None
            self.top -= 1
            return item
# concept of LIFO(last in first out)
'''
operations
1. push
2. pop
3.peep: to give/tell the top most element in the stack without deleting it from stack.
4. search: to tell element position from top of stack, len(lst) - index(element)'''

class Stack(object):

    def __init__(self): # constructor.
        self.st = []

    def isempty(self):
         return self.st == []

    def push(self, val):
        self.st.append(val)

    def pop(self):
        if self.isempty():
            print('stack is empty.')
        else:
            self.st.pop()

    def peep(self):
        if self.isempty():
            print('stack is empty.')
        else:
            print(f'top most element of stack : {self.st[-1]}')

    def search(self):
        val = input('enter element to be searched: ')
        if self.isempty():
            print('stack is empty.')
        else:
            print(f'searched from top of stack {len(self.st)-self.st.index(val)}')

    def show(self):
        return self.st
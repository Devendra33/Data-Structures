'''Operation FIFO(first in first out)
1.add(): from rear
2.delete(): from front
3.search: from front side.
4.exit()
'''
class Queue(object):
    def __init__(self):
        self.que = []

    def isempty(self):
        return self.que == []

    def add(self, val):
        self.que.append(val)

    def delete(self):
        if self.isempty():
            print('stack is empty.')
        else:
            self.que.pop(0)
            print('element deleted successfully...')

    def search(self, val):
        if self.isempty():
            print('stack is empty.')
        else:
            try:
                print( f'element searched at {(self.que.index(val) + 1)} index')
            except ValueError:
                print('element not found....')
    def show(self):
        return self.que

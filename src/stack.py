
class Stack(object):

    def __init__(self):
        self.stack = []


    def add(self, data):
        """Use list 'append' method to add element."""
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False


    def remove(self):
        """Use list 'pop' method to remove element."""
        if len(self.stack) <= 0:
            return 'No elements in the Stack'
        else:
          return self.stack.pop()


    def peek(self):
        """Use peek to look at the top of the stack."""
        return self.stack[0]

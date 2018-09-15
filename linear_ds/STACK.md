# Stack (LIFO)

In the english dictionary the work **stack** means arranging objects on over another. It is the same way memory is allocated in this data structure. The stack data structure allows operations at one end which can be called the top of the stack. We can add or remove elements only from this end of the stack.

In a stack the element inserted last, it will also be the first element out.

### PUSH into a Stack
```
class Stack:
    def __init__(self):
        self.stack = []

    def add(self, data):
        """Use list append method to add element."""
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False

    def peek(self):
        """Use peek to look at the top of the stack."""
        return self.stack[0]
```

### POP from the Stack
As we know we can remove only the top most data element from the stack.
```
class Stack:
    def __init__(self):
        self.stack = []

    def add(self, data):
        """Use list append method to add element."""
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False

    def remove(self):
        """."""
        if len(self.stack) <= 0:
            return 'No elements in the Stack'
        else:
          return self.stack.pop()
```

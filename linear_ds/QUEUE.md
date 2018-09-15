# Queue (FIFO)

The queue data structure is an abstract data structure, somewhat similar to Stacks. Unlike stacks, a queue is open at both its ends. One end is always used to insert (enqueue) data and the other is used to remove (dequeue) data.

**Queue** follows the First-In-First-out (FIFO) methodology, i.e., the data item stored first will be accessed first.

#### Adding Elements to a Queue
We use the built-in insert method for adding data elements.
```
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        """Insert method to add element."""
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        return False

    def size(self):
        """Return the size of the current queue."""
        return len(self.queue)
```

#### Removing Element from a Queue

```
class Queue:
    def __init__(self):
        self.queue = list()

    def enqueue(self, data):
        """Insert method to add element."""
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        return False

    def enqueue(self):
        """Pop method to remove element."""
        if len(self.queue) > 0:
            return self.queue.pop()
        return 'No elements in Queue!'
```

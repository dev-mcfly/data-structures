
class Queue(object):

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


    def size(self):
        """Return the size of the current queue."""
        return len(self.queue)

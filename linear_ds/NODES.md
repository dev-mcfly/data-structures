# Nodes in Python

There are situations when the allocation of memory to store the data cannot be in a continuous block of memory. We take help of pointers, where we store both the data and the address of the location to the next element. We know the address of the next data element from the values of the current data element.
`In general these structures are know as pointers, but in python we refer to them as nodes.`

Nodes are the foundations on which various other data structures (i.e. linked lists and trees) are built on .

### Creation of Nodes
Nodes are created by implementing a class which holds both the data and pointers.

In the example below we create a class named `DayNames` to hold the names of the weekdays. The `next` pointer is initialized to None.
```
class DayNames:
    def __init__(self, data=None):
        self.data = data
        self.next = None

e1 = DayNames('Mon')
e2 = DayNames('Tue')
e3 = DayNames('Wed')

e1.next = e2 # set e1 to point at e2
e2.next = e3 # set e2 to point at e3
```

### Traversing the Node Elements
We can traverse the elements of the node created above by creating a variable and assigning the first element to it. Then use a while loop and the next pointer to print out all the connected node elements.

```
class DayNames:
    def __init__(self, data=None):
        self.data = data
        self.next = None

e1 = DayNames('Mon')
e2 = DayNames('Tue')
e3 = DayNames('Wed')
e4 = DayNames('Thu')

root = e1

while root:
  print(root.val) # prints out 'Mon' 'Tue' 'Wed' 'Thu'
  root = root.next
```

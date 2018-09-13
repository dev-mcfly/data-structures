# Singly Linked List

A linked list is a sequence of data elements that are connected via links. Each data element contains a connection to another data element using a pointer.

We implement the concept of linked lists using the concept of nodes. We have already seen how to create a node and how to traverse the elements of a node. In this type of data structure there is one link between any two data elements.

### Creation of Linked List
We create a Node object and create another class to use this node object.
```
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head =  None

lst1 = SinglyLinkedList()
lst1.head = Node('Mon')
e2 = Node('Tue')
e3 = Node('Wed')

# Link 1st node and 2nd node
lst1.head.next = e2

# Link 2nd node to 3rd node
e2.next = e3
```

### Traversing a Linked List
Singly Linked List can only be traversed in a forward direction, starting from the first node.
```
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head =  None

    def traverse_list(self):
        root = self.head
        while root is not None:
            print(root.val)
            root = root.next
```

### Insertion in a Linked List
Inserting elements in the linked list involves reassigning the pointers from existing nodes to the newly inserted node. Depending on whether the new element is getting inserted at the beginning, middle, or end of the linked list.

#### Inserting at the Beginning of the Linked List
This involves pointing the next pointer of the new node to the current head of the linked list. So the current head of the linked list becomes the second element and the new node becomes the head.
```
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head =  None

    def insert(self, new_data):
        new_node = Node(new_data)

        # Update the new nodes next pointer to existing head
        new_node.next = self.head
        self.head = new_node
```

#### Inserting at the End of the Linked List
This involves pointing the next pointer of the current last node of linked list to the new node. So the current last node of the linked list becomes the second last node and new node becomes the last node of the linked list.
```
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head =  None

    def insert_at_end(self, new_data):
        new_node = Node(new_data)

        # Check if there ll is empty
        if self.head is None:
            self.head = new_node
            return

        # Find the last node in ll
        last = self.head
        while last.next:
            last = last.next

        # Attach the last elements next pointer to the new node
        last.next = new_node

```

#### Inserting in between two nodes
This involves changing the pointer of a specific node to point to the new node. That is possible by passing in both the new node and the existing node, afterwards the new node will be inserted. We define an additional class which will change the next pointer of the new node to the next pointer of the middle node, then assign the new node to the pointer of the middle node.
```
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head =  None

    def insert_in_between(self, middle_node, new_data):
        # Raise exception if the middle node is not None
        if middle_node is None:
            raise Exception('Given node can not be None.')

        new_node = Node(new_data)
        new_node.next = middle_node.next
        middle_node.next = new_node
```

#### Removing an Item from a Linked List
We can remove an existing node using the key for that node. First we locate the previous node of the node which is to be deleted, then point the next pointer of this node to the next node of the node to be deleted.

```
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head =  None

    def remove(self, remove_val):
        cur = self.head

        # Check if the value we are removing is the head
        if cur is not None:
            if cur.val == remove_val:
                self.head = cur.next
                cur = None
                return

        # Traverse the ll
        while cur is not None:
            # If we found the correct value break loop
            if cur.val == remove_val:
                break
            prev = cur
            cur = cur.next

        # Check if we have traversed the entire ll and not found the value
        if cur == None:
            return

        # Set prev pointer to cur.next
        prev.next = cur.next

        # Set cur to None (not needed since python has garbage collection)
        cur = None
```

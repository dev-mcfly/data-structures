
class Node(object):

    def __init__(self, val=None):
        self.val = val
        self.next = None


class SinglyLinkedList(object):

    def __init__(self):
        self.head =  None


    def traverse_list(self):
        """."""
        root = self.head
        while root is not None:
            print(root.val)
            root = root.next


    def insert(self, new_data):
        """."""
        new_node = Node(new_data)

        # Update the new nodes next pointer to existing head
        new_node.next = self.head
        self.head = new_node


    def insert_at_end(self, new_data):
        """."""
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


    def insert_in_between(self, middle_node, new_data):
        """."""
        # Raise exception if the middle node is not None
        if middle_node is None:
            raise Exception('Given node can not be None.')

        new_node = Node(new_data)
        new_node.next = middle_node.next
        middle_node.next = new_node


    def remove(self, remove_val):
        """."""
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

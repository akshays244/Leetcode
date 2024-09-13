# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data  # Holds the value of the node
        self.next = None  # Points to the next node, initially None

# Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # Start with an empty list

    # Append a new node at the end
    def append(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If the list is empty, set the new node as head
        else:
            last = self.head
            while last.next:  # Traverse to the last node
                last = last.next
            last.next = new_node  # Add the new node at the end

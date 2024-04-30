class Node:
    """
    A class representing a node in a singly linked list.
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the data attribute.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Sets the data attribute.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        Gets the next_node attribute.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next_node attribute.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """
    A class representing a singly linked list.
    """

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self._head = None

    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        result = []
        current = self._head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        Inserts a new node with the given value into the list in sorted order.
        """
        new_node = Node(value)

        if self._head is None or self._head.data >= value:
            new_node.next_node = self._head
            self._head = new_node
            return

        current = self._head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

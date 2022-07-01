from nodes import *

class CreateSerial:
    def __init__(self, root: str, *nodes: str) -> None:
        self._node = ListNode(root)
        self._head = self._node

        for node in nodes:
            new_node = ListNode(node)
            self._node.next = new_node
            self._node = self._node.next

    def create(self) -> ListNode:
        return self._head

class Serial:
    def __init__(self, serial: ListNode):
        self._serial: ListNode = serial
        self._current_level = 0
        self._node_position = ""
        self._node_level = 0

    def deserialize(self) -> TreeNode:
        if self._serial != None:
            tree = TreeNode(self._serial.value)

            self._deserialize_string(tree)

            return tree
        else:
            return None

    def _deserialize_string(self, node: TreeNode) -> None:
        self._serial = self._serial.next

        if self._serial == None:
            return None

        serial_value_splitted = self._serial.value.split(".")
        self._node_position = serial_value_splitted[-1] # Get node position
        self._node_level = len(serial_value_splitted) # Get node level

        # Wrong level !!! Backtracking...
        if self._node_level <= self._current_level:
            self._current_level -= 1
            return None

        # If left child node...
        if (self._node_level == (self._current_level + 1)) and "left" == self._node_position:
            node.left = TreeNode(self._serial.value)
            self._current_level = self._node_level
            self._deserialize_string(node.left)

        # If right child node...
        if (self._node_level == (self._current_level + 1)) and "right" == self._node_position:
            node.right = TreeNode(self._serial.value)
            self._current_level = self._node_level
            self._deserialize_string(node.right)

        self._current_level -= 1

class Tree:
    def __init__(self, root: TreeNode):
        self._root: TreeNode = root

    def serialize(self) -> ListNode:
        self._serial: ListNode = None

        if self._root != None:
            self._serial = ListNode(self._root.value)
            root_node = self._serial

            self._serialize_nodes(self._root)

            return root_node
        else:
            return None

    def _serialize_nodes(self, node: TreeNode) -> None:
        if node.left != None:
            self._serial.next = ListNode(node.left.value)
            self._serial = self._serial.next
            self._serialize_nodes(node.left)

        if node.right != None:
            self._serial.next = ListNode(node.right.value)
            self._serial = self._serial.next
            self._serialize_nodes(node.right)

        return None

from node import *


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
        self._serial = self._serial.next()

        if self._serial == None:
            return None

        self._node_position = self._get_node_position(self._serial.value)
        self._node_level = self._get_node_level(self._serial.value)

        if self._wrong_level():
            return self._backtrack()

        if self._is_left_child():
            node.add_left_child(TreeNode(self._serial.value))
            self._current_level = self._node_level
            self._deserialize_string(node.left)

        if self._is_right_child():
            node.add_right_child(TreeNode(self._serial.value))
            self._current_level = self._node_level
            self._deserialize_string(node.right)

        self._current_level -= 1

    def _backtrack(self):
        self._current_level -= 1
        return None

    def _wrong_level(self):
        if self._node_level <= self._current_level:
            return True
        else:
            return False

    def _is_left_child(self):
        if (
            self._node_level == (self._current_level + 1)
        ) and "left" == self._node_position:
            return True

    def _is_right_child(self):
        if (
            self._node_level == (self._current_level + 1)
        ) and "right" == self._node_position:
            return True

    def _get_node_position(self, list_node: ListNode) -> str:
        return list_node.split(".")[-1]

    def _get_node_level(self, list_node: ListNode) -> str:
        return len(list_node.split("."))


class Tree:
    def __init__(self, root: TreeNode):
        self._root: TreeNode = root

    def serialize(self) -> ListNode:
        self._serial: ListNode = None

        if self._root != None:
            self._serial = ListNode(self._root.value)
            root_node = self._serial

            self._serialize_node(self._root)

            return root_node
        else:
            return None

    def _serialize_node(self, node: TreeNode) -> None:
        if node.has_left_child():
            self._serial = self._serial.append(node.left.value)
            self._serialize_node(node.left)

        if node.has_right_child():
            self._serial = self._serial.append(node.right.value)
            self._serialize_node(node.right)

        return None

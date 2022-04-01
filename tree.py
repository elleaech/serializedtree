from node import *


class Tree:
    def __init__(self, root: TreeNode):
        self._tree: TreeNode = root
        self._string: ListNode = None

        self._current_level = 0
        self._node_position = ""
        self._node_level = 0

    def serialize(self) -> ListNode:
        if self._tree != None:
            self._string = ListNode(self._tree.value)
            root_node = self._string

            self._serialize_node(self._tree)

            self._shift_structure(None, root_node)
            return root_node
        else:
            return self._string

    def _shift_structure(self, node: TreeNode, string: ListNode):
        self._string = string
        self._tree = node

    def _serialize_node(self, node: TreeNode) -> None:
        if node.has_left_child():
            self._string = self._string.append(node.left.value)
            self._serialize_node(node.left)

        if node.has_right_child():
            self._string = self._string.append(node.right.value)
            self._serialize_node(node.right)

        return None

    def deserialize(self) -> TreeNode:
        if self._string != None:
            tree = TreeNode(self._string.value)

            self._deserialize_string(tree)
            self._shift_structure(tree, None)

            return tree
        else:
            return self._tree

    def _deserialize_string(self, node: TreeNode) -> None:
        self._string = self._string.next()
        if self._string == None:
            return None

        self._node_position = self._get_node_position(self._string.value)
        self._node_level = self._get_node_level(self._string.value)

        if self._node_level <= self._current_level:
            self._current_level -= 1
            return None

        if (
            self._node_level == (self._current_level + 1)
        ) and "left" == self._node_position:
            node.add_left_child(TreeNode(self._string.value))
            self._current_level = self._node_level
            self._deserialize_string(node.left)
        if (
            self._node_level == (self._current_level + 1)
        ) and "right" == self._node_position:
            node.add_right_child(TreeNode(self._string.value))
            self._current_level = self._node_level
            self._deserialize_string(node.right)

        self._current_level -= 1

    def _get_node_position(self, list_node: ListNode) -> str:
        return list_node.split(".")[-1]

    def _get_node_level(self, list_node: ListNode) -> str:
        return len(list_node.split("."))

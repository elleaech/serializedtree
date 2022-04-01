from node import *


class Tree:
    def __init__(self, root: TreeNode):
        self._tree: TreeNode = root
        self._string: ListNode = None
        self._node_level = 0
        self._last_node_level = 0

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

            self._last_node_level = 1
            return tree
        else:
            return self._tree

    def _deserialize_string(self, node: TreeNode) -> None:
        self._string = self._string.next()
        if self._string == None:
            return None

        position = self._get_node_position(self._string.value)
        if "left" == position:
            node.add_left_child(TreeNode(self._string.value))
            self._last_node_level = self._node_level
            self._deserialize_string(node.left)
        elif "right" == position:
            node.add_right_child(TreeNode(self._string.value))
            self._last_node_level = self._node_level
            self._deserialize_string(node.right)
        elif position == "full":
            self._last_node_level -= 1
            return None

        if self._string == None:
            return None

        position = self._get_node_position(self._string.value)
        if "right" == position:
            node.add_right_child(TreeNode(self._string.value))
            self._last_node_level = self._node_level
            self._deserialize_string(node.right)
        elif "left" == position:
            node.add_left_child(TreeNode(self._string.value))
            self._last_node_level = self._node_level
            self._deserialize_string(node.left)
        elif position == "full":
            self._last_node_level -= 1
            return None

    def _get_node_position(self, list_node: ListNode) -> str:
        value = list_node.split(".")
        value_len = len(value)
        self._node_level = value_len

        if self._node_level > self._last_node_level:
            return value[-1]
        else:
            return "full"

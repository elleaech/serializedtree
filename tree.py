from node import *


class Tree:
    def __init__(self, root: TreeNode):
        self._tree = root
        self._string = None

    def serialize(self) -> list:
        string = list()

        if self._tree != None:
            string.append(self._tree)
            self._serialize_node(self._tree, string)
            self._shift_structure(None, string)
            return string
        else:
            return self._string

    def _shift_structure(self, node: TreeNode, string: list):
        self._string = string
        self._tree = node

    def _serialize_node(self, node: TreeNode, string: list) -> None:
        if node.has_left_child():
            string.append(node.left)
            self._serialize_node(node.left, string)

        if node.has_right_child():
            string.append(node.right)
            self._serialize_node(node.right, string)

        return None

    def deserialize(self) -> TreeNode:
        tree = TreeNode("root", None, None)

        if self._string != None:
            self._deserialize_node(tree, self._string)
            self._shift_structure(tree, None)
            return tree
        else:
            return self._string

    def _deserialize_node(self, node: TreeNode, stringNode: list) -> None:
        if stringNode.next() != None:
            position = self._get_node_position(stringNode.next().value)
            if "left" == position:
                node.add_left_child(stringNode)
                self._deserialize_node(node.left, stringNode)
            if "right" == position:
                node.add_right_child(stringNode)
                self._deserialize_node(node.right, stringNode)
            if "leaf" == position:
                return None

        self._deserialize_node(node, stringNode)

from node import *
from tree import Tree
from sys import exit


def main() -> int:
    root_node = TreeNode(
        "root", TreeNode("left", TreeNode("left.left")), TreeNode("right")
    )

    tree = Tree(root_node)
    node = tree.serialize()

    while node != None:
        print(node.value)
        node = node.next()

    assert tree.deserialize().left.left.value == "left.left"

    return 0


if __name__ == "__main__":
    exit(main())

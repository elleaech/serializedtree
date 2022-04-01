from node import *
from tree import Tree
from sys import exit


def main() -> int:
    root_node = TreeNode(
        "root", TreeNode("left", TreeNode("left.left")), TreeNode("right")
    )

    tree = Tree(root_node)

    # for nodes in tree.serialize():
    #    print(nodes.value)

    # print(tree.serialize())
    # print(tree.serialize())

    # print(tree.deserialize())
    # print(tree.deserialize())
    # print(tree.deserialize())

    # assert tree.deserialize(tree.serialize(node)).left.left.val == "left.left"

    return 0


if __name__ == "__main__":
    exit(main())

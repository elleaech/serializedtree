from node import *
from tree import *
from sys import exit


def main() -> int:
    tree = Tree(
        TreeNode(
            "root", TreeNode("left", left=TreeNode("left.left")), TreeNode("right")
        )
    )
    serial_tree = tree.serialize()

    serial = Serial(serial_tree)
    assert serial.deserialize().left.left.value == "left.left"

    return 0


if __name__ == "__main__":
    exit(main())

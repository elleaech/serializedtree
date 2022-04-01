from node import *
from tree import Tree
from sys import exit


def main() -> int:
    tree = Tree(
        TreeNode(
            "root", TreeNode("left", left=TreeNode("left.left")), TreeNode("right")
        )
    )
    node = tree.serialize()
    new_tree = tree.deserialize()

    tree = Tree(
        TreeNode(
            "root", TreeNode("left", right=TreeNode("left.right")), TreeNode("right")
        )
    )
    node = tree.serialize()
    new_tree = tree.deserialize()

    tree = Tree(
        TreeNode(
            "root",
            TreeNode("left", right=TreeNode("left.right")),
            TreeNode("right", left=TreeNode("right.left")),
        )
    )
    node = tree.serialize()
    new_tree = tree.deserialize()

    tree = Tree(
        TreeNode(
            "root",
            TreeNode("left", left=TreeNode("left.left")),
            TreeNode("right", right=TreeNode("right.right")),
        )
    )
    node = tree.serialize()
    new_tree = tree.deserialize()

    tree = Tree(
        TreeNode(
            "root",
            TreeNode("left", right=TreeNode("left.right")),
            TreeNode("right", right=TreeNode("right.right")),
        )
    )
    node = tree.serialize()
    new_tree = tree.deserialize()

    tree = Tree(TreeNode("root", TreeNode("left"), TreeNode("right")))
    node = tree.serialize()
    new_tree = tree.deserialize()

    return 0


if __name__ == "__main__":
    exit(main())

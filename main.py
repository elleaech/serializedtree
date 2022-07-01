from nodes import *
from interfaces import *
from sys import exit

def main() -> int:
    original_serial = Serial(CreateSerial("root", "left", "left.left", "right").create())

    tree = Tree(original_serial.deserialize())
    assert tree.serialize().next.next.value == "left.left"

    return 0


if __name__ == "__main__":
    exit(main())

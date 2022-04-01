class TreeNode:
    def __init__(self, val, left=None, right=None):
        self._val = val
        self._left = left
        self._right = right

    def has_left_child(self):
        return self._left != None

    def add_left_child(self, left):
        self._left = left

    def has_right_child(self):
        return self._right != None

    def add_right_child(self, right):
        self._right = right

    @property
    def value(self):
        return self._val

    @property
    def right(self):
        return self._right

    @property
    def left(self):
        return self._left

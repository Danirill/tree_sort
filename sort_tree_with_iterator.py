class Counter:
    count = 0
    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1

class node():
    iterations = 0
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val, counter):
        counter.increase()
        if self.val:
            if val <= self.val:
                if self.left is None:
                    self.left = node(val)
                else:
                    self.left.insert(val, counter)
            elif val > self.val:
                if self.right is None:
                    self.right = node(val)
                else:
                    self.right.insert(val, counter)
        else:
            self.val = val


def inorder(root, res, counter):
    counter.increase()
    if root:
        inorder(root.left, res, counter)
        res.append(root.val)
        inorder(root.right, res, counter)

def treesort_with_iterations(arr):
    counter = Counter()
    if len(arr) == 0:
        return arr, counter.count
    root = node(arr[0])
    for i in range(1, len(arr)):
        root.insert(arr[i], counter)
    res = []
    inorder(root, res, counter)
    return res, counter.count

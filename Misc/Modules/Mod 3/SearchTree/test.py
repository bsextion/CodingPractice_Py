# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
	return traverse(tree, [], 0)

def traverse(curr, arr, idx):
	if curr:
		traverse(curr.left, arr, idx)
        arr.append(curr.value)
        if len(arr) > 1:
			if arr[idx] > arr[idx+1]:
				idx += 1
				return False
        traverse(curr.right, arr, idx)
        return True
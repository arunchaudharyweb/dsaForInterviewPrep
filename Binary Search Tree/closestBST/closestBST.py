# Average: O(logn) time , O(logn) space
# Worst: O(n) time, O(n) space

def findClosestValueInBst(tree, target):
	return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):
	if tree is None:
		return closest
	if abs(target - closest) > abs(target - tree.value):
		closest = tree.value
	if target < tree.value:
		return findClosestValueInBstHelper(tree.left, target, closest)
	elif target > tree.value:
		return findClosestValueInBstHelper(tree.right, target, closest)
	else:
		return closest

	

# Average: O(logn) time , O(1) space
# Worst: O(n) time, O(1) space

# def findClosestValueInBst(tree, target):
# 	return findClosestValueInBstHelper(tree, target, float("inf"))

# def findClosestValueInBstHelper(tree, target, closest):
# 	if tree is None:
# 		return closest
# 	if abs(target - closest) > abs(target - tree.value):
# 		closest = tree.value
# 	if target < tree.value:
# 		return findClosestValueInBstHelper(tree.left, target, closest)
# 	elif target > tree.value:
# 		return findClosestValueInBstHelper(tree.right, target, closest)
# 	else:
# 		return closest


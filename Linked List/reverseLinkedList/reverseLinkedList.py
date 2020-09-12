# O(n) time | O(1) space where n is the total no. of nodes in the linked list.
def reverseLinkedList(head):
	previousNode, currentNode = None, head
	while currentNode is not None:
		nextNode = currentNode.next
		currentNode.next = previousNode
		previousNode = currentNode
		currentNode = nextNode
	return previousNode

class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext


class UnorderedList:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return

	def add(self, item):
		temp = Node(item)
		temp.setNext(head)
		self.head = temp

	def size(self):
		current = self.head 
		count = 0
		while current != None:
			count = count + 1
			current = self.getNext()
		return count
		
	def search(self, entry):
		current = self.head
		found = False
		while(current != None and not found):
			if (current.getData() == item):
				found = True
			else:
				current = current.getNext()
		return found
		
	def remove(self, entry):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == entry:
				found = True
			else:
				current = previous
				current = current.getNext()	



var1 = UnorderedList()
var = Node(23)
print var.getData()
print var.getNext()


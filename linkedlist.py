
class Node:
	def __init__(self, item):
		self.data = item
		self.next = None

	def getvalue(self):
		return self.data

	def getnext(self):
		return self.next

	def setvalue(self, item):
		self.data = item
					
	def setnext(self, nextval):
		self.next = nextval


class Unorderedlist:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item)
		temp.setnext(self.head)		
		self.head = temp

	def size(self):
		count = 0 
		current = self.head
		while current != None:
			current = current.getnext()
			count +=1
		return count	

	def search(self, item):
		current = self.head
		found = False
		while not found and current != None:
			if current.getvalue() == item:
				found = True
			else:
				current = current.getnext()

		return found	 	

	def remove(self,item):

		current = self.head
		previous = None
		found = False

		while not found:
			if current.getvalue() == item:
				found = True
			else:
				previous = current
				current = current.getnext()

		if previous == None:
			self.head = current.getnext()
		else:
			previous.setnext(current.getnext())


	def printlist(self):
		current = self.head
		list1 = []
		while current != None:
			list1.append(current.data)	
			current = current.getnext()
		return list1	

	def reverse(self):
		current = self.head
		previous = None
		next = None

		while current != None:
			next = current.getnext()
			current.setnext(previous)
			previous = current
			current = next
		self.head = previous
		return self.printlist()
		

mylist = Unorderedlist()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))
mylist.add(100)
print(mylist.search(100))
print(mylist.size())
mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))
print mylist.printlist()
print mylist.reverse()
#print mylist.printlist()


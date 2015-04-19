"""
Implementing a queue
"""

class queue:
	def __init__(self):
		self.items = []

	def isempty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)	

	def peek(self):
        return self.items[len(self.items)-1]		


q = queue()

q.enqueue(3)
q.enqueue('piss')
q.enqueue('goatpiss')
q.enqueue('hpiss')

print (q.isempty())
print (q.size())
print q.peek()
q.dequeue()
q.dequeue()






class stack:

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return(len(self.items) == 0)

	def push(self,data):
		self.items.append(data)

	def pop(self):
		return self.items.pop()	

	def peek(self):
		return self.items[-1]	

	def size(self):
		return len(self.items)		






s = stack()
s.push(5)
s.push('dog')
s.push('cat')
print(s.pop())
print(s.isEmpty())
print(s.size())
print(s.peek())







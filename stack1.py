class stack:

	def __init__(self):
		self.items = []

	def isempty(self):
		return self.items == []

	def push(self, data):
		self.items.insert(0, data)	

	def pop(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)


def parcheck(item):
	s = stack()
	var = item.split()
	balanced = True
	for i in var:
		if i in "{[(":
			s.push(i)
		else:
			if s.isempty():
				balanced = False
			else:	
				var2 = s.pop()
				if not matches(var2,i):
					balanced = True

	if s.isempty() and balanced :
		return True
	else:
		return False						

def matches(var2, i):
	return var2 == i

print(parcheck('( ) ('))
print(parcheck('( ( ( ) ) )'))
print(parcheck('( ( )'))	
print(parcheck('{ { ( [ ] [ ] ) } ( ) }'))
print(parcheck('[ { ( ) ]'))	

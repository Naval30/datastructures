class TreeNode:
	def __init__(self, key, value, left=None, right=None, parent=None):
		self.key = key
		self.payload = value
		self.leftchild = left
		self.rightchild = right
		self.parent = parent

	def leftchild(self):
		return self.leftchild

	def rightchild(self):
		return self.rightchild	

	def isleftchild(self):
		return self.parent.leftchild and self.parent

	def isrightchild(self):
		return self.parent.rightchild and self.parent		

	def haschildren(self):
		return self.rightchild or self.leftchild	

	def parent(self):
		return self.parent	

	def isLeaf(self):
		return not (self.rightchild or self.leftchild)	


class BinarySearchTree:
	def __init__(self):
		self.root = None
		self.size = 0

	def length(self):
		return self.size

	def put(self, key, value):
		if self.root = None:	
			self.root = TreeNode(key, value)
		else:	
			self._put(key, value, self.root)

		self.size = self.size + 1
		
	def _put(self, key, value, currentNode):
		if key < currentNode.key:
			if currentNode.leftchild():
				self._put(key, value, currentNode.leftchild)
			else:
				currentNode.leftchild = TreeNode(key, value, parent=currentNode)	 
		else:
			if currentNode.rightchild():
				self._put(key, value, currentNode.rightchild)
			else:
				currentNode.rightchild = TreeNode(key, value, parent=currentNode)				

	def __setitem__(self, key, value):
		self.put(key, value)

	def __getitem__(self, key):
		return self.get(key)

	def get(self, key):
		if self.root:
			res = self._get(key, self.root)
			if res:
				return res.payload
			else:
				return None	
		else:
			return None		

	def _get(self, key, currentNode):
		if not currentNode:
			return None
		elif key == currentNode.key:
			return currentNode
		elif key < currentNode.key:
			return _get(key, currentNode.leftchild)
		else:
			return _get(key, currentNode.rightchild)


	def __delitem__(self, key):
		self.delete(key)

	def delete(self, key):
		if self.size == 1:
			if self.root.key == key:
				self.root = None
				size = size - 1
			else:
				raise Exception("Key not present")

		elif self.size > 1:
			nodetoremove = self._get(key,self.root)	
			if nodetoremove:
				self.remove(nodetoremove)
				self.size = self.size - 1
			else:
				raise Exception("Key not present")


	def remove(self, currentNode):
		if currentNode.isLeaf():
    		if currentNode == currentNode.parent.leftChild:
        		currentNode.parent.leftChild = None
    		else:
        		currentNode.parent.rightChild = None								
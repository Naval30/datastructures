class Hash:
	def __init__(self):
		self.size = 11
		self.data = [None] * self.size
		self.slots = [None] * self.size
	

	def hashfunction(self, key):
		return key%self.size

	def rehashfunction(self,value):
		return (value+1)%self.size


	def put(self, key, item):

		hashvalue = self.hashfunction(key)

		if self.slots[hashvalue] == None:
			self.slots[hashvalue] = key
			self.data[hashvalue] = item

		else:
			if self.slots[hashvalue] == key:
				self.data[hashvalue] = item
			else:
				rehashvalue = self.rehashfunction(hashvalue)	

				while(self.slots[rehashvalue] != None and self.slots[rehashvalue] != key):
					rehashvalue = self.rehashfunction(rehashvalue)	

				if self.slots[rehashvalue] == None:
					self.slots[rehashvalue] = key
					self.data[rehashvalue] = item

				else:
					self.data[rehashvalue] = item



	def fetch(self, key):

		hashvalue = self.hashfunction(key)

		if self.slots[hashvalue] == key:
			return self.data[hashvalue]

		else:
			rehashvalue = self.rehashvalue(hashvalue)
			while(self.slots[rehashvalue]!= key):
				rehashvalue	= self.rehashvalue(hashvalue)

			return self.data[rehashvalue]		



	def __setitem__(self,key, item):
		return self.put(key, item)

		

	def __getitem__(self,key):
		return self.fetch(key)	




h = Hash()
h[0] = "ads"
h[1] = "dog"
h[2] = "gog"
h[3] = "sad"
h[4] = "asd"
h[5] = "sfs"
h[6] = "asf"
h[7] = "saaa"
h[8] = "aff"
h[9] = "sgg"
h[10] = "sfsd"
#h[11] = "sdfs"
#h[12] = "sfdss"
print h[1]


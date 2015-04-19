class hashclass:
	def __init__(self):
		self.size = 11
		self.data = [None] * self.size
		self.slots = [None] * self.size


	def put(self,key,data):
  		hashvalue = self.hashfunction(key,len(self.slots))

  		if self.slots[hashvalue] == None:
  			self.slots[hashvalue] = key
  			self.data[hashvalue] = data
  		else:
  			if self.slots[hashvalue] == key:
  				self.data[hashvalue] = data  
  			else:

  				nextslot = self.rehash(hashvalue,len(self.slots))
  				var = 0
      			while self.slots[nextslot] != None and self.slots[nextslot] != key and var < self.size - 1:
      				nextslot = self.rehash(nextslot,len(self.slots))
      				var += 1

      			if var == self.size -1:
      				return None	

      			if self.slots[nextslot] == None:
        			self.slots[nextslot]=key
        			self.data[nextslot]=data
      			else:
        			self.data[nextslot] = data #replace

	def hashfunction(self,key,size):
		return key%size

	def rehash(self,oldhash,size):
		return (oldhash+1)%size

	def get(self,key):
  		startslot = self.hashfunction(key,len(self.slots))

  		data = None
  		stop = False
  		found = False
  		position = startslot
  		while self.slots[position] != None and not found and not stop:
  			if self.slots[position] == key:
  				found = True
       			data = self.data[position]
     		else:
       			position=self.rehash(position,len(self.slots))
       			if position == startslot:
           			stop = True
  		return data

	def __getitem__(self,key):
		return self.get(key)

	def __setitem__(self,key,data):
		self.put(key,data)

h = hashclass()

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
h[11] = "sdfs"

print h.slots
print h.data

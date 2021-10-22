class SubscriptableSet:
	'''
		Set with the property that elements can be subscripted to.
		
			- Note: Order is not guaranteed
	'''

	def __init__(self, values=None):
		self.position, self.values = {}, []
		if values:
			for value in values:
				self.add(value)

	def add(self, val):
		if val in self.position: return
		
		self.position[val] = len(self.values)
		self.values += [val]

	def remove(self, val):
		if val not in self.position: return
		
		if len(self.values) > 1 and self.position[val] < len(self.values)-1:
			index, newValue = self.position[val], self.values.pop()
			self.values[index], self.position[newValue] = newValue, index
		else: self.values.pop()
		
		del self.position[val]

	def __getitem__(self, key):
		return self.values[key]
	
	def __delitem__(self, key):
		self.remove(self.values[key])
	
	def __len__(self):
		return len(self.values)
	
	def __iter__(self):
		return iter(self.values)
		

if __name__ == "__main__":
	ss = SubscriptableSet([1,2,3])
	print(ss[0], ss[::-1])
	del ss[0]
	print(ss[::])

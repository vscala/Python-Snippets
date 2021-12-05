# Disjoint Set / Union-Find

class DisjointSet:
	def __init__(self):
		self.parent = {}
		self.rank = {}
		
	# returns parent of an element (if the element has a parent)
	def find(self, element):
		if element not in self.parent:
			self.parent[element] = element
			self.rank[element] = 0
		elif element != self.parent[element]:
			self.parent[element] = self.find(self.parent[element])
		return self.parent[element]
	
	# unions two elements together
	def union(self, a, b):
		parenta, parentb = self.find(a), self.find(b)
		if parenta != parentb:
			if self.rank[parenta] >= self.rank[parentb]:
				self.parent[parentb] = parenta
				self.rank[parenta] += 1
			else:
				self.parent[parenta] = parentb
				self.rank[parentb] += 1
	
if __name__ == "__main__":
	ds = DisjointSet()
	data = [(8,2), (5,3), (3,4), (2, 8)]
	for a, b in data:
		ds.union(a, b)
	for i in range(9):
		print(ds.find(i))
			
			
			


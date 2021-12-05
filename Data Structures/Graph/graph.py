from collections import defaultdict

class Graph:
	def __init__(self, directed = False, weighted = False):
		self.directed = directed
		self.weighted = weighted
		if weighted:
			self.graph = defaultdict(dict)
		else:
			self.graph = defaultdict(set)
		

	def insert(self, a, b, weight = 0) -> None:
		if self.weighted:
			self.graph[a][b] = weight
			if not self.directed:
				self.graph[b][a] = weight
		else:
			self.graph[a].add(b)
			if not self.directed:
				self.graph[b].add(a)
	
	def path(self, a, b):
		pass # TODO

if __name__ == "__main__":
	test = Graph()
	test.insert(1,2)
	test.insert(2,3)
	test2 = Graph(directed = True)
	test2.insert(1,2)
	test2.insert(2,3)
	test3 = Graph(weighted = True)
	test3.insert(1,2,3)
	test3.insert(2,3,4)
	
	print(test.graph, test2.graph, test3.graph, sep = "\n\n")

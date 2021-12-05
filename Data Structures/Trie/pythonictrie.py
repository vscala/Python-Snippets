from functools import reduce
from collections import defaultdict
from pprint import PrettyPrinter

class Trie:
	def __init__(self):
		node = lambda : defaultdict(node)
		self.trie = node()

	def insert(self, word: str) -> None:
		reduce(dict.__getitem__, word, self.trie)[True] = True
		
	def search(self, word: str) -> bool:
		return True in reduce(dict.__getitem__, word, self.trie)
    
	def startsWith(self, prefix: str) -> bool:
		return bool(reduce(dict.__getitem__, prefix, self.trie))
		

def testTrie():
	test = Trie()
	test.insert("yolo")
	assert (test.startsWith("yo"))
	assert (test.startsWith("yolo"))
	assert (test.search("yolo"))
	assert not (test.search("yol"))
	assert not (test.startsWith("to"))
	assert not (test.search("to"))
	assert not (test.search(""))
	assert (test.startsWith(""))
	

if __name__ == "__main__":
	testTrie()

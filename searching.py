#Searches

def iterative_dfs(graph, root, key):
	seen = set([root]) #if a graph (not tree)
	q = [root]
	while q:
		cur = q.pop()
		print(cur, end=' ')
		if cur == key: return True
		for child in graph[cur]:
			if child not in seen:
				q += [child]
				seen.add(child)
	return False
	
def iterative_bfs(graph, root, key):
	seen = set([root]) #if a graph (not tree)
	q = [root]
	while q:
		cur = q.pop(0)
		print(cur, end=' ')
		if cur == key: return True
		for child in graph[cur]:
			if child not in seen:
				q += [child]
				seen.add(child)
	return False
	
if __name__ == "__main__":
	graph = {1:[2,3], 2:[5,6], 3:[4], 4:[7], 5:[], 6:[], 7:[]}
	print(iterative_dfs(graph, 1, 6))
	print(iterative_bfs(graph, 1, 6))
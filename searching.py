# Searching graphs
from collections import defaultdict
from heapq import heappop, heappush


# Dijkstras algorithm 
def dijkstra(graph, start):

	pq = [(0, start)] 	# priority queue: (path_weight, current_node)
	visited = set() 	# set of visited nodes

	print(f"--- Searching Graph ---")
	while pq:
		path_weight, cur = heappop(pq)
		if cur in visited: continue
		visited.add(cur)
		print(f"Path found {start} to {cur} with length {path_weight}")
		for adj in graph[cur]:
			if adj not in visited:
				heappush(pq, (path_weight + graph[cur][adj], adj))

# Iterative Depth-First-Search 
def iterative_dfs(graph, root, key):
	seen = set([root]) 
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
	
# Iterative Breadth-First-Search 
def iterative_bfs(graph, root, key):
	seen = set([root]) 
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
	
def getGraph(edges):
	graph = defaultdict(dict)
	for a, b, w in edges:
		graph[a][b] = w
	return graph
	
if __name__ == "__main__":
	A, B, C, D, E, F, G, H = "ABCDEFGH"
	edges = [(A, B, 6), (A, E, 6), (A, D, 5), (B, H, 2), (C, B, 3), (C, D, 3), (D, A, 5), 
			 (E, D, 2), (E, G, 5), (G, E, 5), (G, H, 4), (G, F, 7), (H, E, 2), (H, G, 2)]
	graph = getGraph(edges)
	
	print(iterative_dfs(graph, A, F))
	print(iterative_bfs(graph, A, F))
	
	dijkstra(graph, A)


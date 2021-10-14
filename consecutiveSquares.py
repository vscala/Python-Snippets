# Consecutive squares

# Naive solution
def naiveSquares(n):
	return [i**2 for i in range(1,n+1)]

# Math recurrence solution (n+1)^2 = n^2 + 2n + 1
def mathSquares(n):
	out = [1]
	for i in range(1, n):
		out += [out[-1] + (i << 1) + 1]
	return out
	
if __name__ == "__main__":
	sz = 4
	print("naive")
	for i in range(sz):
		print(naiveSquares(10**i))
	print("\nmath")
	for i in range(sz):
		print(mathSquares(10**i))

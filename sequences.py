from functools import lru_cache

# Consecutive squares ((n+1)^2 = n^2 + 2n + 1)
def mathSquares(n):
	out = [1]
	for i in range(1, n):
		out += [out[-1] + (i << 1) + 1]
	return out

# Fibonacci sequence F(n) = F(n-1) + F(n-2) (0-index)
def fib(n, a=0, b=1):
	for i in range(n):
		a, b = b, a+b
	return a

# Catalan numbers (unique binary trees) (0-index)
@lru_cache
def cat(n):
	if n == 0 or n == 1: return 1
	out = 0
	for i in range(n):
		out += cat(i) * cat(n-i-1)
	return out

if __name__ == "__main__":
	for i in range(4):
		print(mathSquares(10**i))
	print(fib(5), cat(6))

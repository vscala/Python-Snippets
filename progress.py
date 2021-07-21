#Python console progress bar and percentage
import sys
from time import sleep

'''
	Print progress percentage cur/mx without creating a new line
'''
def progressPercent(cur = 0, title = 'Progress', mx = 100):
	sys.stdout.write(f"\r{title}: {100*cur/mx}%")
	sys.stdout.flush()

'''
	Generator to print progress bar without creating a new line
'''
def progressBar(title = 'Progress', size = 10):
	sys.stdout.write(f"{title}: [{'-'*size}]{chr(8)*(size+1)}")
	sys.stdout.flush()
	for i in range(size):
		sys.stdout.write("#")
		sys.stdout.flush()
		yield
	

if __name__ == '__main__':
	pb = progressBar()
	for i in range(10):
		next(pb)
		sleep(.01)
	for i in range(1001):
		progressPercent(i, mx=1000)
		sleep(.001)
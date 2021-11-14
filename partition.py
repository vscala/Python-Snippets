# partitionings of collection(s)

# partiton an array
def partition(arr):
	out = []
	for mask in range(2 ** (len(arr) - 1)):	
	
		partition = []
		subset = []
		
		for i in range(len(arr)):
			subset += [arr[i]]
			if (1 << i) & mask:
				partition += [subset]
				subset = []
		if subset: partition += [subset]
		out += [partition]
	return out

if __name__ == "__main__":
	print(partition([1,2,3,4]))

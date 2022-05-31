from bisect import bisect_left
from typing import List, Any

def patienceSortLen(arr : List[Any]) -> int:
	maxArr = [float("inf")] * len(arr)
	for val in arr:
		maxArr[bisect_left(maxArr, val)] = val
	return bisect_left(maxArr, float("inf"))

def patienceSortSeq(arr : List[Any]) -> List[Any]:
	maxArr = [float("inf")] * len(arr)
	for val in arr:
		maxArr[bisect_left(maxArr, val)] = val
	return maxArr[:bisect_left(maxArr, float("inf"))]

'''
	LeetCode : 354. Russian Doll Envelopes
	https://leetcode.com/problems/russian-doll-envelopes/
'''
def maxEnvelopes(envelopes: List[List[int]]) -> int:
	envelopes.sort(key = lambda envelope : (envelope[0], -envelope[1]))
	return patienceSortLen([b for _, b in envelopes])

if __name__ == "__main__":
	from random import randint
	for _ in range(10):
		nums = [randint(-1000, 1000) for _ in range(randint(100, 1000))]
		print(patienceSortLen(nums), patienceSortSeq(nums), sep="\n")
	t1 = [[5,4],[6,4],[6,7],[2,3]]
	t2 = [[1,1],[1,1],[1,1]]
	print(maxEnvelopes(t1), maxEnvelopes(t2))
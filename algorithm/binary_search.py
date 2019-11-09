#!/usr/bin/env python
# -*- coding: utf-8 -*-

# binary_search recursive
data = [1,2,5,23,56,89]

def binary_search(data, key):
	size = len(data)
	if size < 1 or not key:
		return False
	mid = size // 2

	if data[mid] > key:
		return binary_search(data[0:mid], key)
	elif data[mid] < key:
		return binary_search(data[mid+1:], key)
	else:
		return True

print('binary search recursive')
print('search key: 4')
print(binary_search(data, 4))

print('search key: 5')
print(binary_search(data, 5))

# non-recursive
def search(data, key):
	size = len(data)
	if size < 1 or not key:
		return False

	left = 0
	right = size - 1

	while left <= right:
		mid = (left + right) // 2

		if data[mid] > key:
			right = mid -1
		elif data[mid] < key:
			left = mid + 1
		else:
			return True
	return False

print('binary search non-recursive')
print('search key: 4')
print(search(data, 4))

print('search key: 5')
print(search(data, 5))
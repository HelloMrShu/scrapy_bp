#!/usr/bin/env python
# -*- coding: utf-8 -*-

# binary_search
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

print('search key: 4')
print(binary_search(data, 4))

print('search key: 5')
print(binary_search(data, 5))

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# single-scan
data_list = [4,8,15,3,3,1,22,6,11,6]

def quick_sort(data_list):
	if len(data_list) < 2:
		return data_list

	left, right = [], []
	pivot = data_list[0]
	data_list.remove(pivot)

	for item in data_list:
		if item < pivot:
			left.append(item)
		else:
			right.append(item)

	left = quick_sort(left)
	right = quick_sort(right)

	return left + [pivot] + right

print(quick_sort(data_list))

# double-scan
data = [4,8,15,3,3,1,22,6,11,6]

def partition(num, low, high):
    pivot = num[low]
    while (low < high):
        while (low < high and num[high] >= pivot):
            high -= 1
        num[low] = num[high]

        while (low < high and num[low] <= pivot):
            low += 1
        num[high] = num[low]

    num[low] = pivot
    return low

def quicksort(num ,low ,high):
    if low< high:
        location = partition(num, low, high)
        quicksort(num, low, location - 1)
        quicksort(num, location + 1, high)
    return num

print(quicksort(data, 0, len(data) - 1))

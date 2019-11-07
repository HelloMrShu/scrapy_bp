#!/usr/bin/env python
# -*- coding: utf-8 -*-

data_list = [4,8,15,3,3,1,22,6,11,6]

# 随机枢轴
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
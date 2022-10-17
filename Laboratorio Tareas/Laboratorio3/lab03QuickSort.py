# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 22:55:40 2022

@author: hp
"""

# importing the module
from datetime import datetime
def partition(array, low, high):

	
	pivot = array[high]

	i = low - 1

	for j in range(low, high):
		if array[j] <= pivot:

			i = i + 1

			(array[i], array[j]) = (array[j], array[i])

	
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	return i + 1


def quickSort(array, low, high):
	if low < high:

		pi = partition(array, low, high)
		quickSort(array, low, pi - 1)
		quickSort(array, pi + 1, high)

      
data = [10,9,8,7,6,5,4,3,2,1]

print("Matriz sin ordenar :")
print(data) 
start = datetime.now()
size = len(data)
quickSort(data, 0, size - 1)
print('Matriz ordenada en orden ascendente:')
print(data)
end = datetime.now()
print('formato HH: MM: SS: MiliSeg',end-start)
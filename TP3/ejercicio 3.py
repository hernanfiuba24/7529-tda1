#!/usr/bin/env python
import random


def ejercicio_tres_punto_uno(n):
	array = []
	for i in range(0, n):
		array.append(random.randint(0, 10000))
	t = random.randint(0, 10000)
	return	{
		"array": array,
		"t": t
	}

def ejercicio_tres_punto_dos(array, t, e)
	n = len(array)
	Lists =[[0]]
	for i in range(1, n):
		auxList = merge_lists(Lists[i-1], [(x + array[i]) for x in Lists[i-1]])
		auxList = trim_list(auxList, e)
		Lists[i] = filter(lambda x: x < t, auxList)
	return max(Lists[n])

def merge_lists(first_list, second_list):
	return sort(first_list + list(set(second_list) - set(first_list)))

def trim_list(lista, e):
	m = len(lista)
	newList = [lista[0]]
	last = lista[m]
	for i in range(2, m):
		if lista[i] > (last * (1 + e)):
			newList.append(lista[i])
			last = lista[i]
	return newList

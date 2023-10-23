#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
	length = 0
	for e in range(x):
		try:
			print("{}".format(my_list[e]), end= "")
			length += 1
		except Exception:
			break
	print("")
	return length

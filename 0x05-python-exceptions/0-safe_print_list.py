#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
	l = 0
	for e in range(x):
		try:
			print("{}".format(my_list[e]), end= "")
			l += 1
		except Exception:
			break
	print("")
	return l

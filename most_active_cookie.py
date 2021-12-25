#!/usr/bin/python

import sys
from collections import OrderedDict

def main(argv):
	print argv
	if len(sys.argv) != 4:
		print("Not enough arguments")
		return
	filename = sys.argv[1]
	flag = sys.argv[2]
	date = sys.argv[3]

	if flag != "-d":
		print("Invalid Flag")
		return
	
	readFile = open(filename, 'r')
	lines = readFile.readlines()

	arr = {}
	
	for l in lines[1:]:
		cookie, timestamp = l.split(",")[0], l.split(",")[1]

		if timestamp[:10] == date:
			if cookie in arr.keys():
				arr[cookie] += 1
			else:
				arr[cookie] = 1

	# count = max([x for k, x in arr.items()])
	count = max(arr.values())
	for key, val in arr.items():
		if val == count:
			print(key)

	return

if __name__ == "__main__":
	main(sys.argv)

import sys
import time
import random

def mergeSort(list):
	if len(list)>1:
		mid = len(list)//2
		left = list[:mid]
		right = list[mid:]

		mergeSort(left)
		mergeSort(right)

		i=0
		j=0
		k=0
		#leftlen = len(left)
		#rightlen = len(right)
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				list[k] = left[i]
				i=i+1
			else:
				list[k] = right[j]
				j=j+1
			k=k+1

		while i < len(left):
			list[k] = left[i]
			i=i+1
			k=k+1

		while j < len(right):
			list[k] = right[j]
			j=j+1
			k=k+1
	
	return list

list = []
with open("data.txt", "r") as f:
	for line in f:
		for s in line.split(" "):
			num = int(s)
			list.append(num)
		
list = mergeSort(list);
f = open("merge.out", "w")
for num in list:
	one = str(num)
	f.write(one)
	f.write(" ")
f.close()

sys.setrecursionlimit(40000) # raises the buffer limit for recursive methods. (needed for .flip server)

def sort_timer(A):
    X = [random.random() for i in range(A)]  #make the random test array (would "in range(A)" work?)
    start_time = time.time()                            #note the current time
    mergeSort(X)                                        # run your sort function
    elapsed_time = start_time - time.time()   #subtract current time from saved time
    print("Insertion sort speed per n:")           # print the result, the result will be a negative number, use the absolute value
    print(elapsed_time*-1)

M = [350,400,450,500]   # create some test values
for i in M:                                 
  sort_timer(i)                         

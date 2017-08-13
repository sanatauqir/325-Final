def stoogeSort(list, i=0, j=None):
	if j is None:
		j = len(list)-1
	if list[j] < list[i]:
		list[i], list[j] = list[j], list[i]
	if (j-i+1) > 2:
		m = (j-i+1) / 3
		stoogeSort(list, i, j-m)
		stoogeSort(list, i+m, j)
		stoogeSort(list, i, j-m)
	return list

#sys.setrecursionlimit(1500)
list = []
size = 0
with open("data.txt", "r") as f:
	for line in f:
		n = 0
		for s in line.split(" "):
			n=n+1
			if (n==1):
				size = int(s)
			else:
				num = int(s)
				list.append(num)

list = stoogeSort(list);
f = open("stooge.out", "w")
for num in list:
	one = str(num)
	f.write(one)
	f.write(" ")
f.close()                        

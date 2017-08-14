import sys
import math
import time
import random

def createMatrix(file):
	allCities = []
	#read in from the file and place x,y coordinates into an array of cities
	with open(file, "r") as f:
		for line in f:
			oneCity = line.split()
			city = {'c':int(oneCity[0]), 'x':int(oneCity[1]), 'y':int(oneCity[2])}
			#print city
			allCities.append(city)
	#print allCities
	numCities = len(allCities)
	# matrix creation
	cityMatrix = [[0 for x in range(numCities)] for y in range(numCities)]
	for i in range(0, numCities):
		for j in range(i + 1, numCities):
			#not going anywhere
			if (i==j):
				cityMatrix[i][j] = 0
			#going between cities
			else:
				dist = eucDist(allCities[i], allCities[j])
				cityMatrix[i][j] = dist
				cityMatrix[j][i] = dist
	return cityMatrix
	
def eucDist(city1, city2):
	interm = ((city1['x']-city2['x'])**2) + ((city1['y']-city2['y'])**2) 
	dist = round(math.sqrt(interm))
	return dist
	
# get the filename from command line
fil = sys.argv[-1]	
t0 = time.time()
mat = createMatrix(fil);

print "time is", time.time() - t0

tour = ".tour"
outfil = fil + tour
f=open(outfil, "w+")
f.write("%s\n" % mat)
f.close()

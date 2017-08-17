import sys
import math
import time
import random

def Annealing(matrix, T, cooling, numCities):
	path = []
	for i in xrange(0, numCities):
		path.append(i)
	#the path returns to the first city
	path.append(0)
	oldCost = calcCost(matrix, path, numCities)
	bestPath = path
	while T > cooling:
		#swap two vertices in path and recalculate
		newPath = createNewPath(path)
		newCost = calcCost(matrix, newPath, numCities)	
		if newCost <= oldCost: #more optimal than the current solution
			path = newPath
			if newCost <= calcCost(matrix, bestPath, numCities):	#most optimal solution so far
				bestPath = path
		#small corrections to syntax
		#elif Math.exp(oldCost-newCost)/T > rand():
		elif math.exp(oldCost-newCost)/T > random.random():
			path = newPath
		T = T*cooling
	return bestPath
	
def calcCost(matrix, path, numCities):
	x = 0
	pathLength = 0
	matrixPath = 0
	#calculate the path length from 0 -> 0
	while (x < numCities):
		xVal = path[x]
		yVal = path[x + 1]
		pathLength = matrix[xVal][yVal] + pathLength
		x = x + 1
	#for testing
	print("test path length = ", pathLength)
	#return the new pathLength
	return pathLength
	
def createNewPath(path):
	#get 2 random vertecies to flip
	#exclude 0th index and the last index since these are the starting location
	randNum1 = random.randint(1, len(path) -2)
	randNum2 = random.randint(1, len(path) -2)

	#make sure the vertecies are different numbers
	while(randNum2 == randNum1):
		randNum2 = random.randint(1, len(path) -2)

	#flip vertecies	
	path[randNum1], path[randNum2] = path[randNum2], path[randNum1]
	#for testing
	print("new test path = ", path)
	return path

def createMatrix(file):
	allCities = []
	#read in from the file and place x,y coordinates into an array of cities
	with open(file, "r") as f:
		for line in f:
			if line != '\n':
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
fil = sys.argv[1]	
t0 = time.time()
mat = createMatrix(fil);
if len(mat) < 400:
	best = Annealing(mat, 1000, .05, len(mat))
else:
	best = Annealing(mat, 1000, .01, len(mat))
print "best",
print best
print "time is", time.time() - t0
print "best path found was "
final =  calcCost(mat, best, len(mat))
print "final distance"
print final
tour = ".tour"
outfil = fil + tour
f=open(outfil, "w+")
f.write("%s\n" % final)
for x in best:
	f.write("%s\n" % x)
f.close()

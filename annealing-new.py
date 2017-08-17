import sys
import math
import time
import random

def Annealing(matrix, T, cooling, numCities):
	path = []
	for i in xrange(0, numCities):
		path.append(i)
	#the path returns to the first city
	#path.append(0)
	oldCost = calcCost(matrix, path, numCities)
	print "oldCost",
	print oldCost
	bestPath = path

	while T > 0:
		#swap two vertices in path and recalculate
		randNum1 = random.randint(0, len(path) -2)
		randNum2 = random.randint(0, len(path) -2)
		while(randNum2 == randNum1):
			randNum2 = random.randint(0, len(path) -2)

		newPath = createNewPath(path, randNum1, randNum2)
		newCost = calcCost(matrix, newPath, numCities)
		#newCost = 10
		r = random.random()		
		if newCost <= oldCost: #more optimal than the current solution
			print "if"
			path = newPath
			if newCost <= calcCost(matrix, bestPath, numCities):	#most optimal solution so far
				bestPath = path
		#small corrections to syntax
		#elif Math.exp(oldCost-newCost)/T > rand():
		elif math.exp(oldCost-newCost)/T > r:
			print "else if"
			path = newPath
		else:
			print "else"
			path = createNewPath(path,randNum1,randNum2)
		T = T*cooling
	return bestPath
	
def calcCost(matrix, path, numCities):
	x = 0
	pathLength = 0
	matrixPath = 0
	#calculate the path length from 0 -> 0
	while (x < numCities-1):
		xVal = path[x]
		yVal = path[x + 1]
		pathLength = matrix[xVal][yVal] + pathLength
		x = x + 1
	#for testing
	pathLength = matrix[yVal][path[0]]+pathLength
	print("test path length = ", pathLength)
	#return the new pathLength
	return pathLength
	
def createNewPath(path, one, two):
	#get 2 random vertecies to flip
	#exclude 0th index and the last index since these are the starting location
	#randNum1 = random.randint(1, len(path) -2)
	#randNum2 = random.randint(1, len(path) -2)
	
	#make sure the vertecies are different numbers

	#flip vertecies	
	path[one], path[two] = path[two], path[one]
	#for testing
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
fil = sys.argv[-1]	
t0 = time.time()
mat = createMatrix(fil);
if len(mat) < 400:
	best = Annealing(mat, 500000000000000000000000000, .01, len(mat))
else:
	best = Annealing(mat, 1000, .01, len(mat))
print "time is", time.time() - t0
print "best path found was "
final =  calcCost(mat, best, len(mat))
final = int(final)
tour = ".tour"
outfil = fil + tour
f=open(outfil, "w+")
f.write("%s\n" % final)
for x in best:
		f.write("%s\n" % x)
f.close()

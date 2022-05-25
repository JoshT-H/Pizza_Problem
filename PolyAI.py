import numpy as np 

N, M    = [int(x) for x in input('Debug; ').split()]

points = []

for i in range(M):
	X, Y, R = [int(x) for x in input('Loc ').split()] 
	points.append([X, Y, R])


grid = np.zeros((N,N), dtype = int)

for x in range(len(points)):#
	print(points[x])
	i = 0
	while i < points[x][2]:
		grid[points[x][0]+i][points[x][1] + i] = 1 + grid[points[x][0]+i][points[x][1] + i] 
		i= i +1



print(grid)
print(points)
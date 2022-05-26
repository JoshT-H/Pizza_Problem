import numpy as np 

N, M    = [int(x) for x in input('Debug; ').split()]

points = []

for i in range(M):
	X, Y, R = [int(x) for x in input('Loc ').split()] 
	points.append([X, Y, R])


grid = np.zeros((N, N), dtype = int)


for x in range(len(points)):#
	i = 1
	while i < (points[x][2] + 1) :
		if not points[x][0] + 1 < 0 and not points[x][1] + 1 <0:
			grid[points[x][0]+i][points[x][1]] = 1 + grid[points[x][0]+i][points[x][1] + i]
			grid[points[x][0]][points[x][1] + i] = 1 + grid[points[x][0]+i][points[x][1] + i]
		if not points[x][0] - 1 < 0 and not points[x][1] -1 < 0:
			grid[points[x][0] - i][points[x][1]]     = 1 + grid[points[x][0] - i][points[x][1]]
			grid[points[x][0]][points[x][1] - i]     = 1 + grid[points[x][0]][points[x][1] - i]

		#grid[points[x][0] - i][points[x][1]] = 1 + grid[points[x][0]+i][points[x][1] + i]
		#grid[points[x][0]][points[x][1] - i] = 1 + grid[points[x][0]+i][points[x][1] + i]

		i = i +1



print(grid)
print(points)

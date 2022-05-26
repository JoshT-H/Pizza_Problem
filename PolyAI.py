import numpy as np 

N, M  = [int(x) for x in input('Debug; ').split()]
points = []
# https://stackoverflow.com/questions/58348401/numpy-array-filled-in-diamond-shape
for i in range(M):
	X, Y, R = [int(x) for x in input('Loc ').split()] 
	points.append([X, Y, R])

#https://stackoverflow.com/questions/7115437/how-to-embed-a-small-numpy-array-into-a-predefined-block-of-a-large-numpy-arra
def paste_slices(tup):
  pos, w, max_w = tup
  wall_min = max(pos, 0)
  wall_max = min(pos+w, max_w)
  block_min = -min(pos, 0)
  block_max = max_w-max(pos+w, max_w)
  block_max = block_max if block_max != 0 else None
  return slice(wall_min, wall_max), slice(block_min, block_max)

def paste(wall, block, loc):
  loc_zip = zip(loc, block.shape, wall.shape)
  wall_slices, block_slices = zip(*map(paste_slices, loc_zip))
  wall[wall_slices] = block[block_slices]

grids = []

for x in range(len(points)):
	grid = np.zeros((N, N), dtype=int)
	r = points[x][2] -1

	array = np.add.outer(*[np.r_[:r, r:-1:-1]] * 2) >= r
	array = array * 1

	disCentre = array.shape[0]//2 + 1

	paste(grid,array,(points[x][0] - disCentre ,points[x][1]- disCentre))
	print(grid)
	print('--------------------------------')
	grids.append(grid)
#for x in range(len(points)):#
	#i = 1
	#grid[points[x][0]-1][points[x][1]-1] = 1 + grid[points[x][0]-1][points[x][1]-1]

print(grids)
print(sum(grids))
print(np.max(sum(grids)))

	#while i < (points[x][2] + 1) :
		#if not points[x][0] + i -1  < 0 and not points[x][1] + i -1 < 0 and points[x][1] + i - 1 <= len(grid) - 1 and points[x][1] -1 + i <= len(grid) -1 :
		#	grid[points[x][0]+i-1][points[x][1]-1] = 1 + grid[points[x][0]+i-1][points[x][1]-1]
			#grid[points[x][0]-1][points[x][1] + i -1] = 1 + grid[points[x][0]-1][points[x][1] + i - 1]



		#if not points[x][0] - i - 1 < 0 and not points[x][1] - i - 1 < 0 and points[x][1] - i - 1 <= len(grid) - 1 and points[x][1] - 1- i <= len(grid) -1 :
		#	grid[points[x][0] - i - 1][points[x][1] - 1]     = 1 + grid[points[x][0] - i -1][points[x][1] - 1]
			#grid[points[x][0] - 1][points[x][1] - i - 1]     = 1 + grid[points[x][0] - 1][points[x][1] - i -1]

		#grid[points[x][0] - i][points[x][1]] = 1 + grid[points[x][0]+i][points[x][1] + i]
		#grid[points[x][0]][points[x][1] - i] = 1 + grid[points[x][0]+i][points[x][1] + i]

		#i = i +1




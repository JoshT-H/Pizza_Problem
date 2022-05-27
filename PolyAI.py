import numpy as np 

locations = [] # Storing Pizzaria Locations and Delivery Range
grids = [] # Collating Pizzaria Maps

with open('input.txt', 'r') as file:
     lines = ([line.strip() for line in file])

for i, x in enumerate(lines):
	N, M = int(lines[0][0]), int(lines[0][2])
	if i > 0:
		X, Y, R = int(lines[i][0]), int(lines[i][2]), int(lines[i][4])
		locations.append([X, Y, R])

# Debug
if len(locations) > M:
	print("Dimensional error: number of points give is greater greater than N")


#N, M = [int(x) for x in input().split()]  # Obtaining Grid Dims and Number of Pizzarias
#for i in range(M): # Obtaining locations and ranges of Pizzarias
#	X, Y, R = [int(x) for x in input().split()]
#	locations.append([X, Y, R])

def paste_slices(tup):
  pos, w, max_w = tup
  minGrid, maxGrid = max(pos, 0), min(pos+w, max_w)
  minArray, maxArray = -min(pos, 0),  max_w-max(pos+w, max_w)
  maxArray = maxArray if maxArray != 0 else None
  return slice(minGrid, maxGrid), slice(minArray, maxArray)

def paste(grid, array, loc):
  loc_zip = zip(loc, array.shape, grid.shape)
  grid_slices, array_slices = zip(*map(paste_slices, loc_zip))
  grid[grid_slices] = array[array_slices]


for x in range(len(locations)):
	grid = np.zeros((N, N), dtype=int)
	r = locations[x][2]

	array = np.add.outer(*[np.r_[:r, r:-1:-1]] * 2) >= r
	array = array * 1

	disCentre = array.shape[0]//2 + 1
	paste(grid, array, (locations[x][0] - disCentre ,locations[x][1]- disCentre))

	grid = np.rot90(grid)

	grids.append(grid)

print(grids)
print(sum(grids))
print(np.max(sum(grids)))




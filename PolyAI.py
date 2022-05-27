import numpy as np
locations = [] # Storing pizzeria locations and delivery range
grids = [] # Collating individual pizzeria maps


# Initial parsing method for variable via user inputs
#N, M = [int(x) for x in input().split()]  # Obtaining Grid Dims and Number of Pizzarias
#for i in range(M): # Obtaining locations and ranges of Pizzarias
#	X, Y, R = [int(x) for x in input().split()]
#	locations.append([X, Y, R])

# Second parsing method of text file as per requirement
with open('input.txt', 'r') as file:
     lines = ([line.strip() for line in file])

for i, x in enumerate(lines):
	N, M = int(lines[0][0]), int(lines[0][2])
	if i > 0:
		X, Y, R = int(lines[i][0]), int(lines[i][2]), int(lines[i][4])
		locations.append([X, Y, R])

## Debug if the message for mismatch between N and the number of Pizzeria locations given.
#if len(locations) > M:
	#print("Dimensional error: number of points give is greater greater than N")


def sliceArray(tup):
	"""
	Ensures that elements of the mask that exist
	outside the grid are not included, thus allowing
	the mask to be placed onto the grid even if it falls off the edge.
	"""
	position, w, wMax = tup
	minGrid, maxGrid = max(position, 0), min(position+w, wMax)
	minArray, maxArray = -min(position, 0),  wMax-max(position+w, wMax)
	maxArray = maxArray if maxArray != 0 else None
	return slice(minGrid, maxGrid), slice(minArray, maxArray)

def insertArray(grid, array, loc):
	"""
	Inserts smaller pizzeria array into larger world array - similar to placing a mask on an image.
	"""
	loc_zip = zip(loc, array.shape, grid.shape)
	grid_slices, array_slices = zip(*map(sliceArray, loc_zip))
	grid[grid_slices] = array[array_slices]

def pizzeriaArray(r):
	"""
	Take the delivery range of each pizzeria as argument
	 and generates an array highlighting the location of said
	 pizzeria and the tiles it will deliver to.
	"""
	# Generates a boolean array; True = will deliver and False = will not deliver
	smallArray = np.add.outer(*[np.r_[:r, r:-1:-1]] * 2) >= r
	return smallArray * 1 # Convert bool-array => int-array

for x in range(len(locations)):
	grid = np.zeros((N, N), dtype=int)
	smallArray = pizzeriaArray(locations[x][2]) # Argument is delivery radius
	disCentre = smallArray.shape[0] // 2 + 1 # Obtain distance to center i.e location of pizzeria

	# Inserts smaller pizzeria array onto larger grid/world array
	insertArray(grid, smallArray, (locations[x][0] - disCentre , locations[x][1] - disCentre))

	# The (0,0) coordinate is as the top of the grid thus it must be rotated.
	grid = np.rot90(grid)

	# Individually generating grids with the pizzerias projected onto them.
	grids.append(grid)

# Debugging
# Printing a list containing all the individual grids
#print(grids)
# Printing the resultant grid map
#print(sum(grids))

# Summing all the grids in the list to generate a map which includes all the pizzerias and finding the maximum value in the array.
print(np.max(sum(grids)))




import numpy, random 
from mayavi import mlab  # Import the mlab module from mayavi

levels = 5  # Set the number of levels for terrain generation
size = 2 ** (levels - 1)  # Calculate the size of the height grid
height = numpy.zeros((size + 1, size + 1))  # Initialize the height grid with zeros

# Loop through each level
for lev in range(levels):
    step = size // 2 ** lev  # Calculate the step size for the current level
    # Loop through y coordinates with the step size
    for y in range(0, size + 1, step):
        jumpover = 1 - (y // step) % 2 if lev > 0 else 0  # Calculate jumpover value
        # Loop through x coordinates with the step size, considering jumpover
        for x in range(step * jumpover, size + 1, step * (1 + jumpover)):
            pointer = 1 - (x // step) % 2 + 2 * jumpover if lev > 0 else 3  # Calculate pointer value
            yref, xref = step * (1 - pointer // 2), step * (1 - pointer % 2)  # Calculate reference coordinates
            corner1 = height[y - yref, x - xref]  # Get height value of corner 1
            corner2 = height[y + yref, x + xref]  # Get height value of corner 2
            average = (corner1 + corner2) / 2.0  # Calculate average height
            variation = step * (random.random() - 0.5)  # Generate random variation
            height[y, x] = average + variation if lev > 0 else 0  # Assign height value to grid

# Generate meshgrid for X and Y coordinates
xg, yg = numpy.mgrid[-1:1:1j*size, -1:1:1j*size]
surf = mlab.surf(xg, yg, height, colormap='gist_earth', warp_scale='auto')
mlab.show() 

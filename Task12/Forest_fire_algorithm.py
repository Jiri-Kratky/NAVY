import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors

forest_size = (100, 100)

p = 0.05                                                    # New tree after burnt area probability
f = 0.001                                                   # Probability of a tree randomly catching fire
forest_density = 0.5                                        # Forest density
neighborhood = ((-1,-1), (-1,0), (-1,1), (0,-1), (0, 1), (1,-1), (1,0), (1,1))  # Define the Moore neighborhood (check every neighbour)

forest = np.random.choice([0, 1], size=forest_size, p=[0.5, 0.5])   # Initialize the forest grid (50/50)
fig, ax = plt.subplots()    # Create a figure and axis for the animation

# Define the colors for different types (white - space, green - tree, orange - fire, black - burnt tree)
cmap = colors.ListedColormap(['white', 'green', 'orange', 'black'])
bounds = [0, 1, 2, 3, 4]
norm = colors.BoundaryNorm(bounds, cmap.N)


def update(frame): # Function to update the forest grid in each animation frame
    global forest
    
    new_forest = forest.copy()      #copy the forest

    # Replace burnt areas with live trees with probability p
    new_forest[new_forest == 3] = np.random.choice([1, 0], size=np.sum(new_forest == 3), p=[p, 1 - p])

    for i in range(forest_size[0]):
        for j in range(forest_size[1]):
            if forest[i, j] == 1:   # Check for a tree
                for dx, dy in neighborhood:  # Check if any neighbor is on fire
                    if forest[(i + dx) % forest_size[0], (j + dy) % forest_size[1]] == 2:
                        new_forest[i, j] = 2  # Tree catches fire from neighbor
                        break
                
                if(np.random.rand() < f):   # Randomly catch on fire
                    new_forest[i, j] = 2

            elif forest[i, j] == 2: # Tree is on fire
                new_forest[i, j] = 3  # Tree is burnt

            elif forest[i, j] == 0:   # Check for an empty space
                if np.random.rand() < p:
                    new_forest[i, j] = 1
    

    forest = new_forest     # Update the forest grid

    # Display the forest
    ax.clear()
    ax.imshow(forest, cmap=cmap, norm=norm)
    ax.set_title('Forest Fire Algorithm')


ani = animation.FuncAnimation(fig, update, frames=200, interval=100)
plt.show()
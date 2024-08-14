import numpy as np
import matplotlib.pyplot as plt

def fractal_landscape(iterations, length, height_variation, start_y):
    landscape = [(0, start_y), (length, start_y)] #Single straigh line
    
    for _ in range(iterations):
        new_landscape = []
        for i in range(len(landscape) - 1): #Iterate through lines from landscape
            start_x, start_y = landscape[i]
            end_x, end_y = landscape[i + 1]
            
            mid_x = (start_x + end_x) / 2   #Calculate the midpoint
            mid_y = (start_y + end_y) / 2
            
            
            if np.random.rand() < 0.5:      #Go UP or DOWN
                mid_y += np.random.uniform(-height_variation, height_variation)
            else:
                mid_y -= np.random.uniform(-height_variation, height_variation)
            
            
            new_landscape.append((start_x, start_y)) #Add the new points to the landscape
            new_landscape.append((mid_x, mid_y))
            
            if i == len(landscape) - 2:     #When not at the end add end point too
                new_landscape.append((end_x, end_y))
        
        landscape = new_landscape
    
    return landscape

def plot_landscapes(landscapes):
    plt.figure(figsize=(10, 6))
    for i, (landscape, color) in enumerate(landscapes, 1):
        x = [point[0] for point in landscape]
        y = [point[1] for point in landscape]
        plt.plot(x, y, color=color)
        plt.fill_between(x, y, -10, color=color, alpha=0.7)

    plt.title("Fractal Landscapes")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.xlim(0, 10)
    plt.ylim(-10, 10)
    plt.show()

#landscape 1
iterations = 4
length = 10
height_variation = 2
start_y_1 = 6
color_1 = 'green'
landscape1 = fractal_landscape(iterations, length, height_variation, start_y_1), color_1

#landscape 2
iterations = 6
length = 10
height_variation = 0.5
start_y_2 = 0
color_2 = 'brown'
landscape2 = fractal_landscape(iterations, length, height_variation, start_y_2), color_2

#landscape 3
iterations = 3
length = 10
height_variation = 1
start_y_3 = -7
color_3 = 'black'
landscape3 = fractal_landscape(iterations, length, height_variation, start_y_3), color_3

# Plot all landscapes
plot_landscapes([landscape1, landscape2, landscape3])

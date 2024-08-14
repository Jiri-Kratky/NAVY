import numpy as np
import matplotlib.pyplot as plt

def calculation(c, max_iter):
    z = 0
    for i in range(max_iter):
        z = z**2 + c
        if abs(z) > 2:
            return i
    return max_iter

def plot_mandelbrot(x_min, x_max, y_min, y_max, width, height, max_iter):
    image = np.zeros((height, width, 4))  # Create a 4-dimensional array for the image
    
    for i, real in enumerate(np.linspace(x_min, x_max, width)):
        for j, imag in enumerate(np.linspace(y_min, y_max, height)):
            c = complex(real, imag)
            iteration = calculation(c, max_iter)
            hue = iteration / max_iter
            color = plt.cm.RdGy(hue)
            image[j, i] = color
    plt.imshow(image)
    #plt.savefig('image.png')
    plt.show()


#mandelbrot
x_min, x_max = -2, 1
y_min, y_max = -1, 1
width, height = 1200, 1200
max_iter = 40

plot_mandelbrot(x_min, x_max, y_min, y_max, width, height, max_iter)


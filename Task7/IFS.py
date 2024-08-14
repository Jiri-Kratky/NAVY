import random
import matplotlib.pyplot as plt

# Define the transformations for the first fern model
transformation1 = [
    [ 0.00, 0.00, 0.01, 0.00, 0.26, 0.00, 0.00, 0.00, 0.05, 0.00, 0.00, 0.00],
    [0.20, -0.26, -0.01, 0.23, 0.22, -0.07, 0.07, 0.00, 0.24, 0.00, 0.80, 0.00],
    [-0.25, 0.28, 0.01, 0.26, 0.24, -0.07, 0.07, 0.00, 0.24, 0.00, 0.22, 0.00],
    [0.85, 0.04, -0.01, -0.04, 0.85, 0.09, 0.00, 0.08, 0.84, 0.00, 0.80, 0.00]
]

# Define the transformations for the second fern model
transformation2 = [
    [0.05, 0.00, 0.00, 0.00, 0.60, 0.00, 0.00, 0.00, 0.05, 0.00, 0.00, 0.00],
    [0.45, -0.22, 0.22, 0.22, 0.45, 0.22, -0.22, 0.22, -0.45, 0.00, 1.00, 0.00],
    [-0.45, 0.22, -0.22, 0.22, 0.45, 0.22, 0.22, -0.22, 0.45, 0.00, 1.25, 0.00],
    [0.49, -0.08, 0.08, 0.08, 0.49, 0.08, 0.08, -0.08, 0.49, 0.00, 2.00, 0.00]
]

def apply_transformation(transformation, point):
    x,y,z = point
    random_int = random.randint(0,3)    # Randomly choose one of the transformations
    a,b,c,d,e,f,g,h,i,j,k,l = transformation[random_int]
    x_new = a*x + b*y + c*z + j
    y_new = d*x + e*y + f*z + k
    z_new = g*x + h*y + i*z + l

    return (x_new, y_new, z_new)


def generate_fern_model(transformations):
    history = []
    point = (0, 0, 0)
    for _ in range(1000):
        point = apply_transformation(transformations,point)
        history.append(point)
    return history


fern_model1 = generate_fern_model(transformation1)

fern_model2 = generate_fern_model(transformation2)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(*zip(*fern_model1), c='g', marker='.')
plt.show()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(*zip(*fern_model2), c='g', marker='.')
plt.show()

#animate progress
ax = plt.axes(projection='3d')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(0, 1)
for point in fern_model1:
    ax.scatter(*point, c='g', marker='.')
    plt.pause(0.005)
plt.show()




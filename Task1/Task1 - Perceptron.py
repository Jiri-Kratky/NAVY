import numpy as np
import matplotlib.pyplot as plt
import Perceptron
import Functions as fn
from Perceptron import Perceptron


# Generate random x-values and y-values
x_train = np.random.uniform(-10, 10, size=100)
y_train = np.random.uniform(-10, 10, size=100)

# Initialize weights, bias and learning rate
w = np.random.uniform(-1, 1, size=2) #weights, we need 2 because we have 2 features
b = np.random.uniform(-1, 1)
learning_rate = 0.1


# save all results from above_below to array results
results = np.zeros(len(x_train))
for i in range(len(x_train)):
    results[i] = fn.above_below(x_train[i],y_train[i])


perceptron = Perceptron(w, b, learning_rate)
perceptron.Run(x_train, y_train, results)
#perceptron.Run_Epoches(x, y, results,5)


#Generate test points 
x_test = np.random.uniform(-10, 10, size=1000)
y_test = np.random.uniform(-10, 10, size=1000)

#correct test results
test_results = np.zeros(len(x_test))
for i in range(len(x_test)):
    test_results[i] = fn.above_below(x_test[i],y_test[i])

#guess test results
classified_points = []
right=0
for i in range(len(x_test)):
    guess = perceptron.Predict(x_test[i],y_test[i])
    if test_results[i] == guess:
        right+=1
    if guess == 1:
        classified_points.append('red') #above
    elif guess == -1:
        classified_points.append('blue') #below
    else:
        classified_points.append('green') #on the line

print(f"Accuracy: {(right/len(x_test))*100}%")

#plot
plt.scatter(x_test, y_test, c=classified_points)
plt.plot(x_test, fn.line(x_test), color='black')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axhline(0, color='black', lw=1) #highlight x-axis
plt.axvline(0, color='black', lw=1) #highlight y-axis
plt.show()
import numpy as np

def sigmoid (x):
    return 1/(1 + np.exp(-x))

#video k výpočtu Erroru, nové váhy a back-propagation zde: https://www.youtube.com/watch?v=tUoUdOdTkRw

#výpočet chyby...
i_1 = 2
i_2 = 3

w_1, w_2 = 0.5,0.5
w_3, w_4 = 0.2,0.2
w_5, w_6 = 0.3,0.3
w_7, w_8 = 0.4,0.4
w_9 = 0.35
w_10 = 0.45
b = 0.1

o = 0.725

learning_rate=0.1

point1 = sigmoid(i_1 * w_1 + i_2 * w_3 + b)
print("point1: " + str(point1))
point2 = sigmoid(i_1 * w_2 + i_2 * w_4 + b)
print("point2: " + str(point2))
point3 = sigmoid(point1 * w_5 + point2 * w_7 + b)
print("point3: " + str(point3))
point4 = sigmoid(point1 * w_6 + point2 * w_8 + b)
print("point4: " + str(point4))
output = sigmoid(point3 * w_9 + point4 * w_10 + b)

print("Output: " + str(output))
              
error = 0.5 * (o - output) ** 2

print("Error: " + str(error))


#Na základě chyby přepočítejte váhu w_5. Uveďte novou váhu w_5 s přesností na 7 desetinných míst.

s_output = output * (1 - output)* (o - output)
s_point3 = point3 * (1 - point3) * (s_output * w_9)

# Print all variables starting with "s_"
print("s_output: " + str(s_output))
print("s_point3: " + str(s_point3))

#Výpočet chyby 
print("Old weight w_5: {:.7f}".format(w_5))
learning_rate = 0.1
add_w_5 = learning_rate * point1 * s_point3
w_5 = w_5 + add_w_5
print("add_w_5: {:.7f}".format(add_w_5))

print("New weight w_5: {:.7f}".format(w_5))

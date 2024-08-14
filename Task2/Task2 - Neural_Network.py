import numpy as np
import matplotlib.pyplot as plt
import numpy as np 

def sigmoid (x):
    return 1/(1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)


inputs = np.array([[0,0],[0,1],[1,0],[1,1]]) #0-0 -> 0, 0-1 -> 1, 1-0 -> 1, 1-1 -> 0
expected_output = np.array([[0],[1],[1],[0]])

epochs = 10000
learning_rate = 0.1			
inputLayer = 2
hiddenLayer = 2
outputLayer = 1

#Inicializace
hidden_weights = np.random.uniform(size=(inputLayer,hiddenLayer))
hidden_bias =np.random.uniform(size=(1,hiddenLayer))
output_weights = np.random.uniform(size=(hiddenLayer,outputLayer))
output_bias = np.random.uniform(size=(1,outputLayer))

print(f"Initial hidden weights: {hidden_weights[0]} | {hidden_weights[1]}")
print(f"Initial hidden biases: {hidden_bias[0]}")
print(f"Initial output weights: {output_weights[0]} | {output_weights[1]}")
print(f"Initial output biases: {output_bias[0]}")


for _ in range(epochs):
	"""
    Dopředná propagace začíná výpočtem aktivace skryté vrstvy. 
    Nejprve se vynásobí vstupy váhami skrytých neuronů a přičte se bias skryté vrstvy. 
    Poté se výsledek předá funkci sigmoid, která vypočítá výstup skryté vrstvy.
    """
	#Dopředná propagace
	hidden_layer_activation = np.dot(inputs,hidden_weights)
	hidden_layer_activation += hidden_bias
	hidden_layer_output = sigmoid(hidden_layer_activation)

	"""
    Následuje výpočet aktivace výstupní vrstvy. 
    Opět se vynásobí výstup skryté vrstvy váhami výstupních neuronů a přičte se bias výstupní vrstvy. 
    Výsledek je opět předán funkci sigmoid, která vypočítá predikovaný výstup neuronové sítě.
    """
	output_layer_activation = np.dot(hidden_layer_output,output_weights) #Výstup skryté vrstvy je vynásoben vahami výstupní vrstvy a přičten bias výstupní vrstvy.
	output_layer_activation += output_bias
	predicted_output = sigmoid(output_layer_activation)

	"""
    Zpětná propagace, slouží k aktualizaci vah neuronů na základě chyby mezi očekávaným výstupem a predikovaným výstupem. 
    Nejprve se vypočítá chyba jako rozdíl mezi očekávaným výstupem a predikovaným výstupem. 
    Poté se vypočítá derivace sigmoidní funkce pro predikovaný výstup a vynásobí se s chybou. 
    Tím se získá gradient, který se použije k aktualizaci vah neuronů v dalším kroku trénování.
    """
	#Zpětná propagace
	error = expected_output - predicted_output
	gradient_predicted_output = error * sigmoid_derivative(predicted_output) 
	
	error_hidden_layer = gradient_predicted_output.dot(output_weights.T) #Chyba skryté vrstvy je vypočítána derivace sigmoidní funkce pro skrytou vrstvu a vynásobena vahami výstupní vrstvy.
	gradient_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output) #Výsledek je vynásoben chybou skryté vrstvy a vypočítána derivace sigmoidní funkce pro skrytou vrstvu.

	#Updating Weights and Biases
	hidden_weights += inputs.T.dot(gradient_hidden_layer) * learning_rate #Váhy a biasy jsou aktualizovány na základě vstupů a chyby skryté vrstvy.
	hidden_bias += np.sum(gradient_hidden_layer, axis=0, keepdims=True) * learning_rate #Váhy a biasy jsou aktualizovány na základě vstupů a chyby skryté vrstvy.
	output_weights += hidden_layer_output.T.dot(gradient_predicted_output) * learning_rate	#Váhy a biasy jsou aktualizovány na základě výstupu skryté vrstvy a chyby predikovaného výstupu.
	output_bias += np.sum(gradient_predicted_output,axis=0,keepdims=True) * learning_rate #Váhy a biasy jsou aktualizovány na základě výstupu skryté vrstvy a chyby predikovaného výstupu.


print(f"\nFinal hidden weights: {hidden_weights[0]} | {hidden_weights[1]}")
print(f"Final hidden biases: {hidden_bias[0]}")
print(f"Final output weights: {output_weights[0]} | {output_weights[1]}")
print(f"Final output biases: {output_bias[0]}")

print(f"\nOutput after {epochs} epochs: {predicted_output[0]} | {predicted_output[1]} | {predicted_output[2]} | {predicted_output[3]} ")

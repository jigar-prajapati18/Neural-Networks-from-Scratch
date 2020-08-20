import numpy as np 

np.random.seed(0)

x =  [ [1,2,3,2.5],
           [2.0,5.6,-1.0,2.0],
           [-1.4,4.3,3.3,0.8], ]

class layer_Dense:
	def __init__(self,n_inputs,n_neurons):
		self.weights = 0.10 * np.random.randn(n_inputs,n_neurons)
		self.biases = np.zeros((1,n_neurons))

	def forword(self,inputs):
		self.output = np.dot(inputs, self.weights) + self.biases

layer1 = layer_Dense(4,5)
layer2 = layer_Dense(5,2)

layer1.forword(x)

#print(layer1.output)

layer2.forword(layer1.output)

print(layer2.output)
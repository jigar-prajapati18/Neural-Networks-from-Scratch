import numpy as np 

np.random.seed(0)

x =  [ [1,2,3,2.5],
           [2.0,5.6,-1.0,2.0],
           [-1.4,4.3,3.3,0.8], ]

class layer_Dense:
	def __init__(self,n_inputs,n_neurons):
		self.weights = 0.10 * np.random.randn(n_inputs,n_neurons)
		self.biases = np.zeros((1,n_neurons))

	def forward(self,inputs):
		self.output = np.dot(inputs, self.weights) + self.biases

class Activation_Relu:
	def forward(self,inputs):
		self.output = np.maximum(0,inputs)

layer1 = layer_Dense(4,5)
activation1 = Activation_Relu()

layer1.forward(x)

activation1.forward(layer1.output)

print(activation1.output)
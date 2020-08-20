import numpy as np 

training_data = np.array([[0,1,0,],
					   [0,0,1,],
					   [1,0,0,],
					   [1,1,0,],
					   [1,1,1,],
					   [0,1,1,],
					   [0,1,0,], ])

labels = np.array([[1,0,0,1,1,0,1]])
labels = labels.reshape(7,1)

np.random.seed(42)
weights = np.random.rand(3,1)
bias = np.random.rand(1)
Lr = 0.05

#acitivation funcation
def sigmoid(x):
	return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
	return sigmoid(x) * (1-sigmoid(x))

# traing model

for epoch in range(1000):
	inputs = training_data
	op = np.dot(inputs,weights) + bias
	z = sigmoid(op)
	error = z - labels
	#print(error.sum())
	d_cost = error
	d_pred = sigmoid_derivative(z)
	z_del = d_cost + d_cost
	inputs = training_data.T
	weights = weights - Lr*np.dot(inputs,z_del)
	for num in z_del:
		bias = bias - Lr*num

#inputs = training_data
print("weights:",weights)
print("bias:",bias)
#predictingg output

test_data = np.array([0,1,0])
result = sigmoid(np.dot(test_data,weights) + bias)
print(result)






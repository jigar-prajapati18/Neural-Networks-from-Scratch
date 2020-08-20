
#using class method

#multiple layers
import numpy as np
inputs1 = [ [1,2,3,2.5],
           [2.0,5.6,-1.0,2.0],
           [-1.4,4.3,3.3,0.8], ]

weights1 = [ [0.1,0.1,0.1,-0.2],
			[0.1,-0.3,0.4,0.2],
			[0.5,0.5,-0.7,0.3], ]

bias1 = [1,3,0.3]

inputs2 = [ [4,2,3,2.5],
           [3.0,4.6,-1.0,1.0],
           [-3.4,7.3,0.3,3.8], ]

weights2 = [ [0.2,0.6,0.1,-0.2],
			[0.3,-0.2,0.1,0.2],
			[0.6,0.5,-0.4,0.9], ]

bias2 = [2,3,0.5]

layer1 = np.dot(inputs1,np.array(weights1).T) + bias1
layer2 = np.dot(inputs2,np.array(weights2).T) + bias2

print(layer1)
print(layer2)

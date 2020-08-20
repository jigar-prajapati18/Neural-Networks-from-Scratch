
#for single neuron

import numpy as np

"""
inputs = [1.2,5.1,2.1]
weights = [3.1,2.1,8.1]

bias = 3

output = np.dot(inputs,weights) + bias

print(output)

"""
#for multiple neuron

inputs = [1,2,3,2.5]

weights = [ [3.1,2.1,8.1,4.2],
			[2.1,4.3,5.4,3.2],
			[3.5,5.5,2.7,7.3], ]

bias = [2,3,0.5]

output = [ np.dot(inputs,weights[0]) + bias[0] ,
		   np.dot(inputs,weights[1]) + bias[1] ,
		   np.dot(inputs,weights[2]) + bias[2] 
]

print(output)

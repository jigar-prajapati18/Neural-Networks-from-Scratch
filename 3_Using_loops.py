
#using for loop

inputs = [1,2,3,2.5]

weights = [ [3.1,2.1,8.1,4.2],
			[2.1,4.3,5.4,3.2],
			[3.5,5.5,2.7,7.3], ]

bias = [2,3,0.5]

layer_output = []

for nearon_weights , neuron_bias in zip(weights,bias):
	neuron_output= 0
	for n_inputs, weight in zip(inputs,nearon_weights):
		neuron_output  += n_inputs * weight

	neuron_output += neuron_bias
	layer_output.append(neuron_output)

print(layer_output)

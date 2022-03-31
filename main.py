import copy
import json 
import os

import Gate
import reading_functions as read

import Circuit

chassis_name = 'Eco1C1G1T1'
input_dir = os.getcwd() + '/input/' 


# Get input signals from *.input.json file
input_signals = read.read_input_json(input_dir + chassis_name + '.input.json')[0]
print(type(input_signals))
       
# Get output signals from *.output.json file
output_signals = read.read_output_json(input_dir + chassis_name + '.output.json')[0]

    
# Get assignment from *.UCF.json file
ucf_signals = read.read_ucf_json(input_dir + chassis_name + '.UCF.json')[0]


gate_a = input_signals['pTet']
gate_b = input_signals['pTet']
gate_c = ucf_signals['H1_HlyIIR']

# gate_c.assign_input(gate_a)   
# gate_c.assign_input(gate_b)

c = Circuit.Circuit()
c.addVertex(gate_a)
c.addVertex(gate_b)
c.addVertex(gate_c)
c.addEdge(gate_a,gate_c)
c.addEdge(gate_b,gate_c)
#c.BFS(gate_c)




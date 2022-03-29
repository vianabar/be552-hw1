import copy
import json 
import os

import Gate
import reading_functions as read

chassis_name = 'Eco1C1G1T1'
input_dir = os.getcwd() + '/input/' 


# Get input signals from *.input.json file
input_signals = read.read_input_json(input_dir + chassis_name + '.input.json')

       
# Get output signals from *.output.json file
output_signals = read.read_output_json(input_dir + chassis_name + '.output.json')

    
# Get assignment from *.UCF.json file
ucf_signals = read.read_ucf_json(input_dir + chassis_name + '.UCF.json')

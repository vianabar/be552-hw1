import json 
import os

chassis_name = 'Eco1C1G1T1'
input_dir = os.getcwd() + '/input/' 


ucf_file = open(input_dir + chassis_name + '.UCF.json')
input_file = open(input_dir + chassis_name + '.input.json')
output_file = open(input_dir + chassis_name + '.output.json')


data = json.load(input_file)

for i in range(len(data)):
    print(data[i])    
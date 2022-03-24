import json 
import os

chassis_name = 'Eco1C1G1T1'
input_dir = os.getcwd() + '/input/' 


ucf_file = open(input_dir + chassis_name + '.UCF.json')
input_file = open(input_dir + chassis_name + '.input.json')
output_file = open(input_dir + chassis_name + '.output.json')



# Get input signals from *.input.json file
input_data = json.load(input_file)

for i in range(len(input_data)):
    collection = (input_data[i]['collection']) 
    
    
    
'''
collection = (data[0]['collection'])
print(collection)
data[0]['collection'] = 'frog_sensors'
print(data[0]['collection'])
'''
# Get output signals from *.output.json file





# Get assignment
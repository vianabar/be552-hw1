import json 
import os

chassis_name = 'Eco1C1G1T1'
input_dir = os.getcwd() + '/input/' 


chassis_file = open(input_dir + 'Eco1C1G1T1.UCF.json')

data = json.load(chassis_file)

for i in data['collection']:
    print(i)    
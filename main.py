import json 
import os

chassis_file = open('Eco1C1G1T1.UCF.json')

data = json.load(chassis_file)

for i in data['collection']:
    print(i)
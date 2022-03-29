import json
import os

import Gate


def read_input_json(path):
    # Get input signals from *.input.json file
    input_file = open(path)
    input_data = json.load(input_file)

    input_sensors = []
    input_models = []
    input_structures = []
    input_functions = []
    input_parts = []

    for i in range(len(input_data)):
        
        
        collection = (input_data[i]['collection']) 
        
        if collection == 'input_sensors':
            input_sensors.append(input_data[i])
        elif collection == 'models':
            input_models.append(input_data[i])
        elif collection == 'structures':
            input_structures.append(input_data[i])
        elif collection == 'functions':
            input_functions.append(input_data[i])
        elif collection == 'parts':
            input_parts.append(input_data[i])
        
    input_signals = []

    for i in range(len(input_structures)):
        name = input_structures[i]['outputs'][0]
        ymax = None
        ymin = None
        n = None
        k = None
        gate_type = 'Input'
        for j in range(len(input_models)):
            models_label = input_models[j]['name']
            structures_label = input_structures[i]['name']
            if models_label[:len(models_label) - 13] == structures_label[:len(structures_label) - 17]:
                for k in range(len(input_models[j]['parameters'])):
                    if input_models[j]['parameters'][k]['name'] == 'ymax':
                        ymax = input_models[j]['parameters'][k]['value']
                    elif input_models[j]['parameters'][k]['name'] == 'ymin':
                        ymin = input_models[j]['parameters'][k]['value']
                    elif input_models[j]['parameters'][k]['name'] == 'alpha':
                        n = input_models[j]['parameters'][k]['value']
                    elif input_models[j]['parameters'][k]['name'] == 'beta':
                        k = input_models[j]['parameters'][k]['value']
        
        input_signal = Gate.Gate(name, ymax, ymin, n, k, gate_type)
        input_signals.append(input_signal)
    
    input_file.close()
    return input_signals


def read_output_json(path):
    # Get output signals from *.output.json file
    output_file = open(path)
    output_data = json.load(output_file)

    output_devices = []
    output_models = []
    output_structures = []
    output_functions = []
    output_parts = []

        
    for i in range(len(output_data)):

        collection = (output_data[i]['collection'])

        if collection == 'output_devices':
            output_devices.append(output_data[i])
        elif collection == 'models':
            output_models.append(output_data[i])
        elif collection == 'structures':
            output_structures.append(output_data[i])
        elif collection == 'functions':
            output_functions.append(output_data[i])
        elif collection == 'parts':
            output_parts.append(output_data[i])
            
    output_signals = []

    for i in range(len(output_models)):
        name = output_models[i]['name']
        name = name[:len(name) - 15]
        
        output_signal = Gate.Gate(name, None, None, None, None, 'Output')
        output_signals.append(output_signal)
        
    output_file.close()
    return output_signals


def read_ucf_json(path):
    # Get assignment from *.UCF.json file
    ucf_file = open(path)
    ucf_data = json.load(ucf_file)

    ucf_headers = []
    ucf_meas_stds = []
    ucf_logic_consts = []
    ucf_motif_libs = []
    ucf_gen_locs = []
    ucf_gates = []
    ucf_models = []
    ucf_functions = []
    ucf_structures = []
    ucf_parts = []
    ucf_device_rules = []
    ucf_circuit_rules = []


    for i in range(len(ucf_data)):

        collection = (ucf_data[i]['collection'])

        if collection == 'header':
            ucf_headers.append(ucf_data[i])
        elif collection == 'measurement_std':
            ucf_meas_stds.append(ucf_data[i])
        elif collection == 'logic_constraints':
            ucf_logic_consts.append(ucf_data[i])
        elif collection == 'motif_library':
            ucf_motif_libs.append(ucf_data[i])
        elif collection == 'genetic_locations':
            ucf_gen_locs.append(ucf_data[i])
        elif collection == 'gates':
            ucf_gates.append(ucf_data[i])
        elif collection == 'models':
            ucf_models.append(ucf_data[i])
        elif collection == 'structures':
            ucf_structures.append(ucf_data[i])
        elif collection == 'functions':
            ucf_functions.append(ucf_data[i])
        elif collection == 'parts':
            ucf_parts.append(ucf_data[i])
        elif collection == 'device_rules':
            ucf_device_rules.append(ucf_data[i])
        elif collection == 'circuit_rules':
            ucf_circuit_rules.append(ucf_data[i])
        
    ucf_signals = []

    for i in range(len(ucf_gates)):
        name = ucf_gates[i]['name']
        ymax = None
        ymin = None
        n = None
        k = None
        gate_type = ucf_gates[i]['gate_type']
        for j in range(len(ucf_models)):
            if ucf_models[j]['name'] == ucf_gates[i]['model']:
                for k in range(len(ucf_models[j]['parameters'])):
                    if ucf_models[j]['parameters'][k]['name'] == 'ymax':
                        ymax = ucf_models[j]['parameters'][k]['value']
                    elif ucf_models[j]['parameters'][k]['name'] == 'ymin':
                        ymin = ucf_models[j]['parameters'][k]['value']
                    elif ucf_models[j]['parameters'][k]['name'] == 'alpha':
                        n = ucf_models[j]['parameters'][k]['value']
                    elif ucf_models[j]['parameters'][k]['name'] == 'beta':
                        k = ucf_models[j]['parameters'][k]['value']
        
        ucf_signal = Gate.Gate(name, ymax, ymin, n, k, gate_type)
        ucf_signals.append(ucf_signal)
        
    ucf_file.close()
    return ucf_signals
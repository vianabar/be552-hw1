1. What it does:

	This project is an implementation of a genetic circuit design program that takes in a library of genetic input signals, response function (UCF) logic gates, and output signals defined by the user in three input, UCF, and output JSON files. The user is able to create a single genetic circuit using genetic parts from this library by uploading a text file that specifies which parts are being used, how each part is connected, and what operations are done on each part. 

	Input signals can only be used as inputs to UCF gates, while UCF gates can take in up to two input signals or gates. UCF gates are currently supported as AND, OR, NOT, NOR gates. The truth table of each UCF gate is calculated based on the input values as well as the ymin, ymax, alpha, and beta values of the UCF gate itself. One output signal must be connected to a singular UCF gate, in which the output signal’s score represents the score of the overall circuit. The higher the score, the closer the circuit’s behavior resembles a boolean function.

    Operations are simulations of DNA (stronger/weaker promoter, stronger/weaker ribosome binding site) and protein engineering (stretch, increase/decrease slope) techniques. Operations can either be done in the genetic circuit file or directly in the program GUI.scor
	
	
2. Installation:

    conda create -n newenv python
    conda activate newenv
    pip install -r requirements.txt  
        
	https://github.com/vianabar/be552-hw1.git

3. How to use:

    3.1. Preparing libraries:
        Three parts library files must be created in the form for the program to work:
            <chassis organism name>.input.json 
            <chassis organism name>.UCF.json
            <chassis organism name>.output.json

        Read https://www.nature.com/articles/s41596-021-00675-2, Supplementary Information: Section 6


    3.2. Preparing genetic circuit files:
        
        Genetic circuit files are in “.txt” form. 

    To create an input signal (example):
        gate_a = copy.deepcopy(input_signals['pTet'])
        gate_b = copy.deepcopy(input_signals['pLuxStar'])

        To create a UCF gate (example): 
            gate_c = copy.deepcopy(ucf_signals['S1_SrpR'])
        
        To create an output signal (example):
            gate_d = copy.deepcopy(output_signals['YFP'])

        To add a signal or gate to the circuit (example):
            
            c.addVertex(gate_a)
            c.addVertex(gate_b)
            c.addVertex(gate_c)
            c.addVertex(gate_d)
            
        To connect an input signal/gate to an output signal/gate in form (example):
        
            c.addEdge(gate_a,gate_c)
    c.addEdge(gate_b,gate_c)
    c.addEdge(gate_c,gate_d)

        To perform an operation on a gate/signal (example): 
            c.operate(<operation string>, x_value, gate_a)

    **Operation strings are ‘stretch’ (x <= 1.5), ‘increase_slope’ (x <= 1.05), ‘decrease_slope(x <= 1.05), ‘stronger_prom’, ‘weaker_prom’, ‘stronger RBS’, ‘weaker_RBS’

3.3. Running the program:
	
    Start the program with the following command:

        python GUI.py -l <path to directory containing input, UCF, and output JSON files> -c <chassis name>

    To create a new genetic circuit, press the “Upload file” button and search for the 
    desired genetic circuit file which contains all of the commands to executed.

    To generate the genetic circuit file:

    Press the “Design circuit” button which creates a graph containing all of the gates as nodes and the assigned connections as edges. BFS is then performed on the graph to produce details about each gate (name, gate type, ON Min, OFF Max, n, k) and their corresponding truth table. 

    These statistics will be displayed on the “Main Frame” of the GUI for the user to view. The graph is also drawn with the help of networkx library and displayed on the “Circuit Visualization” frame.

    To perform operations on the gates:

    Choose the gate that you want to modify in the “Select gate to modify” combobox.

    Choose the operation to perform in the “Select operation to perform” combobox.

    Enter the appropriate x value for the operation in the entry widget.

    Press “Perform Operation”.




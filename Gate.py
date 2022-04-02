import math

def round_sig(x, sig=5):
    return round(x, sig-int(math.floor(math.log10(abs(x))))-1)

# Gate class for input signals, UCF gates, and output signals
class Gate:
    def	__init__(self, name, ymax, ymin, n, k, gate_type):
        self.name = name
        self.ymax = ymax
        self.ymin = ymin
        self.n = n
        self.k = k
        self.gate_type = gate_type
        
        self.inputs = []
        self.on_min = None
        self.off_max = None
        self.truth_table = None
        self.truth_table_bool = None
        self.score = None
        
        if self.gate_type != 'Output':
            self.calculate_truth_table()
            self.calculate_score()
            
# Prints gate class (purpose-made for graph display in UI)
    def __str__(self):
        
        return str(self.name) + '\n' + \
               str(self.gate_type) +'\n\n'

# Used in BFS() to print the total statistics of each signal/gate
    def get_stats(self): 
        if self.gate_type == 'Output':
            return "Name: " + str(self.name) + '\n' + \
                "Gate Type: " + str(self.gate_type) + '\n' + \
                "Inputs: " + ', '.join(input.name for input in self.inputs) + '\n' + \
                "ON Min: " + str(self.on_min) + '\n' + \
                "OFF Max: " + str(self.off_max) + '\n' + \
                "Output Score: " + str(self.score) + '\n\n' 

        else:
            return "Name: " + str(self.name) + '\n' + \
                "Ymax: " + str(self.ymax) + '\n' + \
                "Ymin: " + str(self.ymin) + '\n' + \
                "n: " + str(self.n) + '\n' + \
                "k: " + str(self.k) + '\n' + \
                "Gate Type: " + str(self.gate_type) + '\n' + \
                "Inputs: " + ', '.join(input.name for input in self.inputs) + '\n' + \
                "Truth Table: " + '\n' + \
                self.print_truth_table() + '\n\n'

# Prints truth table for UCF gates 
    def print_truth_table(self):
        truth_table_str = ""
        
        if len(self.inputs) == 0 or self.gate_type == 'Output':
            truth_table_str = "No Truth Table"
        elif len(self.inputs) == 1:
            truth_table_str = "| " + str(self.inputs[0].name) + str(" " * (12 - len(self.inputs[0].name))) + " | " + str(self.name) + str(" " * (12 - len(self.name))) + " |" + "\n" + \
                              "| " + str(" " * 12) + " | " + str(" " * 12) + " |" + "\n" + \
                              "| " + str(round_sig(self.inputs[0].off_max)) + str(" " * (12 - len(str(round_sig(self.inputs[0].off_max))))) + " | " +  str(round_sig(self.truth_table[0])) + str(" " * (12 - len(str(round_sig(self.truth_table[0]))))) + " |" + "\n" + \
                              "| " + str(" " * 12) + " | " + str(" " * 12) + " |" + "\n" + \
                              "| " + str(round_sig(self.inputs[0].on_min)) + str(" " * (12 - len(str(round_sig(self.inputs[0].on_min))))) + " | " +  str(round_sig(self.truth_table[1])) + str(" " * (12 - len(str(round_sig(self.truth_table[1]))))) + " |" + "\n" + \
                              "| " + str(" " * 12) + " | " + str(" " * 12) + " |" + "\n"
        elif len(self.inputs) == 2:
            truth_table_str = "| " + str(self.inputs[0].name) + str(" " * (12 - len(self.inputs[0].name))) + " | " + str(self.inputs[1].name) + str(" " * (12 - len(self.inputs[1].name))) + " | " + str(self.name) + str(" " * (12 - len(self.name))) + " |" + "\n" + \
                              "| " + str(" " * 12) + " | " + str(" " * 12) + " | " + str(" " * 12) + " |" + "\n" + \
                              "| " + str(round_sig(self.inputs[0].off_max)) + str(" " * (12 - len(str(round_sig(self.inputs[0].off_max))))) + " | " +  str(round_sig(self.inputs[1].off_max)) + str(" " * (12 - len(str(round_sig(self.inputs[1].off_max))))) + " | " +  str(round_sig(self.truth_table[0])) + str(" " * (12 - len(str(round_sig(self.truth_table[0]))))) + " |" + "\n" + \
                              "| " + str(" " * 12) + " | " + str(" " * 12) + " | " + str(" " * 12) + " |" + "\n" + \
                              "| " + str(round_sig(self.inputs[0].off_max)) + str(" " * (12 - len(str(round_sig(self.inputs[0].off_max))))) + " | " +  str(round_sig(self.inputs[1].on_min)) + str(" " * (12 - len(str(round_sig(self.inputs[1].on_min))))) + " | " +  str(round_sig(self.truth_table[1])) + str(" " * (12 - len(str(round_sig(self.truth_table[1]))))) + " |" + "\n" + \
                              "| " + str(" " * 12) + " | " + str(" " * 12) + " | " + str(" " * 12) + " |" + "\n" + \
                              "| " + str(round_sig(self.inputs[0].on_min)) + str(" " * (12 - len(str(round_sig(self.inputs[0].on_min))))) + " | " +  str(round_sig(self.inputs[1].off_max)) + str(" " * (12 - len(str(round_sig(self.inputs[1].off_max))))) + " | " +  str(round_sig(self.truth_table[2])) + str(" " * (12 - len(str(round_sig(self.truth_table[2]))))) + " |" + "\n" + \
                              "| " + str(" " * 12) + " | " + str(" " * 12) + " | " + str(" " * 12) + " |" + "\n" + \
                              "| " + str(round_sig(self.inputs[0].on_min)) + str(" " * (12 - len(str(round_sig(self.inputs[0].on_min))))) + " | " +  str(round_sig(self.inputs[1].on_min)) + str(" " * (12 - len(str(round_sig(self.inputs[1].on_min))))) + " | " +  str(round_sig(self.truth_table[3])) + str(" " * (12 - len(str(round_sig(self.truth_table[3]))))) + " |" + "\n" + \
                              "| " + str(" " * 12) + " | " + str(" " * 12) + " | " + str(" " * 12) + " |"
                
        return truth_table_str

    def change_name(self, new_name):
        self.name = new_name

# DNA and protein engineering operations
    def stretch(self, x):
        if (x > 1.5):
            raise ValueError("x can be at-most 1.5")

        self.ymax = self.ymax * x
        self.ymin = self.ymin / x

        self.calculate_truth_table()
        self.calculate_score()

    def increase_slope(self, x):
        if (x > 1.05):
            raise ValueError("x can be at-most 1.05")

        self.n = self.n * x

        self.calculate_truth_table()
        self.calculate_score()

    def decrease_slope(self, x):
        if (x > 1.05):
            raise ValueError("x can be at-most 1.05")

        self.n = self.n / x

    def stronger_prom(self, x):
        self.ymax = self.ymax * x
        self.ymin = self.ymin * x

        self.calculate_truth_table()
        self.calculate_score()

    def weaker_prom(self, x):
        self.ymax = self.ymax / x
        self.ymin = self.ymin / x

        self.calculate_truth_table()
        self.calculate_score()

    def stronger_RBS(self, x):
        self.k = self.k / x

        self.calculate_truth_table()
        self.calculate_score()

    def weaker_RBS(self, x):
        self.k = self.k * x

        self.calculate_truth_table()
        self.calculate_score()
    
# Connects input nodes to output node, limit to 0-2 inputs
    def assign_input(self, gate=None):
        if (len(self.inputs) >= 2):
            raise ValueError("Exceeded Maximum of 2 Inputs")
        if gate is not None:
            self.inputs.append(gate)
        
        if self.gate_type != 'Output':
            self.calculate_truth_table()
        self.calculate_score()

# Disconnects inputs
    def erase_inputs(self):
        self.inputs = []
        self.calculate_truth_table()
        self.calculate_score()

# Helper function to calculate response
    def calculate_y(self, in_0, in_1):
        
        x = in_0 + in_1
        
        output = self.ymin + ((self.ymax - self.ymin) / 
                                  (1.0 + (x/self.k) ** self.n))
        
        return output
    
# Calculate truth table
    def calculate_truth_table(self):
        
        # Zero inputs
        if len(self.inputs) == 0 or self.gate_type == 'Output':
            self.truth_table = None
            self.truth_table_bool = None
            
        # One input
        elif len(self.inputs) == 1:
            self.truth_table = [self.calculate_y(self.inputs[0].off_max, 0),
                                self.calculate_y(self.inputs[0].on_min, 0)]
            
            if self.gate_type == 'OR' or self.gate_type == 'AND':
                ## |0| =  |0|
                ## |1|    |1|
                self.truth_table_bool = [0, 1]
                
            elif self.gate_type == 'NOT' or 'NOR':                     
                ## |0|| = |1|
                ## |1|    |0|
                self.truth_table_bool = [1, 0]

        
        # Two inputs
        elif len(self.inputs) == 2:
            self.truth_table = [self.calculate_y(self.inputs[0].off_max, 
                                                 self.inputs[1].off_max),
                                self.calculate_y(self.inputs[0].off_max,
                                                 self.inputs[1].on_min),
                                self.calculate_y(self.inputs[0].on_min,
                                                 self.inputs[1].off_max),
                                self.calculate_y(self.inputs[0].on_min,
                                                 self.inputs[1].on_min)]
            if self.gate_type == 'OR':
                ## |0|0| = |0|
                ## |0|1|   |1|
                ## |1|0|   |1|
                ## |1|1|   |1|
                self.truth_table_bool = [0, 1, 1, 1]
               
            elif self.gate_type == 'AND':
                ## |0|0| = |0|
                ## |0|1|   |0|
                ## |1|0|   |0|
                ## |1|1|   |1|
                self.truth_table_bool = [0, 0, 0, 1]
              
                                        
            elif self.gate_type == 'NOR':
                ## |0|0| = |1|
                ## |0|1|   |0|
                ## |1|0|   |0|
                ## |1|1|   |0|
                self.truth_table_bool = [1, 0, 0, 0]

    #Calculate output score using truth table and truth_table_bool
    def calculate_score(self):
        
        # Output
        if self.gate_type == 'Output':
            self.on_min = self.inputs[0].on_min
            self.off_max = self.inputs[0].off_max
            self.score = math.log(self.on_min/self.off_max)
        
        # Input
        elif len(self.inputs) == 0:
            self.off_max = self.ymin
            self.on_min = self.ymax
            self.score = math.log(self.on_min/self.off_max)
        

        # UCF Gate with Inputs Connected
        elif len(self.inputs) > 0:
            off_vals = []
            on_vals = []
            for i in range(len(self.truth_table_bool)):
                if self.truth_table_bool[i] == 0:
                    off_vals.append(self.truth_table[i])
                elif self.truth_table_bool[i] == 1:
                    on_vals.append(self.truth_table[i])
            
            self.off_max = max(off_vals)
            self.on_min = min(on_vals)
            self.score = math.log(self.on_min/self.off_max)
                     


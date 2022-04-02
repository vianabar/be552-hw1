from collections import defaultdict
import math
import networkx as nx
import matplotlib.pyplot as plt

import Gate


# Adapted from: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

# Circuit class is a graph of signal/gate vertices
# Graph actually takes shape of a tree in which output is root, UCF gates are children in between,
# Input signals are leaves

class Circuit:
    def	__init__(self):
        self.adjList = defaultdict(list) #adjacency list
        self.V = 0 #num of vertices
        self.visited = dict()
        self.visual = []
        self.root = None
    
# Clear Circuit class to reset 
    def clear(self):
        self.adjList = defaultdict(list) #adjacency list
        self.V = 0 #num of vertices
        self.visited = dict()
        self.visual = []
        self.root = None
    
# Add gate/signal to circuit
    def addVertex(self, gate):
        self.V = self.V + 1
        new_name = gate.name + ': 0'
        gate.name = new_name
        while gate.name in self.adjList: # if gate: num exists, assign new 
            gate.name = gate.name[:-1] + str(int(gate.name[-1]) + 1)

        self.adjList[gate.name] = gate.inputs
        self.visited[gate.name] = False
        if gate.gate_type == 'Output':
            self.root = gate

# Add connection between gates and signals
    def addEdge(self, in_gate, out_gate):
        out_gate.assign_input(in_gate)
        self.adjList[out_gate.name] = out_gate.inputs
        temp = [in_gate, out_gate]
        self.visual.append(temp); 

    def visualize(self):
        G = nx.DiGraph()
        G.add_edges_from(self.visual)
        return G

# Breadth-First-Search to print statistics of gates and signals
# Starting with the output signal first, then backtracking
    def BFS(self): 
        circuit_str = ""
        
        s = self.root
        
        for vertex in self.adjList:
            self.visited[vertex] = False

        queue = []

        queue.append(s)
        self.visited[s.name] = True

        while queue:

            s = queue.pop(0)

            circuit_str =  circuit_str + s.get_stats()

            for i in self.adjList[s.name]:
                if self.visited[i.name] == False:
                    queue.append(i)
                    self.visited[i.name] == True
        
        return circuit_str

        '''
        self.visualize()
        '''

# Recursively calculate truth table/score for gates/signals,
# Starting from input signal leaf nodes and ending at ouput signal
# Root node
    def post_order_score(self, output_gate):
        for input_gate in output_gate.inputs:
            self.post_order_score(input_gate)
        output_gate.calculate_truth_table()
        output_gate.calculate_score()

# Find a gate of a certain name through BFS, useful for 
# doing operations on specific gates through UI
    def BFS_find(self, gate_name): # input s is output_gate
        
        s = self.root
        
        for vertex in self.adjList:
            self.visited[vertex] = False

        queue = []

        queue.append(s)
        self.visited[s.name] = True

        while queue:

            s = queue.pop(0)

            if s.name == gate_name:
                return s

            for i in self.adjList[s.name]:
                if self.visited[i.name] == False:
                    queue.append(i)
                    self.visited[i.name] == True
        
        return


# Do operation on a UCF gate or input signal, recursively
# calculate score
    
    def operate(self, operation, x, gate):
        if operation == "stretch":
            gate.stretch(x)
        elif operation == "increase_slope":
            gate.increase_slope(x)
        elif operation == "decrease_slope":
            gate.decrease_slope(x)
        elif operation == "stronger_prom":
            gate.stronger_prom(x)
        elif operation == "weaker_prom":
            gate.weaker_prom(x)
        elif operation == "stronger_RBS":
            gate.stronger_RBS(x)
        elif operation == "weaker_RBS":
            gate.weaker_RBS(x)

        self.post_order_score(self.root)
        self.BFS()

        




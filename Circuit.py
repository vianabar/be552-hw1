from collections import defaultdict
import math
import networkx as nx
import matplotlib.pyplot as plt

import Gate


# Adapted from: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

class Circuit:
    def	__init__(self):
        self.adjList = defaultdict(list) #adjacency list
        self.V = 0 #num of vertices
        self.visited = dict()
        self.visual = []
        self.root = None

    def addVertex(self, gate):
        self.V = self.V + 1
        new_name = gate.name + ': 0'
        gate.name = new_name
        if gate.name in self.adjList: # if gate: num exists, assign new 
            new_name = gate.name[:-1] + str(int(gate.name[-1]) + 1)
            gate.name = new_name

        self.adjList[gate.name] = gate.inputs
        self.visited[gate.name] = False
        if gate.gate_type == 'Output':
            self.root = gate

    def addEdge(self, in_gate, out_gate):
        out_gate.assign_input(in_gate)
        self.adjList[out_gate.name] = out_gate.inputs
        temp = [in_gate, out_gate]
        self.visual.append(temp); 

    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()

    def BFS(self): # input s is output_gate
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
    
    





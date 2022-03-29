from collections import defaultdict
import math

import Gate

# Adapted from: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

class Circuit:
    def	__init__(self):
        self.adjList = defaultdict(list) #adjacency list
        self.V = 0 #num of vertices
        self.visited = dict()

    def addVertex(self, gate):
        self.V = self.V + 1
        if gate.name in self.adjList: # if gate: num exists, assign new 
            new_name = gate.name[:-1] + str(int(gate.name[-1]) + 1)
            gate.change_name(new_name)

        self.adjList[gate.name] = gate.inputs
        self.visited[gate.name] = False

    def addEdge(self, in_gate, out_gate):
        out_gate.assign_input(in_gate)
        self.adjList[out_gate.name] = out_gate.inputs
        
        
    def BFS(self, s): # input s is output_gate
        for vertex in self.adjList:
            self.visited[vertex.name] = False

        queue = []

        queue.append(s)
        self.visited[s.name] = True

        while queue:

            s = queue.pop(0)

            print(s)

            for i in self.adjList[s.name]:
                if self.visited[i.name] == False:
                    queue.append(i)
                    self.visited[i.name] == True






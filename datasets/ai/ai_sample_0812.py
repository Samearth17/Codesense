"""
Calculate the shortest path from source to destination using Dijkstra's Algorithm.
"""

# Python program for Dijkstra's single 
# source shortest path algorithm. The program is 
# for adjacency matrix representation of the graph 
  
# Library for INT_MAX 
import sys 
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = graph
  
    # A utility function to find the vertex with 
    # minimum distance value, from the set of vertices 
    # not yet included in shortest path tree 
    def minDistance(self, dist, mstSet): 
  
        # Initilaize minimum distance for next node 
        min = sys.maxint 
  
        # Search not nearest vertex not in the 
        # shortest path tree 
        for v in range(self.V): 
            if dist[v] < min and mstSet[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index 
  
    # Funtion that implements Dijkstra's single source 
    # shortest path algorithm for a graph represented  
    # using adjacency matrix representation 
    def dijkstra(self, source): 
  
        dist = [sys.maxint] * self.V 
        dist[source] = 0
        mstSet = [False] * self.V 
  
        for cout in range(self.V): 
  
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.minDistance(dist, mstSet) 
  
            # Put the minimum distance vertex in the  
            # shotest path tree 
            mstSet[u] = True
  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                if self.graph[u][v] > 0 and mstSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                        dist[v] = dist[u] + self.graph[u][v] 
  
        # print the constructed distance array 
        print ("Shortest path from %s to %s is %d" % (source, dest, dist[dest]))
  
# Driver program 
graph = { 
    'a': {'b':10, 'c':3}, 
    'b': {'c':1, 'd':2}, 
    'c': {'b':4, 'd':8, 'e':2}, 
    'd': {'e':7}, 
    'e': {'d':9} 
    }

g = Graph(len(graph))
source = "a"
dest = "d"
g.dijkstra(graph.index(source))
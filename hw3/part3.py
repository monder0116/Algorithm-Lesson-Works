# -*- coding: utf-8 -*-
#!/usr/bin/python


def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    gezilen = []
    # keep track of nodes to be checked
    queue = [start]
    while queue:
        # pop shallowest node (first node) from queue
        vertex = queue.pop(0)
        if vertex not in gezilen:
            komsular = graph[vertex]
            gezilen.append(vertex)
            for komsu in komsular:
                queue.append(komsu)
                
    return sorted(gezilen)
def getUnConnectedGraps(graph):
  unConnectedgraphs=[]
  for key in graph:
    bfsresult=bfs_connected_component(graph,key)
    if bfsresult not in unConnectedgraphs:
        unConnectedgraphs.append(bfsresult)
  return unConnectedgraphs

mapOfGTU = {  1 : set([2,3]),     
              2 : set([1,3,4]),     
              3 : set([1,2,4]),     
              4 : set([3,2]),     
              5 : set([6]),     
              6 : set([5]) } # graph is initialized as dictionar
# visits all the nodes of a graph (connected component) using BFS

print(getUnConnectedGraps(mapOfGTU))
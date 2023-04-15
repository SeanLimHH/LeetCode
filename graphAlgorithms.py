import graphs
'''
Imports graphs.py in the same directory and uses its graph adjacency list implementation for the following algorithms.

Steps to use:
1: Call and set a graph to graphs.buildGraph(noOfVertices, isDirectional, isWeighted) to build the graph.
2. Call the graph.addEdge(sourceNode, destinationNode, weightIfApplicable = 0) to add EACH edge

Example:

graph = graphs.buildGraph(4,1,1)
graph.addEdge("A","B",2)

Then after adding edges, to show the adjacency list, you can call:

graph.printEdges()

To use certain algorithms like bfs, you can call:

graph.bfs()

Example 2:

graph2 = graphs.buildGraph(3,1,0)
graph2.addEdge("A","B")
graph2.addEdge("B","C")
graph2.addEdge("B","E")
graph2.addEdge("B","D")
graph2.addEdge("D","F")
graph2.printEdges()
graphs.bfs(graph2,"D")
'''
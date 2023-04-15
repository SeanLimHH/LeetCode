
import heapq
class Graph:
    def __init__(self, noOfVertices, isWeighted, isDirectional):
        self.noOfVertices = noOfVertices
        self.weighted = isWeighted
        self.directional = isDirectional
        self.adjacencyList = {} # We use adjacency list to represent the edges
        
    
    # For below, choose either of the adding operations. This determines the behaviour of your graph.
    def addEdge(self, source, destination, weight = 0): # Builder for edges
        try:
            weight = int(weight)
        except ValueError:
            print("Please enter a valid integer for the weight in the third input!")
            return False
    
        if self.weighted == 0 and self.directional == 1: # Directed, unweighted edges
            self.addUnweightedEdge(source, destination)
        
        if self.weighted == 0 and self.directional == 0: # Bidirectional, unweighted edges
            self.addBidirectionalUnweightedEdge(source, destination)

        if self.weighted == 1 and self.directional == 1: # Directed, weighted edges
            self.addWeightedEdge(source, destination, weight)

        if self.weighted == 1 and self.directional == 0: # Bidirectional, weighted edges
            self.addBidirectionalWeightedEdge(source, destination, weight)


    # TODO: In the future i can add an addEdges function to quickly add multiple edges.

    def addUnweightedEdge(self, source, destination): # 1 direction, no weights.
        if source not in self.adjacencyList:
            self.adjacencyList[source] = []
        if destination not in self.adjacencyList:
            self.adjacencyList[destination] = []
        self.adjacencyList[source].append(destination)
    
    def addBidirectionalUnweightedEdge(self, source, destination):
        if source not in self.adjacencyList:
            self.adjacencyList[source] = []
        if destination not in self.adjacencyList:
            self.adjacencyList[destination] = []
        self.adjacencyList[source].append(destination)
        self.adjacencyList[destination].append(source)
    
    def addWeightedEdge(self, source, destination, weight):
        if source not in self.adjacencyList:
            self.adjacencyList[source] = []
        if destination not in self.adjacencyList:
            self.adjacencyList[destination] = []
        self.adjacencyList[source].append((destination, weight))

    def addBidirectionalWeightedEdge(self, source, destination, weight):
        if source not in self.adjacencyList:
            self.adjacencyList[source] = []
        if destination not in self.adjacencyList:
            self.adjacencyList[destination] = []
        self.adjacencyList[source].append((destination, weight))
        self.adjacencyList[destination].append((source, weight))

    def printEdges(self): # Prints in adjacency list
        print()
        print("These are the current edges:")
        for v in self.adjacencyList:
            print("Vertex " + str(v) + " :",self.adjacencyList[v])
        print("Note: These represent adjacencyList[node] for each node.")



def buildGraph(noOfVertices, isDirectional, isWeighted):
    print()
    try:
        noOfVertices = int(noOfVertices)
    except ValueError:
        print("Please enter a valid integer for the first input!")
        print("Input 1 represents the number of vertices.")
        return False
    
    try:
        isDirectional = int(isDirectional)
    except ValueError:
        print("Please enter a valid integer for the second input!")
        print("Input 2 represents whether the graph's edges are directed. If so, input as 1, else input as 0.")
        return False
    
    try:
        isWeighted = int(isWeighted)
    except ValueError:
        print("Please enter a valid integer for the third input!")
        print("Input 3 represents whether the graph's edges are weighted. If so, input as 1, else input as 0.")
        return False

    # At this point all three inputs are integers

    if noOfVertices <= 1:
        print("Please enter a positive integer > 1 for the first input!")
        return False
    
    if isDirectional != 0 and isDirectional != 1:
        print("Please enter either a 0 or 1 for the second input!")
        return False
    
    if isWeighted != 0 and isWeighted != 1:
        print("Please enter either a 0 or 1 for the third input!")
        return False
    
    print("Your graph you built has these properties:")
    print(f"Number of vertices: {noOfVertices}")

    if isWeighted:
        if isDirectional: # Directed weighted graph
            print("It is weighted.")
            print("It has direction.")
            return Graph(noOfVertices, 1, 1)

        if not isDirectional: # Bidrectional weighted graph
            print("It is weighted.")
            print("It bidirectional.")
            return Graph(noOfVertices, 1, 0)
        
    if not isWeighted:
        if isDirectional: # Directed unweighted graph
            print("It is not weighted.")
            print("It has direction.")
            return Graph(noOfVertices, 0, 1)

        if not isDirectional: # Bidrectional unweighted graph
            print("It is not weighted.")
            print("It is bidirectional.")
            return Graph(noOfVertices, 0, 0)

def bfs(graph, start):
    print()
    print("BFS algorithm: START")
    print(f"Input(s): starting node {start}")
    visited = set()
    queue = [start]
    if graph.weighted:
        def recurTupleFormat(graph, start):
            if len(queue) == 0:
                return None
            node = queue.pop(0)
            visited.add(node)
            if len(graph.adjacencyList[node]) > 0: # This vertex HAS at least one neighbour
                for neighbour in graph.adjacencyList[node]:
                    if neighbour[0] not in visited and neighbour[0] not in queue:
                        queue.append(neighbour[0])
                    recurTupleFormat(graph, neighbour[0])
        recurTupleFormat(graph,start)
    elif not graph.weighted:
        def recurListFormat(graph, start):
            if len(queue) == 0:
                return None
            node = queue.pop(0)
            visited.add(node)
            if len(graph.adjacencyList[node]) > 0: # This vertex HAS at least one neighbour
                for neighbour in graph.adjacencyList[node]:
                    if neighbour not in visited and neighbour not in queue:
                        queue.append(neighbour)
                    recurListFormat(graph, neighbour)
        recurListFormat(graph,start)

    print(f"Output(s): Set of vertices explored starting from node {start} : {visited}")
    print("BFS algorithm: END")
    print()
    return visited
# DFS implementation for directed graph
def dfs(graph, start):
    print()
    print("DFS algorithm: START")
    print(f"Input(s): starting node {start}")

    visited = set()

    if graph.weighted:
        def recurTupleFormat(graph, start):
            visited.add(start)
            if len(graph.adjacencyList[start]) > 0: # This vertex HAS at least one neighbour
                for nextNode in set(graph.adjacencyList[start]) - visited:
                    recurTupleFormat(graph, nextNode[0])
        recurTupleFormat(graph,start)
    elif not graph.weighted:
        def recurListFormat(graph, start):
            visited.add(start)
            for nextNode in set(graph.adjacencyList[start]) - visited:
                recurListFormat(graph, nextNode)
        recurListFormat(graph,start)

    print(f"Output(s): Set of vertices explored starting from node {start} : {visited}")
    print("DFS algorithm: END")
    print()
    return visited

def bellman_ford(graph, start):
    print()
    print("Bellman-Ford algorithm: START")
    print(f"Input(s): starting node {start}")

    if not(graph.directional and graph.weighted):
        print("Graph type is not suitable for Bellman-Ford's algorithm. Please change your graph type. Exiting function")
        print("Bellman-Ford algorithm end: END")
        print()
        return False
    
    if len(graph.adjacencyList[start]) == 0:
        print(f"Starting node does not have directed neighbours in the graph provided.")
        print("Bellman-Ford algorithm end: END")
        print()
        return start

    distances = {node: float('inf') for node in graph.adjacencyList}
    distances[start] = 0
    for _ in range(len(graph.adjacencyList)-1):
        for u in graph.adjacencyList: # u is initial node, v is final node
            for v, w in graph.adjacencyList[u]:
                if distances[u] != float('inf') and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
    for u in graph.adjacencyList:
        for v, w in graph.adjacencyList[u]:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                return "Graph contains a negative-weight cycle"
            
    print(f"Output(s): distances from starting node {start}:{distances}")
    print("Bellman-Ford algorithm end: END")
    print()
    return distances

def dijkstra(graph, start):
    print()
    print("Dijkstra algorithm: START")
    print(f"Input(s): starting node {start}")
    
    if not(graph.directional and graph.weighted):
        print("Graph type is not suitable for Dijkstra's algorithm. Please change your graph type. Exiting function")
        print("Dijkstra algorithm end: END")
        print()
        return False
    
    if len(graph.adjacencyList[start]) == 0:
        print(f"Starting node does not have directed neighbours in the graph provided.")
        print("Dijkstra algorithm end: END")
        print()
        return start

    distances = {node: float('inf') for node in graph.adjacencyList}
    distances[start] = 0
    heap = [(0, start)]
    while heap:
        (cost, node) = heapq.heappop(heap)
        if cost > distances[node]:
            continue
        for neighbour, weight in graph.adjacencyList[node]:
            new_cost = cost + weight
            if neighbour in distances:
                if new_cost < distances[neighbour]:
                    distances[neighbour] = new_cost
                    heapq.heappush(heap, (new_cost, neighbour))
    print(f"Output(s): distances from starting node {start}:{distances}")
    print("Dijkstra algorithm end: END")
    print()
    return distances

'''
# Examples
graph = buildGraph(3,1,1)
graph.addEdge("A","B",3)
graph.addEdge("A","E",3)
graph.addEdge("B","E",4)
graph.addEdge("D","G",4)
graph.printEdges()

bfs(graph,"A")

graph2 = buildGraph(3,1,0)
graph2.addEdge("A","B")
graph2.addEdge("B","C")
graph2.addEdge("B","E")
graph2.addEdge("B","D")
graph2.addEdge("D","F")
graph2.printEdges()
bfs(graph2,"D")
'''
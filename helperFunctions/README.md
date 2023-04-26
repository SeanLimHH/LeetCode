# Helper functions

The functions listed here are sole to help speed up basic processes like creating random 2D matrix that is a float, a random list of strings with string size 5, and many more trivial tasks. For example, this includes tasks like setting up a hash table, or anything that is particularly custom and tedious, a requirement like hash table with doubling of size upon load factor >= 0.8. 

The main idea is to enable more time eventually to be spent on solving any problems on LeetCode, rather than focus on little details such as these.

Over time, I will also add basic functionality like the ability to see the changes in a matrix or list in a nicely formatted way.

I understand that many libraries such as numpy or pandas exist and even other libraries that implement what i do here. But in some situations, these libraries are allowed to be used. Recreating from scratch also enables me to add more possible customisability in my code.

The following are the currently available functionality:
Each of the functions should have parameter 'info'. Upon setting this to 1 or True, then the corresponding function will print out as many relevant information about it.

This is just to aid the debugging process.

The following are currently available functions:

# arrayMatrixHelper.py
1. createList
2. printList
3. create2DMatrix
4. print2DMatrix
5. getEntry
6. setEntry
7. setLeftColumn
8. setTopRow
9. setDiagonal
10. getRows
11. getColumns
12. getMax
13. getMin
14. createListRandom
15. create2DMatrixRandom

# hashing.py
1. DirectAddressTable
2. DirectAddressTable.setRehashPolicy
3. DirectAddressTable.calculateLoadFactor
4. DirectAddressTable.printTable
5. DirectAddressTable.divisionMethod
6. DirectAddressTable.multiplicationMethod
7. DirectAddressTable.getHashValue
8. DirectAddressTable.insertByKey
9. DirectAddressTable.deleteByKey
10. DirectAddressTable.deleteByValue
11. DirectAddressTable.searchByKey

# linkedList.py
Here I have two variations: a linked list with list nodes with just value, no key.
Another variation is a linked list with list nodes that has key and value. This is for hash tables.

Linked list with key and value
1. ListNodeWithKeyValue
2. ListNodeWithKeyValue.getKey
3. ListNodeWithKeyValue.setKey
4. ListNodeWithKeyValue.getValue
5. ListNodeWithKeyValue.setValue
6. ListNodeWithKeyValue.getPrevious
7. ListNodeWithKeyValue.setPrevious
8. ListNodeWithKeyValue.getNext
9. ListNodeWithKeyValue.setNext
10. LinkedListWithKeyValue
11. LinkedListWithKeyValue.size
12. LinkedListWithKeyValue.printLL
13. LinkedListWithKeyValue.searchKey
14. LinkedListWithKeyValue.insertKey
15. LinkedListWithKeyValue.deleteKey
16. LinkedListWithKeyValue.reset

Linked list with no key, just value
1. ListNode
2. ListNode.getValue
3. ListNode.setValue
4. ListNode.getPrevious
5. ListNode.setPrevious
6. ListNode.getNext
7. ListNode.setNext
8. LinkedList
9. LinkedList.size
10. LinkedList.printLL
11. LinkedList.search
12. LinkedList.insert
13. LinkedList.delete
14. LinkedList.reset

# graphs.py
Uses adjacency list
1. Graph
2. Graph.addEdge
3. Graph.addUnweightedEdge
4. Graph.addWeightedEdge
5. Graph.addBidirectionalUnweightedEdge
6. Graph.addBidirectionalWeightedEdge
7. Graph.printEdges
8. buildGraph
Inputing whether the graph should be directional and should have weights, it calls the corresponding function for adding edges.
9. bfs
10. dfs
11. bellman_ford
12. dijkstra

#togglePrinting
Create a TogglePrint object, call .enable() or .e() to enable printing; .disable() or .d() to disable printing
1. TogglePrint

def isNode(node, info = 0):
    if info:
        print("\nisNode()")

    if isinstance(node,BinaryNode):

        if info:
            print("Input is a node!")
        return True
    
    if info:
        print("Input is not a node!")
    return False

class BinaryNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
    
    def setKey(self, key, info = 0):
        if info:
            print("\nsetKey()")
        self.key = key

    def getKey(self, info = 0):
        if info:
            print("\ngetKey()")
            print(f"The key is {self.key}.")
        return self.key
    
    def setValue(self, value, info = 0):
        if info:
            print("\nsetValue()")
        self.value = value
        
    def getValue(self, info = 0):
        if info:
            print("\ngetValue()")
            print(f"The value is {self.value}.")
        return self.value
    
    def setParent(self, parentNode, info = 0):

        if not isNode(parentNode):
            print("Input is not a node!")
        
        if info:
            print("\nsetParent()")
        self.parent = parentNode
        
    def getParent(self, info = 0):
        if info:
            print("\ngetParent()")
            print(f"The parent is {self.parent}.")
        return self.parent
    
    def setLeft(self, node, info = 0):
        if info:
            print("\nsetLeft()")
        
        if not isNode(node):
            print("Input is not a node!")
        
        self.left = node

    def getLeft(self, info = 0):
        if info:
            print("\ngetLeft()")
            print(f"The left node is {self.left}.")
        return self.left

    def setRight(self, node, info = 0):
        if info:
            print("\nsetRight()")
        
        if not isNode(node):
            print("Input is not a node!")
            
        self.right = node

    def getRight(self, info = 0):
        if info:
            print("\ngetRight()")
            print(f"The right node is {self.right}.")
        return self.right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def getMax(self, node, info = 0):
        if info:
            print("\ngetMax()")
            
        if self.root is None:
            print("Tree is empty. No maximum.")
            return None
        
        if not isNode(node):
            print("Input is not a node!")

        node = self.root
        while node.getRight() is not None:
            node.setRight(node.getRight())
        
        if info:
            print(f"The maximum of this binary search tree is {node.getKey()}")

        return node

    def getMin(self, node, info = 0):
        if info:
            print("\ngetMin()")
            
        if self.root is None:
            print("Tree is empty. No minimum.")
            return None
        
        if not isNode(node):
            print("Input is not a node!")

        node = self.root
        while node.getLeft() is not None:
            node.setLeft(node.getLeft())
        
        if info:
            print(f"The minimum of this binary search tree is {node.getKey()}")
        return node
  
    def getSuccessor(self, node, info = 0):
        if info:
            print("\ngetSuccessor()")
        
        if not isNode(node):
            print("Input is not a node!")
        
        if node.getRight() is not None:
            self.getMin(node.getRight())

        parentNode = node.getParent()

        while parentNode is not None and node is parentNode.getRight():
            node = parentNode
            parentNode = parentNode.getParent()
        
        if info:
            print(f"The successor is {parentNode.getKey()}")

        return parentNode

    def getPredecessor(self, node, info = 0):
        if info:
            print("\ngetPredecessor()")
        
        if not isNode(node):
            print("Input is not a node!")
        
        if node.getLeft() is not None:
            self.getMax(node.getLeft())

        parentNode = node.getParent()

        while parentNode is not None and node is parentNode.getLeft():
            node = parentNode
            parentNode = parentNode.getParent()
        
        if info:
            print(f"The successor is {parentNode.getKey()}")

        return parentNode

    def printTree(self):
        print("\nprintTree()")
        print("Key: Value")
        print(f"Root: {self.root.getKey()}")
        print("In-order traversal")
        print("------------------")
        if self.root is None:
            print("Tree is empty")
        else:
            self.printTreeHelper(self.root)

    def printTreeHelper(self, node):
        if node:
            self.printTreeHelper(node.getLeft())
            print(node.getKey())
            self.printTreeHelper(node.getRight())

    def insertNode(self, nodeToBeInserted, info = 0):
        if info:
            print("\ninsertNode()")

        if not isNode(nodeToBeInserted):
            print("Input is not a node!")
            return None

        if self.root is None:
            if info:
                print("Root is not set. Setting root of tree to target node.")
            self.root = nodeToBeInserted
            return None

        self.iterateDown(self.root,nodeToBeInserted, info)
    
    def iterateDown(self, currentNode, nodeToBeInserted, info = 0):

        if info:
            print("\niterateDown()")
            print(f"Current node's key: {currentNode.getKey()}")
            print(f"Node to be inserted's key: {nodeToBeInserted.getKey()}")

        if nodeToBeInserted.getKey() >= currentNode.getKey():
            if currentNode.getRight() is None: #* No right child
                #* This means you should insert as current's right child
                if info:
                    print("Current node's key < node to be inserted's key. Current node has no right child. Setting it to the target node.")
                    print("Also setting target node's parent to current node.")
                nodeToBeInserted.setParent(currentNode)
                currentNode.setRight(nodeToBeInserted)
                return currentNode
            if info:
                print("Current node's key < node to be inserted's key. Traversing rightwards down.")
            #* Here means right child exists; so you want to recurse down right child
            return self.iterateDown(currentNode.getRight(), nodeToBeInserted, info)
            
        elif nodeToBeInserted.getKey() < currentNode.getKey():
            if currentNode.getLeft() is None: #* No left child
                #* This means you should insert as current's left child
                if info: 
                    print("Current node's key >= node to be inserted's key. Current node has no left child. Setting it to the target node.")
                    print("Also setting target node's parent to current node.")
                nodeToBeInserted.setParent(currentNode)
                currentNode.setLeft(nodeToBeInserted)
                return currentNode
            
            if info:
                print("Current node's key >= node to be inserted's key. Traversing leftwards down.")
            #* Here means left child exists; so you want to recurse down left child
            return self.iterateDown(currentNode.getLeft(), nodeToBeInserted, info)

    def searchKey(self, currentNode, key, info = 0):
        #* Returns node with that matches target key. Returns None if not found
        #* Similar to iterateDown

        if info:
            print("\nsearchKey()")
            print(f"Current node's key: {currentNode.getKey()}")
            print(f"Target key is: {key}")

        if key == currentNode.getKey():
            if info:
                print("Current node's key is equal to target key.")
            return currentNode
        
        elif key > currentNode.getKey():
            if info:
                print("Current node's key is less than target key.")

            if currentNode.getRight() is None: #* No right child
                
                if info:
                    print("No right child. This means that key does not exist in tree!")
                
                return None
            
            if info:
                print("Current node has a right child. Traversing to right child.")
            #* Here means right child exists; so you want to recurse down right child

            return self.searchKey(currentNode.getRight(), key, info)
            
        elif key < currentNode.getKey():
            if info:
                print("Current node's key is less than target key.")

            if currentNode.getLeft() is None: #* No left child
                
                if info:
                    print("No left child. This means that key does not exist in tree!")
                
                return None
            
            if info:
                print("Current node has a left child. Traversing to left child.")
            #* Here means left child exists; so you want to recurse down left child
            
            return self.searchKey(currentNode.getLeft(), key, info)

    def deleteKey(self, key, info = 0):
        if info:
            print("\ndeleteKey()")

        if self.root is None:
            if info:
                print("Binary Search Tree is empty. No key to delete.")
            return None

        node = self.searchKey(self.root, key)
        if node is None:
            print("Key is not found in tree. Cannot delete")
            return False

        if node.getLeft() is None and node.getRight() is None:
            if node.getParent() is None: #* Is root to be deleted. And has no other element
                self.root = None

            elif node.getParent().getLeft() == node:
                node.getParent().setLeft(None)

            else:
                node.getParent().setRight(None)

        elif node.getLeft() is not None and node.getRight() is None:
             #* Has left child no right child
            if node.getParent() is None:
                self.root = node.getLeft()
                self.root.setParent(None)

            elif node.getParent().getLeft() is node:
                node.getParent().setLeft(node.getLeft())
                node.getLeft().setParent(node.getParent())
            else:
                node.getParent().setRight(node.getLeft())
                node.getLeft().setParent(node.getParent())

        elif node.getLeft() is None and node.getRight() is not None:
             #* Has no left child but has right child
        
            if node.getParent() is None:
                self.root = node.getRight()
                self.root.setParent(None)

            elif node.getParent().getLeft() is node:
                node.getParent().setLeft(node.getRight())
                node.getRight().setParent(node.getParent())

            else:
                node.getParent().setRight(node.getRight())
                node.getRight().setParent(node.getParent())

        else:
            successor = self.getSuccessor(node)
            node.setKey(successor.getKey())
            node.setValue(successor.getValue())
            self.deleteKey(successor.getKey())

        return True


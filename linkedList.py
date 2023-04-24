class ListNode:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

    def getValue(self, info = 0):
        if info == 1:
            print('ListNode.getValue()')
            print(f'The current object has value {self.value}')
        return self.value
    
    def setValue(self, newValue, info = 0):
        if info == 1:
            print('ListNode.setValue()')
            print(f'The current object will have its value set to {newValue}')
        self.value = newValue

    def getPrevious(self, info = 0):
        if info == 1:
            print('ListNode.getPrevious()')
            if self.previous is None:
                print('Previous node is None.')
                return None
            print(f'The previous object has value {self.previous.getValue()}')
            return self.previous
        
        if self.previous is None:
                return None
        return self.previous
        
    
    def setPrevious(self, node, info = 0):
        if info == 1:
            print('ListNode.setPrevious()')
            if not isinstance(node, ListNode):
                print('Object to be set as .previous is not a ListNode!')
            self.previous = node

        else:
            if not isinstance(node, ListNode):
                print('Object to be set as .previous is not a ListNode!')
            self.previous = node
        
    def getNext(self, info = 0):
        if info == 1:
            print('ListNode.getNext()')
            if self.next is None:
                print('Next node is None.')
            else:
                print(f'The next object has value {self.next.getValue()}')
            return self.next
        else:
            return self.next
    
    def setNext(self, node, info = 0):
        if info == 1:
            print('ListNode.setNext()')
            if not isinstance(node, ListNode):
                print('Object to be set as .next is not a ListNode!')
            self.next = node
        else:
            self.next = node


class LinkedList: #* Doubly linked list
    def __init__(self):
        self.head = None

    def printLL(self):
        print(f'\nLinkedList.printLL()')
        current = self.head

        if current is None:
            print('No elements in linked list. Cannot print anything.')
            return None
        
        print(f'{"Current value":<14}: ', end = '')
        while current is not None:
            print(f'{str(current.getValue()):<5}{"->":^10}', end = '')
            current = current.getNext()
        print('None')
        current = self.head
        print(f'{"Next node":<14}: ', end = '')
        while current.getNext() is not None:
            print(f'{str(current.getNext().getValue()):<5}{"  ":^10}', end = '')
            current = current.getNext()
        print('None')

        current = self.head
        print(f'{"Previous node":<14}: ', end = '')
        print(f'{"None":<5}{"  ":^10}', end = '')
        current = current.getNext()
        while current is not None:
            print(f'{str(current.getPrevious().getValue()):<5}{"  ":^10}', end = '')
            current = current.getNext()
        print()

    def search(self, value, info = 0):
        if info == 1:
            print('LinkedList.search()')

            currentNode = self.head

            while currentNode is not None and currentNode.getValue() != value:
                currentNode = currentNode.getNext()

            #* Returns None if no value found
            print(f'Search found and will return this node with value {currentNode.getValue()}.')
            return currentNode
        else:
            currentNode = self.head

            while currentNode is not None and currentNode.getValue() != value:
                currentNode = currentNode.getNext()

            #* Returns None if no value found
            return currentNode

    def insert(self, listNode, info = 0):
        if info == 1:
            print('LinkedList.insert()')
            if not isinstance(listNode, ListNode):
                print('Object to be inserted into Linked List is not a ListNode!')
                return None
            
            if self.head is None:
                self.head = listNode
                return None

            currentNode = self.head
            prevNode = currentNode #* For running the lines after while loop if while loop does not run
            
            while currentNode is not None:
                prevNode = currentNode
                currentNode = currentNode.getNext()
            
            #* Here is at the last node. currentNode.next is None
            prevNode.setNext(listNode)
            listNode.setPrevious(prevNode)
        
        else:
            if not isinstance(listNode, ListNode):
                print('Object to be inserted into Linked List is not a ListNode!')
                return None
            
            if self.head is None:
                self.head = listNode
                return None

            currentNode = self.head
            prevNode = currentNode #* For running the lines after while loop if while loop does not run
            
            while currentNode is not None:
                prevNode = currentNode
                currentNode = currentNode.getNext()
            
            #* Here is at the last node. currentNode.next is None
            prevNode.setNext(listNode)
            listNode.setPrevious(prevNode)
    
    def delete(self, value, info = 0):
        if info == 1:
            print('LinkedList.delete()')
            if self.search(value) is None:
                print('Node does not exist in Linked List!')
                return None
            
            if self.head.getValue() == value:
                self.head = self.head.getNext()
                self.head.setPrevious(None)
                return None

            currentNode = self.head
            prevNode = currentNode #* For running the lines after while loop if while loop does not run
            while currentNode.getValue() != value:
                prevNode = currentNode
                currentNode = currentNode.getNext()
            
            #* Here is where currentNode.getValue() == value
            prevNode.setNext(currentNode.getNext())
            if currentNode.getNext() is not None:
                currentNode.getNext().setPrevious(prevNode)

            #* Else do nothing
            if currentNode is self.head:
                self.head = None
            
        else:
            
            if self.search(value) is None:
                print('Node does not exist in Linked List!')
                return None
            
            if self.head.getValue() == value:
                self.head = self.head.getNext()
                self.head.setPrevious(None)
                return None

            currentNode = self.head
            prevNode = currentNode #* For running the lines after while loop if while loop does not run
            while currentNode.getValue() != value:
                prevNode = currentNode
                currentNode = currentNode.getNext()
            
            #* Here is where currentNode.getValue() == value
            prevNode.setNext(currentNode.getNext())
            if currentNode.getNext() is not None:
                currentNode.getNext().setPrevious(prevNode)

            #* Else do nothing
            if currentNode is self.head:
                self.head = None
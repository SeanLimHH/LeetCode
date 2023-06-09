import math
class MaxHeap:
    def __init__(self):
        self.size = 0
        self.heap = []
        
    def printHeap(self):
        print("printHeap()")
        
        # Check if the heap is empty
        if self.size == 0:
            print("Heap is empty.")
            return None
            
        numLevels = math.ceil(math.log2(len(self.heap) + 1))
        maxNodeStrLen = max(len(str(node)) for node in self.heap)
        maxStrLen = max(maxNodeStrLen, len(str(self.heap[0])))
        outputWidth = maxStrLen * int(math.pow(2,(numLevels - 1)))
        formattedHeap = []
        for i in range(numLevels):
            numNodes = int(math.pow(2,i))
            nodeSpacing = outputWidth // numNodes
            line = ''
            for j in range(numNodes):
                nodeIndex = int(math.pow(2,i)) - 1 + j
                if nodeIndex >= len(self.heap):
                    line += ' ' * nodeSpacing
                else:
                    nodeStr = f'{str(self.heap[nodeIndex]):^{nodeSpacing}}'
                    line += nodeStr
                line += ' ' * nodeSpacing
            formattedHeap.append(line)
        formattedHeap[0] = ' ' * (maxStrLen // 2) + formattedHeap[0]
        print('\n'.join(formattedHeap))

                
    def getParent(self, index, info = 0):
        if info:
            print("\nMaxHeap.getParent()")
            print(f'Parent of node index {index} is: {(index-1)//2}.')
        return (index-1)//2
    
    def getLeftChild(self, index, info = 0):
        if (2*index)+1 >= self.size:
            if info:
                print("\nMaxHeap.getLeftChild() is out of range.")
            return None
        if info:
            print("\nMaxHeap.getLeftChild()")
            print(f'Left child of node index {index} is: {(2*index)+1}.')
        return (2*index)+1

    def getRightChild(self, index, info = 0):
        if (2*index)+2 >= self.size:
            if info:
                print("\nMaxHeap.getRightChild() is out of range.")
            return None
        if info:
            print("\nMaxHeap.getRightChild()")
            print(f'Right child of node index {index} is: {(2*index)+2}')
        return (2*index)+2

    def swap(self, A, B, info = 0):
        if info:
            print("\nMaxHeap.swap()")
            print(f'Swapping node indices {A} with {B} in the heap directly.')
        self.heap[A], self.heap[B] = self.heap[B], self.heap[A]
        if info:
            print("New heap:")
            self.printHeap()

    def insert(self, key, info = 0):
        if info:
            print("\nMaxHeap.insert()")
        
        self.heap.append(key)
        if self.size == 0:
            if info:
                print(f"Inserted {key} as root.")
            self.size += 1
            return None
        
        currentIndex = self.size
        parentIndex = self.getParent(currentIndex)
        
        while parentIndex != 0:
            
            if key >= self.heap[parentIndex]:
                self.swap(currentIndex, parentIndex)
                currentIndex = parentIndex
                parentIndex = self.getParent(currentIndex)

        if parentIndex == 0:
            if key >= self.heap[parentIndex]:
                self.swap(currentIndex, parentIndex)

        self.size += 1

    def buildMaxHeap(self, arrayToBeHeap, info = 0):
        
        if info:
            print("\nMaxHeap.buildMaxHeap()")

        n = len(arrayToBeHeap)
        self.heap = arrayToBeHeap
        self.size = n
        
        for i in range((n // 2)-1,-1,-1):
            
            self.maxHeapify(i)

        if info:
            print("Built max heap:")
            self.printHeap()

    def maxHeapify(self, index, info = 0):

        if info:
            print("\nMaxHeap.maxHeapify()")
            print(f"Heapifying index {index}: {self.heap[index]}.")
        
        if self.getRightChild(index) is None: #* No right child, may have left child
            if self.getLeftChild(index) is None: #* No children
                return None
            else: #* Has left child, no right child
                if self.heap[self.getLeftChild(index)] > self.heap[index]:
                    self.swap(index, self.getLeftChild(index))
                    return self.maxHeapify(self.getLeftChild(index))

        else: #* Has both children
            if self.heap[self.getLeftChild(index)] > self.heap[self.getRightChild(index)]:
                #* Here means: Left child is > Right child
                #* We then check if parent is less than left child. If so, swap with left child
                if self.heap[index] < self.heap[self.getLeftChild(index)]:
                    self.swap(index, self.getLeftChild(index))
                    return self.maxHeapify(self.getLeftChild(index))
            
            else: #* Here means: Right child > Left child
                #* We then check if parent is less than right child. If so, swap with right child
                if self.heap[index] < self.heap[self.getRightChild(index)]:
                    self.swap(index, self.getRightChild(index))
                    return self.maxHeapify(self.getRightChild(index))

    def extractMax(self, info = 0):

        if info:
            print("\nMaxHeap.extractMax()")
            
        self.swap(0,self.size-1)

        maxValue = self.heap.pop()
        self.size -= 1
        self.maxHeapify(0)

        if info:
            print(f"Max value extracted is {maxValue}.")

        return maxValue











class MinHeap:
    def __init__(self):
        self.size = 0
        self.heap = []
        
    def printHeap(self):
        print("printHeap()")
        
        # Check if the heap is empty
        if self.size == 0:
            print("Heap is empty.")
            return None
            
        numLevels = math.ceil(math.log2(len(self.heap) + 1))
        maxNodeStrLen = max(len(str(node)) for node in self.heap)
        maxStrLen = max(maxNodeStrLen, len(str(self.heap[0])))
        outputWidth = maxStrLen * int(math.pow(2,(numLevels - 1)))
        formattedHeap = []
        for i in range(numLevels):
            numNodes = int(math.pow(2,i))
            nodeSpacing = outputWidth // numNodes
            line = ''
            for j in range(numNodes):
                nodeIndex = int(math.pow(2,i)) - 1 + j
                if nodeIndex >= len(self.heap):
                    line += ' ' * nodeSpacing
                else:
                    nodeStr = f'{str(self.heap[nodeIndex]):^{nodeSpacing}}'
                    line += nodeStr
                line += ' ' * nodeSpacing
            formattedHeap.append(line)
        formattedHeap[0] = ' ' * (maxStrLen // 2) + formattedHeap[0]
        print('\n'.join(formattedHeap))

                
    def getParent(self, index, info = 0):
        if info:
            print("\nMinHeap.getParent()")
            print(f'Parent of node index {index} is: {(index-1)//2}.')
        return (index-1)//2
    
    def getLeftChild(self, index, info = 0):
        if (2*index)+1 >= self.size:
            if info:
                print("\nMinHeap.getLeftChild() is out of range.")
            return None
        if info:
            print("\nMinHeap.getLeftChild()")
            print(f'Left child of node index {index} is: {(2*index)+1}.')
        return (2*index)+1

    def getRightChild(self, index, info = 0):
        if (2*index)+2 >= self.size:
            if info:
                print("\nMinHeap.getRightChild() is out of range.")
            return None
        if info:
            print("\nMinHeap.getRightChild()")
            print(f'Right child of node index {index} is: {(2*index)+2}.')
        return (2*index)+2

    def swap(self, A, B, info = 0):
        if info:
            print("\nMinHeap.swap()")
            print(f'Swapping node indices {A} with {B} in the heap directly.')
        self.heap[A], self.heap[B] = self.heap[B], self.heap[A]
        if info:
            print("New heap:")
            self.printHeap()

    def insert(self, key, info = 0):
        if info:
            print("\nMinHeap.insert()")
        
        self.heap.append(key)
        if self.size == 0:
            if info:
                print(f"Inserted {key} as root.")
            self.size += 1
            return None
        
        currentIndex = self.size
        parentIndex = self.getParent(currentIndex)
        
        while parentIndex != 0:
            
            if key <= self.heap[parentIndex]:
                self.swap(currentIndex, parentIndex)
                currentIndex = parentIndex
                parentIndex = self.getParent(currentIndex)

        if parentIndex == 0:
            if key <= self.heap[parentIndex]:
                self.swap(currentIndex, parentIndex)

        self.size += 1

    def buildMinHeap(self, arrayToBeHeap, info = 0):
        
        if info:
            print("\nMinHeap.buildMinHeap()")

        n = len(arrayToBeHeap)
        self.heap = arrayToBeHeap
        self.size = n
        
        for i in range((n // 2)-1,-1,-1):
            print("i",i)
            self.minHeapify(i)
            self.printHeap()

        if info:
            print("Built min heap:")
            self.printHeap()

    def minHeapify(self, index, info = 0):

        if info:
            print("\nMinHeap.minHeapify()")
            print(f"Heapifying index {index}: {self.heap[index]}")
        
        if self.getRightChild(index) is None: #* No right child, may have left child
            if self.getLeftChild(index) is None: #* No children
                return None
            else: #* Has left child, no right child
                if self.heap[self.getLeftChild(index)] < self.heap[index]:
                    self.printHeap()
                    self.swap(index, self.getLeftChild(index))
                    return self.minHeapify(self.getLeftChild(index))

        else: #* Has both children
            
            if self.heap[self.getLeftChild(index)] > self.heap[self.getRightChild(index)]:
                #* Here means: Left child is > Right child
                #* We then check if parent is more than right child. If so, swap with right child
                if self.heap[index] > self.heap[self.getRightChild(index)]:
                    self.swap(index, self.getRightChild(index))
                    return self.minHeapify(self.getRightChild(index))
            
            else: #* Here means: Right child > Left child
                #* We then check if parent is more than left child. If so, swap with left child
                if self.heap[index] > self.heap[self.getLeftChild(index)]:
                    self.swap(index, self.getLeftChild(index))
                    return self.minHeapify(self.getLeftChild(index))

    def extractMin(self, info = 0):

        if info:
            print("\nMinHeap.extractMin()")
            
        self.swap(0,self.size-1)
        minValue = self.heap.pop()
        self.size -= 1
        self.minHeapify(0)

        if info:
            print(f"Min value extracted is {minValue}.")

        return minValue

def heapsort(array, ascending = 0, descending = 1, info = 0):
    
    if info:
        print("\nheapsort()")

    sortedList = []

    if ascending == 1:
        if info:
            print("Array to be sorted will be in ascending order.")
        minHeap = MinHeap()
        minHeap.buildMinHeap(array,info=1)
        for _ in range(minHeap.size-1):
            sortedList.append(minHeap.extractMin())
            minHeap.minHeapify(0)

        sortedList.append(minHeap.extractMin())

    elif descending == 1:
        if info:
            print("Array to be sorted will be in descending order.")
        maxHeap = MaxHeap()

        maxHeap.buildMaxHeap(array,info=1)
        for _ in range(maxHeap.size-1):
            sortedList.append(maxHeap.extractMax())
            maxHeap.maxHeapify(0)

        sortedList.append(maxHeap.extractMax())
        
    return sortedList

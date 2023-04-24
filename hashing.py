import math
from arrayMatrixHelper import *
from linkedList import *

class DirectAddressTable:
    def __init__(self, size):
        self.size = size
        self.table = createList(size)
        for slot in range(size):
            self.table[slot] = LinkedListWithKeyValue()
        self.loadFactor = 0
        
        self.loadFactorThreshold = 0
        self.rehashFunction = 'division'
        self.enableRehashTable = False

    def setRehashPolicy(self, loadFactorThreshold, rehashFunction = 'division', enableRehashTable = True, info = 0):
        if info == 1:
            print('\nDirectAddressTable.setRehashPolicy()')
        self.loadFactorThreshold = loadFactorThreshold
        self.rehashFunction = rehashFunction
        self.enableRehashTable = enableRehashTable

    def calculateLoadFactor(self, info = 0):
        numberOfElements = sum(ll.size() for ll in self.table)
        
        if info == 1:
            print('\nDirectAddressTable.calculateLoadFactor()')
            print(f'There are {numberOfElements} elements and {self.size} slots in hash table.')
            print(f'Calculated load factor is {numberOfElements}/{self.size} = {numberOfElements / self.size}.')
        
        self.loadFactor = numberOfElements / self.size
    
    def printTable(self):
        print('\nDirectAddressTable.printTable()')
        for LL in range(self.size):
            print(f'Index {LL}:', end='')
            self.table[LL].printLL()
            print()

    def divisionMethod(self, key, info = 0):
        print('\nDirectAddressTable.divisionMethod()')
        if isinstance(key, int) or isinstance(key, float):
            if info == 1:
                print(f'The hash value of {key} is {key % self.size}.')
            return key % self.size
        
        else:
            print('Error occurred.')
            print('Please ensure that the data type of value is a number!')
            return None
        
    def multiplicationMethod(self, key, constant, info = 0):
        print('\nDirectAddressTable.multiplication()')
        if isinstance(key, int) or isinstance(key, float):
            if info == 1:
                print(f'The hash value of {key} is {math.floor(((constant*key)%1)*self.size)}.')
            return math.floor(((constant*key)%1)*self.size)
        
        else:
            print('Error occurred.')
            print('Please ensure that the data type of value is a number!')
            return None

    def getHashValue(self, key, hashFunction, constant = (math.sqrt(5)-1)/2, info = 0):
        if info == 1:
            print('\nDirectAddressTable.getHashValue()')

        match hashFunction:
            case "division":
                return self.divisionMethod(key)

            case "multiplication":
                return self.multiplicationMethod(key,constant)

            case _:
                print('Please enter a valid hash function to be used!')
                print("Either key in 'division' or 'multiplication' in parameter!")
                return None

    def insertByKey(self, listNodeWithKeyValue, hashFunction, constant = (math.sqrt(5)-1)/2, info = 0):
        #* Assumes you are inserting a ListNodeWithKeyValue

        if info == 1:
            print('\nDirectAddressTable.insertByValue()')
            
            if self.enableRehashTable:
                
                self.calculateLoadFactor()


                if self.loadFactor > self.loadFactorThreshold:

                    print('Load factor passed threshold. Will rehash table by doubling its size.')
                    newTable = createList(self.size*2)

                    for slot in range(self.size*2):
                        newTable[slot] = LinkedListWithKeyValue()
                    
                    for slot in range(self.size):
                        newTable[slot] = self.table[slot] #* Maintain old values
                    
                    self.size = self.size*2
                    print(f'New size is {self.size}.')
                    
                    self.table = newTable
                    self.printTable()

            if hashFunction == "division":

                print('Hash function to be used is division.')
                print(f'The item to be inserted has key value : {listNodeWithKeyValue.getKey()}.')
                print(f"Its hash value is {self.getHashValue(listNodeWithKeyValue.getKey(), hashFunction)} and this is its index in the direct address table.")
                self.table[self.getHashValue(listNodeWithKeyValue.getKey(), hashFunction)].insertKey(listNodeWithKeyValue)
                return None
        
            elif hashFunction == "multiplication":

                print('Hash function to be used is multiplication.')
                print(f'The item to be inserted has key value : {listNodeWithKeyValue.getKey()}. The constant used is {constant}.')
                print(f"Its hash value is {self.getHashValue(listNodeWithKeyValue.getKey(), hashFunction, constant)} and this is its index in the direct address table.")
                self.table[self.getHashValue(listNodeWithKeyValue.getKey(), hashFunction, constant)].insertKey(listNodeWithKeyValue)
                return None
        else:

            if self.enableRehashTable:
                
                self.calculateLoadFactor()

                if self.loadFactor > self.loadFactorThreshold:

                    newTable = createList(self.size*2)

                    for slot in range(self.size*2):
                        newTable[slot] = LinkedListWithKeyValue()
                    
                    for slot in range(self.size):
                        newTable[slot] = self.table[slot]
                    
                    self.size = self.size*2
                    self.table = newTable

            if hashFunction == "division":
                self.table[self.getHashValue(listNodeWithKeyValue.getKey(), hashFunction)].insertKey(listNodeWithKeyValue)
                return None
        
            elif hashFunction == "multiplication":
                self.table[self.getHashValue(listNodeWithKeyValue.getKey(), hashFunction, constant)].insertKey(listNodeWithKeyValue)
                return None
            
    def deleteByValue(self, itemValue, info = 0):
        if info == 1:
            print('\nDirectAddressTable.deleteByValue()')
            print(f'The item to be deleted has value : {itemValue}.')
            print(f"Its hash value is {self.getHashValue(itemValue)} and this is its index in the direct address table.")
        self.table[self.getHashValue(itemValue)].delete(itemValue)

    def deleteByKey(self, key, info = 0):
        if info == 1:
            print('\nDirectAddressTable.deleteByKey()')
            print(f'The item to be deleted by key has key : {key}.')
            print(f'The linked list in this slot is {self.table[key]}.')
            print(f'Resetting this linked list (this slot) to empty linked list.')
        self.table[key].reset()
    
    def searchByKey(self, key, info = 0):
        if info == 1:
            print('\nDirectAddressTable.searchByKey()')
            print(f'The item to be searched has key : {key}.')
            print(f'The linked list in this slot is {self.table[key]}')
            print(f'Returning this linked list (this slot)')
        return self.table[key]

'''
dTable = DirectAddressTable(4)
a = ListNodeWithKeyValue(1,1)
b = ListNodeWithKeyValue(2,2)
c = ListNodeWithKeyValue(3,3)
d = ListNodeWithKeyValue(4,4)
e = ListNodeWithKeyValue(5,5)
f = ListNodeWithKeyValue(6,6)
g = ListNodeWithKeyValue(7,7)
'''
'''
dTable.insertByKey(a,"division")
dTable.insertByKey(b,"division")
dTable.insertByKey(c,"division")
dTable.insertByKey(d,"division")
dTable.insertByKey(e,"division")
dTable.insertByKey(f,"division")
dTable.insertByKey(g,"division")
dTable.printTable()
'''
'''
mTable = DirectAddressTable(4)
mTable.setRehashPolicy(0.70, enableRehashTable=1)
mTable.insertByKey(a,"multiplication", info = 1)
mTable.insertByKey(b,"multiplication", info = 1)
mTable.insertByKey(c,"multiplication", info = 1)
mTable.insertByKey(d,"multiplication", info = 1)
mTable.insertByKey(e,"multiplication", info = 1)
mTable.insertByKey(f,"multiplication", info = 1)
mTable.insertByKey(g,"multiplication", info = 1)
mTable.printTable()
'''
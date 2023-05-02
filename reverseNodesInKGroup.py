'''
Problem : Hard

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should
remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

https://leetcode.com/problems/reverse-nodes-in-k-group/

Personal Interpretations:

Input : Singly linked list
Integer k, which represents the k nodes to reverse at a time, until the end of linked list.

Output : New linked list

Personal Interpretations (rough idea dump list; thought processes) : 

If the number of nodes to reverse exceeds the length, then cannot pursue the reversal. There will be one block of code that detects this.

Then we need another function to do the actual reversal : 

Given 1 2 3 4 5, we will reassign 1 to 4, 2 to 1, 3 to 2, for k = 3. Then we will need to select the start of the list to be the last of this snippet.

Generalising this reassignment, we can perform a recursive reversal of this form:
first => last + 1, second to first, third to second, fourth to third, fifth to fourth ...

The "base" case can be the first part where we assign it to last + 1

UPDATE: Not necessary. We can use a for loop to iterate in the multiples by controlling the step. Just needs more checking and being careful.

Also, it is simply updating the pointers. No need to play with the values.

I also noticed that it is important that we update the nodes backwards in order first. The reason is so that we can consistently keep track of which next node to update.

But you cannot iterate backwards since it is a singly-linked list.

So we have a constraint of only iterating forward. I think the approach then is to keep track of a nodes position in the previous and final linked list, updating accordingly.

The issue i face is that once you update the next node's next property, you cannot access the subsequent node.
This ultimately points to one thing: If you are iterating through the .next property which i am, then you must update in the reverse order.
If you are iterating through the list element method, then you can update in the forward order

UPDATE: What if i used a stack: LIFO property means that i will be able to reassign accordingly. it will take O(n) space. But the question wants O(1) in memory space

If we do a simple way: if k = 2, we settle the 2 elements swapping first. This means i should just focus on the simpler aspect of settling a smaller array

Now if this question used doubly-linked list, this would be a very easy question. If we can simulate the previous pointer without manipulating this ListNode class, then we
might lead towards a solution

So using same example: 1 2 3 4 5, k = 3
If we use this idea: At 1 => No previous, pause
At 2 => set 2.next to previous (1). Then go to the next element.
At 3 => set 3.next to previous (2). Then go to the next element.
We also need a checker before the setter: If it matches k, we want to figure this node as the final terminating node. We set its previous (first element of the previous set) 
.next to itself. 

Subproblem: Given integer k, reverse the first k nodes of a singly-linked list

Base cases: For the first node of the k nodes, if size of list > k, meaning list[k + 1] exists, then we set the .next of this node to it. 
This base case will need to be handled very very carefully. If there exists an element in the next set, we can set this last node in set to this element.

Otherwise set to None

UPDATE: Simplifying the messiness, whereby common codes can be taken out, i have cleaned up the code for the solution below. For comments, refer to the workings.


UPDATE: Setting of the previous set's last element to this set's last element is special. Best handled at the end of the iteration. The reason being is that the current set is
incomplete, we will then set it to current set's first element. Otherwise last element.
So the base case actually has two - three ways to handle.



UPDATE: I will try doing the approach where you do not have the full list, just the head

Base case: 
if currentNode is None: end
else: upon iteration == k: 


It is actually quite hard. The issue i faced is the case where k = 3, you have 2 nodes. Something of this sort. My idea is to cycle once more. I think this must be the only 
way. The reason is that if you do not cycle, you will not know if you have a complete set within the bigger theoretical set of nodes

so only upon a nice cycle, then we actually perform the reassignment


Some workings:
When will we terminate in a loop? Will there possibly be multiple .next = None? There are 2 cases to analyse: 
1. N = 3, K = 2 (Incomplete set)
2. N = 3, K = 3 (Complete set)

There should only be one .next == None.
How should we then terminate the loop? When .next = ? This should be:
1. N = 3, K = 2 (Incomplete set)
    0 cycles formed on second iteration, this mean do not set the .next properties. End loop, end function.
    The terminator will be when .next == None

2. N = 3, K = 3 (Complete set)
    1 cycle formed on first iteration. set the .next property by looping once more.
    The terminator will be when .next == None

With the above two, we can formulate a while loop with terminating condition .next = None

I can create a function called isComplete. This cycles through the set to determine if it is complete or not in that iteration. If so, i can react accordingly.

I will create another helper function called setReverse. This is the main iterative code. It loops through k nodes at a time and set the reverse. This will run if isComplete
returns True.

Also, at the start of each set, i definitely want to set the previous set's last element to the current set's last element (if complete) or current set's first element (if
incomplete.)

Another helper function is to get the next set's first element. This is useful if the set is complete.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

'''
Clean solution: See below for workings.
'''



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList_(head):
    print("The head is", head.val)
    print("The next is", head.next.val)
    returnList = []      
    current = head
    while current.next is not None:
        returnList.append(current.val)
        current = current.next
    returnList.append(current.val)
    print([x for x in returnList])
    return returnList

class Solution:

    def reverseKGroup(self, head, k):
        if k == 1:
            return head
        start = head
        currentNode = head
        previousSetStartingNode = head
        while currentNode is not None:
            #* At this stage, currentNode is the start of this unknown complete or incomplete set.
            #* This value is important; we want to see: if current cycle is in complete: set to the next set's element. Else set to None

            #* Here, we also must consider the continuation case: Set the first element to where?
            
            startingNode = currentNode #* We store this important node. On the next cycle, we determine how to assign its value.
            if Solution.isComplete(self, currentNode, k):

                currentNode = Solution.getNextSetFirstElement(self, currentNode, k) #* Can be either None or an actual node.
                
                currentLast = Solution.getThisSetLastElement(self, startingNode, k)
                Solution.setReverse(self, startingNode, k)
                if start == head:
                    start = currentLast
                    print(start.val)
                previousSetStartingNode.next = currentLast
                previousSetStartingNode = startingNode
                
                startingNode.next = currentNode
                #* This case has implications: your previous set's last element must thus be reassigned to this set's last element.
                
            else:

                if currentNode == head:
                    start = Solution.getThisSetLastElement(self, startingNode, k)
                #* This case has implications: your previous set's last element must thus be reassigned to this set's first element.
                #* This case also means it is the end; last set.
                break

        return start
            

    def isComplete(self, startingNode, iterations):
        #* Iterations == k
        loops = 0
        currentNode = startingNode
        while currentNode is not None:
            
            loops += 1

            if loops == iterations:
                return True
            currentNode = currentNode.next

        return False
    
    def setReverse(self, startingNode, iterations):
        loops = 0
        currentNode = startingNode
        previousNode = startingNode
        while loops != iterations:
            nodeToIterateNextTemporary = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nodeToIterateNextTemporary
            loops += 1

    def getNextSetFirstElement(self, startingNode, iterations):
        #* Assumes set is complete
        loops = 0
        currentNode = startingNode
        while currentNode.next is not None:
            loops += 1
            if loops == iterations:
                return currentNode.next

            currentNode = currentNode.next
        #* Here means the set is not complete!
        return None
    
    def getThisSetLastElement(self, startingNode, iterations):
        #* Assumes set is complete
        loops = 0
        currentNode = startingNode
        while currentNode.next is not None:
            
            loops += 1
            if loops == iterations:
                return currentNode

            currentNode = currentNode.next
        #* Here means the set is not complete!
        return currentNode


from helperFunctions.arrayMatrixHelper import *
list_ = createListRandom("int",5,0,100)


head = []
for element in list_:
    head.append(ListNode(element))


for node in range(len(head)):
    if node+1 < len(head):
        head[node].next = head[node+1]


Solution.reverseKGroup(Solution,head[0],2)


















'''
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
The following are workings and rough solutions
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Latest working:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList_(head):
    print("The head is", head.val)
    print("The next is", head.next.val)
    returnList = []      
    current = head
    while current.next is not None:
        returnList.append(current)
        current = current.next
    returnList.append(current)
    print([x.val for x in returnList])
    return returnList

class Solution:

    def reverseKGroup(self, head, k):
        test = printList_(head)
        print(test)
        start = head
        currentNode = head
        previousSetStartingNode = head
        while currentNode is not None:
            #* At this stage, currentNode is the start of this unknown complete or incomplete set.
            #* This value is important; we want to see: if current cycle is in complete: set to the next set's element. Else set to None

            #* Here, we also must consider the continuation case: Set the first element to where?
            print("\n\n\nNew Iteration")
            
            startingNode = currentNode #* We store this important node. On the next cycle, we determine how to assign its value.
            if Solution.isComplete(self, currentNode, k):
                
                print(f"This is the last element of this set: {Solution.getThisSetLastElement(self, startingNode, k).val}")
                print(f"Current starting node {startingNode.val}")

                currentNode = Solution.getNextSetFirstElement(self, currentNode, k) #* Can be either None or an actual node.
                
                currentLast = Solution.getThisSetLastElement(self, startingNode, k)
                #print(f"Next element to iterate to: {currentNode.val}")
                Solution.setReverse(self, startingNode, k)
                print(f"This is after the reversal process. We want the starting node to be the currently, last node: {startingNode.val}")
                print(f"This is still your starting node value {startingNode.val}")
                if start == head:
                    start = currentLast
                print(f"This is your current set's last node {currentLast.val}")
                previousSetStartingNode.next = currentLast
                previousSetStartingNode = startingNode
                
                print(f"This is now your previousSetStartingNode {previousSetStartingNode.val}")
                startingNode.next = currentNode
                #* This case has implications: your previous set's last element must thus be reassigned to this set's last element.
                
            else:

                
                if currentNode == head:
                    start = Solution.getThisSetLastElement(self, startingNode, k)
                #* This case has implications: your previous set's last element must thus be reassigned to this set's first element.
                #* This case also means it is the end; last set.
                break
        
        
        printList_(start)

    def isComplete(self, startingNode, iterations):
        #* Iterations == k
        loops = 0
        currentNode = startingNode
        print(f"isComplete() to check: startingNode {startingNode.val}")
        while currentNode is not None:
            
            loops += 1

            if loops == iterations:
                print("isComplete returns True")
                return True
            currentNode = currentNode.next

        return False
    
    def setReverse(self, startingNode, iterations):
        loops = 0
        currentNode = startingNode
        previousNode = startingNode
        while loops != iterations:
            
            nodeToIterateNextTemporary = currentNode.next
            
            
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nodeToIterateNextTemporary
            loops += 1

    def getNextSetFirstElement(self, startingNode, iterations):
        #* Assumes set is complete
        loops = 0
        currentNode = startingNode
        while currentNode.next is not None:
            loops += 1
            if loops == iterations:
                return currentNode.next

            currentNode = currentNode.next
        return None
    
    def getThisSetLastElement(self, startingNode, iterations):
        #* Assumes set is complete
        loops = 0
        currentNode = startingNode
        while currentNode.next is not None:
            
            loops += 1
            if loops == iterations:
                return currentNode

            currentNode = currentNode.next
        return currentNode


from helperFunctions.arrayMatrixHelper import *
list_ = createListRandom("int",10,0,100)


head = []
for element in list_:
    head.append(ListNode(element))


for node in range(len(head)):
    if node+1 < len(head):
        head[node].next = head[node+1]


Solution.reverseKGroup(Solution,head[0],2)




Outdated working: Assumes head is a list
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList_(head):
            
    current = head[0]
    toPrint = ""
    print("HEAD HEAD HEAD ", current.val)
    while current.next is not None:
        toPrint += str(current.val) + " "
        current = current.next

    toPrint += str(current.val)

    print(toPrint)

class Solution:

    def reverseKGroup(self, head, k):
        #* Assumes that head is a list
        for _ in range(0, len(head), k):
            
            #* Setting the previous set's last element to this set's last element


            if _ + k < len(head): #* There exists at least one element in the next set
                print("The next set's first element will be at index:",_+k)

                if _ > 0: #* We need this otherwise thisSetFirst is undefined!
                    thisSetFirst.next = head[_ + k - 1] #* At this stage, thisSetFirst is referring to the previous set's last node!
            
            elif _ + k == len(head):
                print("This set is complete. (This is the last set)")

                if _ > 0: #* We need this otherwise thisSetFirst is undefined! 
                    thisSetFirst.next = head[_ + k - 1] #* At this stage, thisSetFirst is referring to the previous set's last node!

            else:
                print("This set is incomplete. The last set was the previous set!")

                if _ > 0: #* We need this otherwise thisSetFirst is undefined! 
                    thisSetFirst.next = head[_] #* At this stage, thisSetFirst is referring to the previous set's last node!



            if _ + k <= len(head): #* There exists at least one element in the next set, or this is the last set. Here then we begin the iterative reassignment
                thisSetFirst = head[_]
                thisSetLast = head[_ + k - 1]
                print(f"First of this set:{thisSetFirst.val}")
                print(f"Last of this set:{thisSetLast.val}")

                #* At this stage, we can assume that thisSetFirst.next will be set in the next cycle. But if this set is the last set, we need to handle it separately.
                #* A quick trick, then, is to set this node's .next to None. Because regardless, in the cycle, it will overwrite this None. If it does not, also good
                #* since this means that it is the last node of a complete cycle. So i will put this outside this if-block.

                #* UPDATE: We cannot do the above. The reason being is that if you set to None and the next set is incomplete, you will lose nodes. So we will need to do
                #* one more check if the current set is complete. If so, then we can set it to None. Only then do we set this node to None. Otherwise, we preserve the
                #* values

                currentNode = thisSetFirst.next #* We will begin the following while loop in the second element.
                previousNode = thisSetFirst
                while currentNode is not thisSetLast: #* We simply loop until the last node. Then, we will handle the last node's next outside this while-block.
                    nodeToIterateNextTemporary = currentNode.next
                    
                    print(f"previousNode: {previousNode.val}")
                    print(f"currentNode: {currentNode.val}")
                    currentNode.next = previousNode
                    previousNode = currentNode
                    currentNode = nodeToIterateNextTemporary
                
                print(f"previousNode: {previousNode.val}")
                print(f"currentNode: {currentNode.val}")
                currentNode.next = previousNode
                previousNode = currentNode

                if _ + k == len(head):
                    print("Complete set detected at the end of all iterations. Setting thisSetFirst.next to None")
                    thisSetFirst.next = None
                
                        
                        
        returnList = []      
        current = head[k-1]
        while current.next is not None:
            returnList.append(current)
            current = current.next
        print([x.val for x in returnList])
        return returnList

from helperFunctions.arrayMatrixHelper import *
list_ = createListRandom("int",10,0,100)


head = []
for element in list_:
    head.append(ListNode(element))


for node in range(len(head)):
    if node+1 < len(head):
        head[node].next = head[node+1]

    

Solution.reverseKGroup(Solution,head[0],5)





-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList_(head):
            
    current = head[0]
    toPrint = ""
    print("HEAD HEAD HEAD ", current.val)
    while current.next is not None:
        toPrint += str(current.val) + " "
        current = current.next

    toPrint += str(current.val)

    print(toPrint)

class Solution:

    def reverseKGroup(self, head, k):
        
        printList_(head)

        for _ in range(0, len(head), k):
            
            #* Setting the previous set's last element to this set's last element


            if _ + k < len(head): #* There exists at least one element in the next set
                print("The next set's first element will be at index:",_+k)

                if _ > 0: #* We need this otherwise thisSetFirst is undefined!
                    thisSetFirst.next = head[_ + k - 1] #* At this stage, thisSetFirst is referring to the previous set's last node!
            
            elif _ + k == len(head):
                print("This set is complete. (This is the last set)")

                if _ > 0: #* We need this otherwise thisSetFirst is undefined! 
                    thisSetFirst.next = head[_ + k - 1] #* At this stage, thisSetFirst is referring to the previous set's last node!

            else:
                print("This set is incomplete. The last set was the previous set!")

                if _ > 0: #* We need this otherwise thisSetFirst is undefined! 
                    thisSetFirst.next = head[_] #* At this stage, thisSetFirst is referring to the previous set's last node!



            if _ + k <= len(head): #* There exists at least one element in the next set, or this is the last set. Here then we begin the iterative reassignment
                thisSetFirst = head[_]
                thisSetLast = head[_ + k - 1]
                print(f"First of this set:{thisSetFirst.val}")
                print(f"Last of this set:{thisSetLast.val}")

                #* At this stage, we can assume that thisSetFirst.next will be set in the next cycle. But if this set is the last set, we need to handle it separately.
                #* A quick trick, then, is to set this node's .next to None. Because regardless, in the cycle, it will overwrite this None. If it does not, also good
                #* since this means that it is the last node of a complete cycle. So i will put this outside this if-block.

                #* UPDATE: We cannot do the above. The reason being is that if you set to None and the next set is incomplete, you will lose nodes. So we will need to do
                #* one more check if the current set is complete. If so, then we can set it to None. Only then do we set this node to None. Otherwise, we preserve the
                #* values

                currentNode = thisSetFirst.next #* We will begin the following while loop in the second element.
                previousNode = thisSetFirst
                while currentNode is not thisSetLast: #* We simply loop until the last node. Then, we will handle the last node's next outside this while-block.
                    nodeToIterateNextTemporary = currentNode.next
                    
                    print(f"previousNode: {previousNode.val}")
                    print(f"currentNode: {currentNode.val}")
                    currentNode.next = previousNode
                    previousNode = currentNode
                    currentNode = nodeToIterateNextTemporary
                
                print(f"previousNode: {previousNode.val}")
                print(f"currentNode: {currentNode.val}")
                currentNode.next = previousNode
                previousNode = currentNode

                if _ + k == len(head):
                    print("Complete set detected at the end of all iterations. Setting thisSetFirst.next to None")
                    thisSetFirst.next = None
                
                        
                        
              
        start = head[k-1]
        printList_([start])

from helperFunctions.arrayMatrixHelper import *
list_ = createListRandom("int",10,0,100)


head = []
for element in list_:
    head.append(ListNode(element))


for node in range(len(head)):
    if node+1 < len(head):
        head[node].next = head[node+1]

    

Solution.reverseKGroup(Solution,head,5)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




Working 2:
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList_(head):
            
    current = head[0]
    toPrint = ""
    print("HEAD HEAD HEAD ", current.val)
    while current.next is not None:
        toPrint += str(current.val) + " "
        current = current.next

    toPrint += str(current.val)

    print(toPrint)

class Solution:

    def reverseKGroup(self, head, k):
        
        printList_(head)

        for _ in range(0, len(head), k):
            print("Iteration:", _)
            lastPermissibleIndex = _ + k - 1
            print(_)
            if _ == 0:
                
                previousGroupsLastNode = head[0]

            if _ > 0:
                print(f"{previousGroupsLastNode.val}")
                print(f"Here we link {previousGroupsLastNode.val} to {currentNode.val}")
                previousGroupsLastNode.next = currentNode

            if lastPermissibleIndex < len(head): #* Means you should perform the operation on this group
                
                if lastPermissibleIndex + 1 < len(head): #* This means that there exists an element at least, beyond this group. Set the next of the first node to the first
                    #* element of the next set
                    print("POSSIBLY 1 more")
                    startNodeOfGroup = head[_]
                    previousNode = startNodeOfGroup
                    nextNodeNextIteration = startNodeOfGroup.next #* Store the second element to begin the iteratively solving
                    head[_].next = head[lastPermissibleIndex+1]

                    #* At this stage, we settled the base case. Can now begin on iteratively solving the standard cases

                    currentNode = nextNodeNextIteration #* Second element of the group
                    while currentNode.next is not head[lastPermissibleIndex+1]: #* We want to terminate the iteration the moment we meet the first node in the next set of nodes
                        nextNodeNextIteration = currentNode.next
                        currentNode.next = previousNode
                        previousNode = currentNode
                        currentNode = nextNodeNextIteration
                
                    currentNode.next = previousNode
                

                elif lastPermissibleIndex + 1 == len(head): #* This means that this current group is nicely the last group. Set the next of the first node to None.

                    startNodeOfGroup = head[_]
                    previousNode = startNodeOfGroup
                    nextNodeNextIteration = startNodeOfGroup.next #* Store the second element to begin the iteratively solving
                    head[_].next = None
                    
                    #* At this stage, we settled the base case. Can now begin on iteratively solving the standard cases

                    currentNode = nextNodeNextIteration #* Second element of the group
                    while currentNode.next is not None: #* We want to terminate the iteration the moment we meet the first node in the next set of nodes
                        nextNodeNextIteration = currentNode.next
                        currentNode.next = previousNode
                        previousNode = currentNode
                        currentNode = nextNodeNextIteration
                
                    currentNode.next = previousNode
                    
                
                        
              
        start = head[k-1]
        printList_([start])

from helperFunctions.arrayMatrixHelper import *
list_ = createListRandom("int",11,0,100)


head = []
for element in list_:
    head.append(ListNode(element))


for node in range(len(head)):
    if node+1 < len(head):
        head[node].next = head[node+1]

    

Solution.reverseKGroup(Solution,head,5)



-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Older workings:
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from helperFunctions.arrayMatrixHelper import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList_(head):
            
    current = head[0]
    toPrint = ""
    print("HEAD HEAD HEAD ", current.val)
    while current.next is not None:
        toPrint += str(current.val) + " "
        current = current.next

    toPrint += str(current.val)

    print(toPrint)

class Solution:

    def reverseKGroup(self, head, k):
        
        printList_(head)

        for _ in range(0, len(head), k):
            print("Iteration:", _)
            lastPermissibleIndex = _ + k - 1


            if lastPermissibleIndex < len(head): #* Means you should perform the operation on this group
                
                if lastPermissibleIndex + 1 < len(head): #* This means that there exists an element at least, beyond this group. Set the next of the first node to the first
                    #* element of the next set
                    if _ > 0:
                        previousGroupsLastNode = startNodeOfGroup
                    startNodeOfGroup = head[_]
                    previousNode = startNodeOfGroup
                    nextNodeNextIteration = startNodeOfGroup.next #* Store the second element to begin the iteratively solving
                    head[_].next = head[lastPermissibleIndex+1]

                    #* At this stage, we settled the base case. Can now begin on iteratively solving the standard cases

                    currentNode = nextNodeNextIteration #* Second element of the group
                    while currentNode.next is not head[lastPermissibleIndex+1]: #* We want to terminate the iteration the moment we meet the first node in the next set of nodes
                        nextNodeNextIteration = currentNode.next
                        currentNode.next = previousNode
                        previousNode = currentNode
                        currentNode = nextNodeNextIteration
                        print("TO iterate to", currentNode.val)
                
                    currentNode.next = previousNode
                
                    if _ > 0:
                        print(f"{previousGroupsLastNode.val}")
                        print(f"Here we link {previousGroupsLastNode.val} to {currentNode.val}")
                        previousGroupsLastNode.next = currentNode

                elif lastPermissibleIndex + 1 == len(head): #* This means that this current group is nicely the last group. Set the next of the first node to None.

                    if _ > 0:
                        previousGroupsLastNode = startNodeOfGroup
                    startNodeOfGroup = head[_]
                    previousNode = startNodeOfGroup
                    nextNodeNextIteration = startNodeOfGroup.next #* Store the second element to begin the iteratively solving
                    print("Next node iteration", nextNodeNextIteration.val)
                    print("Previous node", previousNode.val)
                    head[_].next = None
                    
                    #* At this stage, we settled the base case. Can now begin on iteratively solving the standard cases
                    currentNode = nextNodeNextIteration #* Second element of the group
                    while currentNode.next is not None: #* We want to terminate the iteration the moment we meet the first node in the next set of nodes
                        nextNodeNextIteration = currentNode.next
                        
                        print(f"Settign current node {currentNode.val}.next to previous node {previousNode.val}")
                        currentNode.next = previousNode
                        previousNode = currentNode
                        currentNode = nextNodeNextIteration
                        print("TO iterate to", currentNode.val)
                
                    currentNode.next = previousNode
                    print(f"Settign current node {currentNode.val}.next to previous node {previousNode.val}")
                    
                    if _ > 0:
                        print(f"{previousGroupsLastNode.val}")
                        print(f"Here we link {previousGroupsLastNode.val} to {currentNode.val}")
                        previousGroupsLastNode.next = currentNode
                
                        
              
        start = head[k-1]
        printList_([start])

list_ = createListRandom("int",10,0,100)


head = []
for element in list_:
    head.append(ListNode(element))


for node in range(len(head)):
    if node+1 < len(head):
        head[node].next = head[node+1]

    

Solution.reverseKGroup(Solution,head,5)'''

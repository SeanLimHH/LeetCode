'''
Problem : Hard

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Personal Interpretations (rough idea dump list; thought processes) : You need to figure out somehow to sort the merged arrays or obtain the sorted merged array FAST. 
This will be the hardest step. If you can figure this out then the other part will be easy - to extract the median.

Given two sorted arrays, how do you find its merged median?

Given two arrays, find the most optimal way to sort them and represent in one large array.

If let us say the two arrays each are 1 element in size, then we just do a basic comparison of both elements. The larger one ends up being concatenated to the right.

If you have two arrays each of 2 elements in size, the worst case scenario => need to analyse the four elements. How to do it fast?

Property of median? elements after it are greater than it. Similarly for elements before it.

7 elements => median is list[3]
4 elements => median is (list[1] + list[2])/2

so if N elements, N is odd => median is element in (N+1)/2
If N elements, N is even => median is (element in (N/2) + element (N/2)-1)/2
Can we combine such that we only analyse the median of the middle elements in between?

For example median of list A is 6, median of list B is 8, we can guarantee that the median of the new sorted list will be in between both. It can be one of them (if A is 6 OR
B is 6 and the median of newly sorted merge list is also 6, this means that the median for both lists are 6, individually.)

So we can drop the elements in the arrays of the lower half of the smaller median and the upper half of the larger median.

Now we need to think about the precision. We can guarantee that the median of the new list is in between both. But how to figure out precisely? Can we simply join the two
preserved list's elements and get its median? Does this work?

If A = [1, 3] and B = [2 , 6], the new list C = [3, 2] => 2.5?
So [1, 2, 3, 6] will have median 2.5. This is therefore valid.

Another example:
A = [3, 5, 7] and B = [1, 3, 9, 10]. Median of A is 5, median of B is 6.
C = [1, 3, 3, 5, 7, 9, 10]. Median of C == actual median == 5.
Using our method,
C = [5, 7, 1, 3]. Observe that we preserve the median value itself for if the number of elements in list is odd.
Then the sort C into [1, 3, 5, 7] and the median will be 4. This is wrong though...

Maybe preserve the upper median of B:
Using the same method,
C = [5, 7, 1, 3, 9].
Then the sort C into [1, 3, 5, 7, 9] and the median will be 5

Using this new hypothesis: preserve the median elements used in the new list.

Then one more thing we can do is remove away confirmed-wrong values? For example, if we know that the range is [5,6], we can filter out elements not in this range

The basic workflow can be this then:

1. Find out medians of lists A and B separately.
2. Find out which list has lower median and which has higher median.
3. For lower-median list, start from lower-median index, and check if the value is <= higher median. If so, add.
4. For the upper-median list, start from index 0, and check if the value is <= higher median

I thought of another method now:

What if, you measure the medians for both, then whilst creating the new list, check for even: if for A, element at index i <= median <= element at index i + 1, add.
for odd: if for B, element at index i == median => iterate through C => add in its appropriate place.
So for the example: A = [3, 5, 7] and B = [1, 3, 9, 10]. Median of A is 5, median of B is 6.
C = [3, 5, 9] => median is 5

Another test case for this method:
If A = [1, 3] and B = [2 , 6], the new list C = [1, 2, 3, 6] => median is 2.5
So [1, 2, 3, 6] will have median 2.5. This is therefore valid.

This method will be fast enough because no matter what values of m or n, worst case is iterating through the 4 elements. So it will take O(1) in time complexity.

To test this hypothesis, i will use my helper function to create random lists, then perform actual sort, then find its actual median. Then i will use the hypothesis function
to double check the validity. If this work, i will try to see why it works. Otherwise, i will explore other methods.

New hypothesis: Keep preserving the upper and lower halves of the two lists.
Is the final value in between the median of upper half of the lower-median list and the lower half of the higher-median list?
This is something like the Squeeze Theorem, where we squeeze the the medians of the two different lists separately towards a common value. 
We can test this by performing recursion.

Update: We need to consider the overlapping case.

The main idea: The median of the combined, sorted list will be in between the two medians of two separate lists.

The median of a list with exactly two elements should be studied more carefully than a list with more than 2 elements in the process detailed above.
This is very important because, based on my observations:
If you discard the upper or lower half of a list with size 2 (which is one element), this essentially means that you could potentially throw away the element that is the true
median.

This is because the case whereby one list is a strict subset of the other, and that the smaller list has one its elements smack middle of the larger one, then you will see 
that the right course of action is to extract out either one of the two elements.

The general idea i have will therefore be to brute force a very small case. This means that the general case, we whittle it down severely with recursion.
When either list is left with 2 elements, we will need to study the situation and brute force the solution accordingly.

Regardless, it will still be O(log n) because the brute forcing only applies possibly 2 scenarios: either list A has <= 2 elements, list B <= 2 elements. We can then manually
combine both lists and calculate the new median.

Based on Squeeze Theorem, if you can bring down both medians to a common one, it means you found the correct median.

One core idea i realise is that minusing even number off the total of the sets is safe. This is because the median will not get erased if you minus the edges wisely. However,
if you minus off uneven numbers off both sets, you might end up with a loss of information -- one set is even, the other set is odd. Such information will be lost and thereby
affecting the final result.

Therefore, a safe delete would include equal elements off both sets.

For nested scenario of one strict-subset of the other: we loop once more as per normal. The reason is because best case: you can minus 2 off the other larger set's median or 
plus 2 to it.

The worst case, which is that the median is one of this 2 elements, is then handled by looping once more: which compares which median is greater. If these' 2 elements median 
is greater than the larger set's median, we pick the first lower element of the two. Likewise for the other case, we pick the second upper element of the two. The natural 
occurrence will be that this happens through the standard looping.

Another information that i picked up is that there are situations of 3 + 2 where you have to handle manually. It is entirely possible that the median is in the last element
of the 3. To handle, we can analyse concretely all situations that has one element of size 2. The reason is that for such situation, we can possibly reconcile the two to the
final list by destroying it, then shifting the median of the list of 3 by 1 to the left, or that the median is in either the second or third element in the list with 3
elements. This can be resolved by computing if the largest of the 2-element list is less than the first element of the 3-element list, or vice-versa

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Analyses

Input(s) : nums1 = list. nums2 = list. Both contain integers. -106 <= nums1[i], nums2[i] <= 106 

Output(s) : an integer, representing the median of the merged array. The merged array must be sorted in ascending order.

Problem Rephrasal (If applicable) : 

The time complexity should be O(log m) + O(log n).

Subproblem : How many multiples of 2 (even number) can i remove from both lists such that the actual median value is still preserved?
Another valid subproblem will be : How can i remove (filter) out unwanted elements WHILST preserving the median in each iteration?
The solution for this is to, for even number of elements, preserve the middle two values and NOT FILTER THEM OUT! For odd number of elements, we just simply have to include 
the median number. 

UPDATE: It is NECESSARY to use the shorter list to control the filtering of elements. The reason is this: We want to play safe instead of accidentally deleting the median.

=> Decision variable(s) : Should I keep the upper/lower half of this array and discard the other half?
=> State variable(s) : The medians of each list separately

Base case(s): If one of list has 2 elements we can consider every possible scenarios in which we can reconcile (absorb) this 2-element list into the larger list.

Time complexity : O(log n) + O(log m). The reason is because we are continuously halving both lists. Upon one of the lists hitting 2 elements or less left, we terminate the 
entire recursion by computing its corresponding base case. For abstraction purposes, i have simply sorted 2 elements into the other list. Some cases that i can think of if
i were to manually implement the cases would be:
If the last element of the 2-element list is less than the first element of the other list; vice-versa. Then there will be an overlapping case where the first element of the
two-element list lies outside the other N-element list, but the second element lies within it. There will be another case where the two elements are encompassed by the
N-element list, and then the last case where the N-element list lies within the second element. I hope i have covered all angles here. But for simplicity of concept-wise,
and not to clutter the code, these base cases will be abstracted. A simple sort with a O(1) calculation median will do for this part, since it will not be too expensive, due
to the already whittled-down elements for both lists.

O(log n) + O(log m) = O(log (min(m,n))

Space complexity : O(log (min(m,n))

The idea for why it is min(m, n) => The moment the smaller list hits 2 elements or less, the recursion entirely stops. With this, you can immediately say that the runtime
as well as space complexity is constrained by the smaller list. (The smaller list controls the number of iterations TOTALLY.)


Personal thoughts and reflection: 

This was the hardest question so far, with me spending over easily 5 hours solving this question. Moving forward, i should think about the properties of the problem (median 
in this case; the concept of it). For this question, the realisation that the median of two lists lies in between the medians of the two  separate lists came quite late. A 
massive chunk of time, about half of the time, was quantifying the details of how to filter out. The strongest inspiration came when i realise that theoretically, visualise 
the final list with A + B in size. What we are essentially doing is filtering multiples of 2 from the left and right of the theoretical combined list from the sides.

With this visualisation, i realised that the removal of elements must be equal. This was also supported by the idea that if you remove separate elements from both lists, you 
will lose the essence of median. The meaning and coherence will also be lost: what i mean by this is that consider that the ideal median falls in index 3 of the theoretical
list of size 5. If you remove irregular elements from both list, you essentially, possibly, for example, remove 3 elements out of the 5. Then you will be left with 2 elements.
But the issue will thus be the loss of the actual median itself. With this, i noted that you must remove in multiples of 2.

Then, the concept that you should remove based on the smaller list came in much later as i was manipulating very tediously the two lists. For example, the situation where one
list has three elements and the other has 10 elements => i realised that you cannot just remove 5 elements on both lists. This means that if you remove in multiples of 2 +
this newfound fact => i begin thinking about using the smaller list as a basis for removal.

To summarise, the main idea was difficult but not too difficult to arrive to. The main issue was figuring out the implementation of smaller constraints and smaller subconcepts
that proved seriously hard.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

def solution(A, B): #* This is my final solution, a clean version without print statements.
    def main(A, B):
        def getMedian(list_):

            length = len(list_)

            if length % 2 == 1:
                return list_[int(length/2)]

            else:
                return (list_[int(length/2)-1] + list_[int(length/2)])/2
            
        def getNumberOfElementsRemoved(originalList, newList):

            return len(originalList) - len(newList)

        def getUpperHalfAndLowerHalf(upperList, lowerList):

            if len(upperList) < len(lowerList): #* upper list is shorter than lower list, we control how much to filter based on upper list
                if len(upperList) % 2 == 1:
                    newUpper = upperList[(len(upperList)//2):]
                    removed = getNumberOfElementsRemoved(upperList, newUpper)
                    newLower = lowerList[:len(lowerList)-removed]
                    return newUpper, newLower

                else:
                    #* Even case
                    newUpper = upperList[(len(upperList)//2)-1:]
                    removed = getNumberOfElementsRemoved(upperList, newUpper)
                    newLower = lowerList[:len(lowerList)-removed]
                    return newUpper, newLower
            
            else: #* lower list is shorter than upper list, we control how much to filter based on lower list
                if len(lowerList) % 2 == 1:
                    newLower = lowerList[:(len(lowerList)//2)+1]
                    removed = getNumberOfElementsRemoved(lowerList, newLower)
                    newUpper = upperList[removed:]
                    return newUpper, newLower

                else:
                    #* Even case
                    newLower = lowerList[:(len(lowerList)//2)+1]
                    removed = getNumberOfElementsRemoved(lowerList, newLower)
                    newUpper = upperList[removed:]
                    return newUpper, newLower
                
    
        if len(A) <= 2 or len(B) <= 2:
            D = sorted(A + B)
            return getMedian(D)

        medA = getMedian(A)
        medB = getMedian(B)

        if medA == medB:
            return medA

        elif medA > medB:
            newUpper, newLower = getUpperHalfAndLowerHalf(B,A)
            return main(newUpper, newLower)
        
        else:
            newUpper, newLower = getUpperHalfAndLowerHalf(A, B)
            return main(newUpper, newLower)
    
    return main(A, B)
















'''



def hypothesis(A, B): #* A and B are lists

    
    print(f"Input A {A}")

    print(f"Input B {B}")
    if len(A) == 0:
        if len(B) % 2:
            return B[len(B)//2]
        else:
            return (B[len(B)//2] + B[(len(B)//2)+1])/2
    elif len(B) == 0:
        if len(A) % 2:
            return A[len(A)//2]
        else:
            return (A[len(A)//2] + A[(len(A)//2)+1])/2

    #* For simplicity of abstraction, i will just concatenate both lists and then sort if either len(A) or len(B) <= 2
    #* But a basic approach is to cover all cases:
    if len(A) <= 2 or len(B) <= 2:
       
        D = sorted(A + B)
        print("RETURN",getMedian(D))
        return getMedian(D)
        

  
    print("CurrentA",A)
    print("CurrentB",B)
    medA = getMedian(A)
    medB = getMedian(B)

    if medA == medB:
        return medA

    elif medA > medB:
        print(f"{medA}>{medB}")
        print(getUpperHalfAndLowerHalf(B, A))
        newUpper, newLower = getUpperHalfAndLowerHalf(B,A)
        return hypothesis(newUpper, newLower)
        #return hypothesis(getLowerHalf(A), getUpperHalf(B))
        #C.append(getLowerHalf(A))
        #C.append(getUpperHalf(B))
    else:
        print(f"{medA}<{medB}")
        
        print(getUpperHalfAndLowerHalf(A, B))
        
        newUpper, newLower = getUpperHalfAndLowerHalf(A, B)
        return hypothesis(newUpper, newLower)
        #return hypothesis(getUpperHalf(A), getLowerHalf(B))
        #C.append(getLowerHalf(B))
        #C.append(getUpperHalf(A))

    match (len(C)):
        case 1:
            return C[0]
        case 2:
            return (C[0] + C[1])/2
        case 3:
            return C[1]
        case 4:
            return (C[1] + C[2])/2
        case _:
            print("Error occurred!")
            return None

def getMedian(list_):
    length = len(list_)

    if length % 2 == 1:
        return list_[int(length/2)]

    else:
        return (list_[int(length/2)-1] + list_[int(length/2)])/2


def getNumberOfElementsRemoved(originalList, newList):
    return len(originalList) - len(newList)

def getUpperHalfAndLowerHalf(upperList, lowerList):
    print(f'upperList enter {upperList}')
    print(f'lowerList enter {lowerList}')
    print("Length of upperList",len(upperList))
    print("Length of lowerList",len(lowerList))
    if len(upperList) < len(lowerList): #* upper list is shorter than lower list, we control how much to filter based on upper list
        if len(upperList) % 2 == 1:
            newUpper = upperList[(len(upperList)//2):]
            removed = getNumberOfElementsRemoved(upperList, newUpper)
            print('removed', removed)
            newLower = lowerList[:len(lowerList)-removed]

            print(f'newUpper {newUpper}')
            print(f'newLower {newLower}')
            return newUpper, newLower

        else:
            print("Even case")
            newUpper = upperList[(len(upperList)//2)-1:]
            print(len(upperList)//2-1)
            print(newUpper)
            print()
            removed = getNumberOfElementsRemoved(upperList, newUpper)
            print('removed', removed)
            newLower = lowerList[:len(lowerList)-removed]
            print(f'newUpper {newUpper}')
            print(f'newLower {newLower}')
            return newUpper, newLower
    
    else: #* lower list is shorter than upper list, we control how much to filter based on lower list
        if len(lowerList) % 2 == 1:
            newLower = lowerList[:(len(lowerList)//2)+1]
            removed = getNumberOfElementsRemoved(lowerList, newLower)
            print('removed', removed)
            newUpper = upperList[removed:]

            print(f'newUpper {newUpper}')
            print(f'newLower {newLower}')
            return newUpper, newLower

        else:
            print("Even case")
            newLower = lowerList[:(len(lowerList)//2)+1]
            removed = getNumberOfElementsRemoved(lowerList, newLower)
            print('removed', removed)
            newUpper = upperList[removed:]

            print(f'newUpper {newUpper}')
            print(f'newLower {newLower}')
            return newUpper, newLower
    
'''

def getMedian(list_):

        length = len(list_)

        if length % 2 == 1:
            return list_[int(length/2)]

        else:
            return (list_[int(length/2)-1] + list_[int(length/2)])/2
        
from helperFunctions.arrayMatrixHelper import *

from random import *
count = 0
print(count)
testSize = 500
for _ in range(testSize):
    ASize = randint(1,testSize)
    BSize = randint(1,testSize)
    A = createListRandom("int",ASize,0,10000,seed = _-1)
    B = createListRandom("int",BSize,0,10000,seed = _)
    A.sort()
    B.sort()
    C = sorted((A+B))
    print("Theoretical median:", getMedian(C))
    print("Solution results:", solution(A, B))
    if getMedian(C) == solution(A, B):
        count += 1
    print(f"Current correct:{count}/{testSize}")

        
'''
Problem : Easy

Given an integer array nums, move all 0's to the end of it while maintaining the 
relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Personal Interpretations:

Input: Array of numbers. Some of these numbers are 0s. We want to "shift" the zeros to the end
Output: The same array, now with all 0s shifted to the end of the array.

Constraint: In-place

Mark the start and end of the arrays with two pointers: let them be S and E.

The end of the array, more specifically, should be: the end of the array such that the last element is not zero.

We now assign pointer E as the proverbial mark of a imaginary split of the data (array).

So all elements on the right hand side of E will be 0s; all elements on the left hand side of E will be non-zeros.

We shall move pointer S slowly, from left-most of array to the point where it touches pointer E.
The moment it touches, we can deduce that we have iterated through all the elements,
where the elements are non-zero or zero.

Now, throughout this iteration: if the element is zero, just move it to index pointer E.

Here, we highlight the constraint - in-place. So this process more involved then just insertion. We need to perform swapping.

Then, since we have this constraint of in-place and swapping as an implicit requirement, we should reconfigure our concept of
pointer E.

We cannot also delete and then append. So the "right" way would be to swap.

Now, since we have to swap, the options are limited:
1. Swap a zero with a non-zero.

The ordering of the elements after swapped must be revised and reconsidered.

Consider the example provided: [0,1,0,3,12]

Then, if we use our above's conceptual model: pointer S => index 0 and pointer E => index 4.
This would fail, since after swapping, we would get: [12,1,0,3,0].
The order cannot be recovered; for 12 is now the first element and our S now points to index 1; E to index 3

This conceptual model i proposed above would not work.

Some key considerations why it would fail: there is a "jumping" over of >= 1 non-zero elements during the swap.
This is an informal invariant, which we can say that the algorithm should not ever perform during a swap operation.

Then, using this fact, this invariant, we deduce that the pointers must be configured in a way such that this fact
does not occur.

This implies one solution: instant swapping, of non-zero and zero elements with pointers both starting from the front
of the array.

This way, this algorithm holds this invariant and it should be able to work.

Testing this hypothesis with the new conceptualised pointers S and E, we have:

[0,1,0,3,12]

S and E will now point at the start of the index: index 0.
We iterate one pointer - let this be E and NOT S.
E will iterate rightwards.

As E detects '1', it should swap with S and we will get [1,0,0,3,12].

Here, we observe that the conceptualisation of the pointers are very loose.

So more concretely, we should say that:

Let S be the pointer that points at the first zero, and let E be the pointer that points at the first non-zero.

We iterate E from index 0 to the end of the array.

Each time E points at a non-zero, we will swap values at S and E.

Then, we shall increment S by 1.

Next, we would have to set E to be S + 1. Then we can do the same iteration and repeat as above.

We terminate this process when E is just out of range (equal to length of array).

Testing this hypothesis:

[0,1,0,3,12]
S:0, E:0
Iterate E until non-zero detected. Once non-zero is detected, swap values in S and E.

[0,1,0,3,12]
S:0, E:1
After swap:

[1,0,0,3,12]
S:0, E:1
Set S = S+1, then E = S + 1:

[1,0,0,3,12]
S:1, E:2
Repeat the iteration as above...

[1,0,0,3,12]
S:1, E:3
Then swap:

[1,3,0,0,12]
S:1, E:3
Set S = S+1, then E = S + 1:

[1,3,0,0,12]
S:2, E:3

...
...
...

[1,3,12,0,12]
S:3, E:4

This algorithm should work

#TODO: Implement code

'''
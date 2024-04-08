'''
Problem: Easy

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 

Any answer with a calculation error less than 10-5 will be accepted.

Personal Interpretations:

Premise 1: Integer array of n elements
Premise 2: Integer k
Show: Find a contiguous subarray: len(subarray) = k AND the subarray has the highest maximum average value.

Simplified understanding of question: Length of subarray must be of the second input, and it must have highest maximum average value.

Useful information:
k is implied to be <= n; otherwise question would not make sense

Contiguous subarray simplifies the problem.

Solution idea:

Have two pointers that demarcate what we want - the maximum average value between the two pointers.

Position one of the pointers at the start

Move the other pointer to the end iteratively, and update the maximum average value? :
This can actually be simplified. We know that the array is length k. So we can already mark out a k-length pointer range. And move this

"window" across the array.

#TODO: Implement code
'''



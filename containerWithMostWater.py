'''
Problem: Medium

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are:

(i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Personal Interpretations:

Input: An array of numbers. Length is n. Each element represents a conceptual vertical line.
The endpoints of this conceptual vertical lines are represented as a tuple; and mark the bottom and top
of the line.
Output: Two lines, from the same array of numbers. These two lines must form a container where 
the minimum of the two heights is maximised across all the pairs of elements in the array
Constraint(s): -

We can simplify the understanding of the inputs - the endpoint that we should pay attention to is the second
tuple; for it changes in value for each element (apart from the index value).

What we essentially want are top two highest lines in the array.

The idea would be to use a marker at the start and end of the array.
Then, iterate both towards a "centre", where they are touching / adjacent to each other.

This iteration described, will only be O(n) and check for all possible container heights.

At each iteration, all is left to do is keep track of: min(height 1, height 2) for both lines and indices.

The goal is to find the largest pair of min(height 1, height 2), for all possible pairs in the iterations.

This algorithm should work as described above.

#TODO: Implement code
'''
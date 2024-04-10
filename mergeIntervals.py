'''
Problem : Medium

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Personal Interpretations:

Input: Multiple arrays in an array, each has a starting value and ending value; defining a range
Output: "Merged" arrays whereby we merge the ranges together of all arrays.

Difficulty comes from the complex ordering and lack of structure.
It is not easy to even think of a way to check it.

Hence we have to perform some sort to organise the information.

If we sort all by their starting values, like in the example; we get: [[1,3],[2,6],[8,10],[15,18]]

At this point, it would help to visually think about the arrays in a horizontal row literally.

Then we could have two pointers: one where it looks at the first element of the first array.
Then the second looks at the second element. The second pointer: we could iterate over all other elements.

The idea is that since the first numbers are sorted, the next adjacent contiguous array's first number must be the next
smallest number in all the set of numbers in the arrays.

Iterating over the second index in the array, then to the next adjacent contiguous array, then all the way to the end;
or the moment where there is "jump".

This concept could be summarised as: move the second pointer UNTIL the starting index of the array DOES NOT overlap
with the first pointer.

If a "jump" is detected (an overlap occurs), then set the first pointer to the second pointer; and then the second pointer to
its index + 1.

Also, if a "jump" is detected, conclude that range (first pointer value : second pointer value).



#TODO: Implement code
'''
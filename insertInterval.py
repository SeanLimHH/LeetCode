'''
Problem: Medium

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the 
start and the end of the ith interval and intervals is sorted in ascending order by starti.

You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals 
still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.


Personal Interpretations:

Similar to the mergeIntervals.py problem, we have a similar problem here.

Inputs: We are given a "sorted" array of arrays. More concretely, start index is sorted; "lambda x: x[0]" in the arrays.

Then we are also given a insertion array to insert.

Output: Merged array with array inserted. For cases of overlap, combine and return as a single array.

Based on the question, we can identify that the hardest part of the problem is figuring out where to insert.

Because we can reuse the concept of the merging of intervals in mergeIntervals.py to merge afterwards; after inserting the
new array.

So we could do the same of having two pointers:
One points to first index of first array
Second points to second index of first array.
From here, we iterate the second pointer rightwards.

The complexity of insertion arises in the following ways:
1. Inserted array is (half) overlapping with the current array X; its starting index is < last index of X
2. Inserted array is not overlapping with any arrays - easy, no problem. Just insert the array in the right index of arrays.
3. Inserted array is (half) overlapping with current array X: its ending index is > first index of X
4. Inserted array is within the current array X - easy, no problem. Just ignore and return the same array. 

We should thus focus our analyses on 1. and 3.

On 1., we would have one pointer at the start of index X, and ideally, the second pointer eventually at the end of inserted
array. These two arrays should become a singular one.

On 3., we would have one pointer at the start of inserted array, and ideally, the second pointer at the end of itself.
These two arrays should become a singular one.

Since we need not modify the arrays in-place, this would be simpler to implement:

Have the same set up as above:

So we could do the same of having two pointers:
One points to first index of first array
Second points to second index of first array.
From here, we iterate the second pointer rightwards.

We could, also, keep track of the start of the array to be inserted.
This start value could be denoted as Y, and its end value be Z.
So we want to integrate [Y,Z] into our existing arrays.

Now, with iteration of the second pointer, we do have to check for each iteration:

Is the second pointer > Y. If so, it would be case 1.
Here, i notice that we must also then, consider the case of double overlap.
This would be case 5: both cases 1 and 3 combined. One hypothesis to solve this issue:

We pursue with the focus on second pointer. If it is > Y, it does indicate case 1 being true.
Then, we can and should move the pointer to the next adjacent existing array's first index.

Because only then, can we compare this value with Z.
In such a case: if this value is < Z: we know that at this point, our new merged array would
consist of these 3 arrays combined into 1; starting index is as per the first array; the last index's value
is Z. This would form the new interval.

And if, the other case is true: if this value is >= Z: we know that, at this point, we should
proceed iterating the second pointer to the end of the adjacent existing array's second index.
Then, because we already cover the inserted array's ideal position, we would conclude and return a merged
array that combines the 3 arrays together.

#TODO: Implement code
'''
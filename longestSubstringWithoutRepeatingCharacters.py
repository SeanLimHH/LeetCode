'''
Problem: Medium

Given a string s, find the length of the longest substring without repeating characters.

Personal Interpretations:

Input: a string of characters
Output: longest substring of the characters - its length
Constraint(s): No repeating characters

The substring keyword implies a contiguous array.

We can use two pointers, position them both at the start of the string.
Then move one of the pointers rightwards, UNTIL it hits a repeated character.
The moment it sees a repeated character, we mark out the length of this range.

At this point: move both pointers to the this repeated character.
Then repeat: move one of the pointer rightwards, UNTIL it hits a repeated character...

This repeats until the pointer that is moved rightwards hits the end of the string s. Then
we can conclude this process.

Next, we just have to compare the lengths of each of this ranges.

#TODO: Implement code
'''
'''Problem : Difficulty unsure, i think it is medium

Question from school: Subsequence

Suppose your set of valid words is {“hot”, “hots”, “shot”, “shots”, “hotshot”, “hotshots”}. Find the number of ways to partition the string “hotshotshotshots” into a sequence
of valid words.

Assume you have a procedure Is word(s, i, j) that, for any string s[1..n] of length n and two numbers 1 ≤ i ≤ j ≤ n, determines if the substring s[i..j] is a valid word. We
wish to determine how many ways there are to partition a given string into a sequence of valid words.

(a) Find a recurrence/recurrences for this problem. Specify the base cases for your recurrence(s). In your answer, please specify clearly (in English) how you define your 
sub-problems, and what the input and output of your function represents for each sub-problem you have identified.

(b) Design an algorithm to solve the problem with dynamic programming. Please give your algorithm in pseudocode.

(c) Analyze the time and space complexity of your algorithm.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Personal Interpretations :

This was done during my school term quite a while back, so i will try and remember as many details as i can, otherwise i will provide my new insights on the problem.

I remembered solving this by drawing a tree that segments out the words. So it lists all permutations but also keep tracks of the segmented words from the string. This idea,
if you can translate it into code, will solve the problem.

This is essentially: Scan the first first left-most part of the string with any valid word in valid_words. If you can find one, then pursue an iteration downwards.
This step should run many times.

Then, only if we can have a nice complete finish of matching (no more remaining characters), then we can add 1 to a counter.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Analyses

Input(s) :
list of valid words, and the target string word itself.

Output : Integer value representing the number of ways you can split it.

Subproblem : What is the number of valid partitions of given sub-word.

State variable(s) : The number of complete(word == "") sub-strings in given string. This is the "count" variable.

Recurrence: Given a prefix X, recur the function with the remaining suffix of the input word with prefix X removed.
Base case: word == "", then you add +1 to the count

The time complexity of my solution is: It depends on space complexity. If there are more subwords to check, then this will take longer. If we assume that the size of valid
words increases as the length of the word increases, this is O(n^2). Otherwise O(n). (because we loop through a constant size n times)

The space complexity is O(n) if we assume that the size of valid words increases as the length of the word increases. Otherwise it is O(1)
'''
valid_words = ["hot","hots","shot","shots","hotshot","hotshots"]
word = "hotshotshotshots"
count = 0
def is_word(s,i,j):
    if s[i:j] in valid_words:
        return True
    return False

def partition(valid_words, word):
    global count
    if word == "":
        count += 1
    else:
        for i in range(len(valid_words)):
            if word[:len(valid_words[i])] == valid_words[i]:
                partition(valid_words,word[len(valid_words[i]):])

partition(valid_words,word)
print(count)

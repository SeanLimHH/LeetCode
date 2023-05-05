'''Problem : Difficulty unsure, i think it is hard

Question from school: Triangle Game

Alice and Bob are playing a game, where n objects are put in a pile in the middle of a table. Players take turns to remove one or more objects from the table, but the number
of objects removed must be a triangle number (i.e. there must be a positive integer i such that the number of objects removed is i(i+1)/2). A player loses when they are
forced to remove the last object from the table. (If both players play optimally, this will happen only if there is one object left, since 1 is a triangle number, and a player
can always remove 1 object from a pile with at least 2 objects.)

Suppose the value of n has been decided, and Alice is allowed to decide whether to play first or second. Should Alice play first or second, in order to guarantee that she can
win the game (assuming that Alice plays optimally)?

(a) Find a recurrence/recurrences for this problem. Specify the base cases for your recurrence(s). In your answer, please specify clearly (in English) how you define your 
sub-problems, and what the input and output of your function represents for each sub-problem you have identified.

(b) Design an algorithm to solve the problem with dynamic programming. Please give your algorithm in pseudocode.

(c) Analyze the time and space complexity of your algorithm.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Personal Interpretations :

This was done during my school term quite a while back, so i will try and remember as many details as i can, otherwise i will provide my new insights on the problem.

The question's problem is compoundingly complicated. Think of a tree that grows more and more branches. This is true - look at a large number like 5731. How will then either
player figure out, by manual methods, who has the theoretical way to win?

Are there many ways to win, or just one? It seems that there should only be one. Because if you break down the problem to subproblem:

Subproblem: Given n = 1, and player X starts first, who is guaranteed to win? The answer is player Y (Assume there are two players X and Y)
=> Given n = 2, and player X starts first, who is guaranteed to win? Player X
=> Given n = 3, and player X starts first, who is guaranteed to win? Player Y (X - 1, Y - 1, X - 1)
...
This repeats, but we can clearly see there is definitely a singular winner based on who starts first.

This hints to an approach - i call it the current-player-win-or-lose table. It simply shows this: on which turn, will the current player win or lose.
This simple subproblem is easier to analyse, and is very useful. The reason is this: if based on this table, you can force your enemy (next player) to fall on a row n where
the current player loses, you will win the game.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Analyses

Input(s) :
1. n, the number of objects on the table

Output :  "Win" or "Lose" of player X which assumes that player X starts first.

Subproblem : Given n, and player X starts first, who is guaranteed to win? (Assume there are two players X and Y)
=> Decision variable(s) : Can i remove triangle-number objects from the table such that with the remaining number of objects on the table, the current player will lose?
(Opponent)

=> State variable(s) : The record for all objects up to n on the table => will the player on this turn dealt this number of objects win or lose?
Optimal-substructure? : Yes. If you can, for step X, find out who wins or who loses, you can force your opponent to this state by removing a triangle number

Recurrence: f(n) = "win" if f(n-X) = "lose" where X is a triangle number. Else f(n) = "lose" if you cannot find a triangle number X where f(n-X) = "lose"
Base case: f(1) = "lose"

The time complexity of my solution is:
Generating the triangle numbers: O(n). Because we do it n times.
Nested for loops: The outer one runs n times. In each of this iteration, there is another n iterations (looping through triangle numbers). This is O(n^2).
The rest are constant time.
So the time complexity of my solution is O(n^2).

The space complexity is O(n) because O(n) space for triangle numbers, O(n) space for f. O(n) + O(n) = O(2n) which is still O(n).
'''
def triangleGame(n):
    triangleNumbers = []
    for i in range(n):
        triangleNumbers.append(int((i*(i+1))/2))

    f = ["NIL"] * n
    f[0] = "lose"
    for i in range(1,n):
        if f[i] == "NIL":
            for t in triangleNumbers:
                if i-t >= 0:
                    if f[i-t] == "lose":
                        f[i] = "win"
                        break
            if f[i] == "NIL": # Still NIL; cannot find a win == lose
                f[i] = "lose"

    return f[n-1]


n = 9
print(triangleGame(n))
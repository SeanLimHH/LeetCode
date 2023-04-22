'''
Problem : Difficulty unsure

Question from friend: Tourist

There are n cities in a row with city 1 being the leftmost city and city n being the rightmost city. There is one hotel in each city. A tourist has c gold coins.

Each city has a hotel. Staying in the hotel in city i rewards the tourist with k_i happiness.

The tourist can stay in each hotel at most once.

A tourist begins from city 1 (the leftmost city). He can repeatedly perform the following actions until he runs out of gold coins.

1. Move right to the next city. Costs 1 gold coin.
2. Stay in the hotel in the current city. Costs 1 gold coin.

What is the maximum happiness the tourist can get?

----------------------------------------------------------------------------------------------------------------------------------------------------------------

Personal Interpretations :

Information: 1 city == 1 hotel == i as the index referring to which hotel. There are in total n hotels.

Two actions: Move left, or stay ONE MORE NIGHT.

Constraints :

1. Cannot return back to same hotel.
2. Can only travel to adjacent right hotel. Rightwards, one hotel per trip only.
3. Can only stay an extra 1 day or 1 night.

----------------------------------------------------------------------------------------------------------------------------------------------------------------
Analyses

Input(s) :
1. k, a list of hotels. Each element is the happiness of each hotel.
2. c, an integer. Represents the number of gold coins.

Output : An integer representing maximum theoretical happiness achieved.

Problem Rephrasal (If applicable) : 

You are at grid 1. 
You have c coins. You can only move right or stay in one step. Each step costs 1 coin. 
Staying at grid i awards k_i points. Upon touching a new grid i, you are also awarded k_i points.

Find the theoretical maximum of points you can attain

Subproblem : Find the best sequence of steps that maximises your points
=> Subproblem : Is my current sequence of steps the best sequence?
=> Subproblem : How do i know if my sequence of steps is the best?
=> Decision variable(s) : Stay one more night or move right to maximise final points.
=> State variable(s) : Is my decision in the sequence of best steps? => The current sequence and its corresponding points.

Optimal-substructure? : Yes. If you can, for step X, find out if your sequence up to step X maximises your points, you can build up to the last step, step C.

Subproblem solution ideas (rough idea dump list; thought processes) : Track theoretical maximum at each step? Cannot. This type of problem is like you start with one node, then
branch off to like 100 different nodes in the middle, then you have possibly 100 different nodes to end off with. This means that you cannot work forward, nor backwards. A smarter
algorithm NOT greedy must be used. Bottom-up approach will be very hard. I will try the top-down approach. But it also cannot be easy. This is because remember, we have 100 possible ending nodes.
The only confirmation and starting point we have is literally the starting point.
But what if you explore backwards. Theoretically, if you have C coins, the farthest hotel is hotel C. Then you work backwards. Is there a way this would fail? 
You have to play with both constraints - the coins and steps and points.

If you have 1 coin ==> you have 1 step ==> What is the best move? Of course, this would be simply staying in current hotel.
if you have 2 coins ==> you have 2 steps ==> What is the best move? If i can figure this out, i can solve the entire question. So i will focus on this question from now onwards.

2D matrix? Literally you start from the top left. Moving down means you stay. Moving right means you move right. Each grid can represent points.

This works maybe? Cause if you fill up from top left, at each grid you can see what is the points you attained. Yes. This should work.

So we transform our problem to a 2D matrix one.

Transformed :

Subproblem solution: Each cell of a 2D matrix represents the theoretical maximum of steps that reaches the current cell. The column of this cell is significant - it represents the hotel i. Each cell element
is the hotel points awarded.

r = row, c = column

Recurrence formula : f(r, c) = max(f(r-1,c), f(r, c-1)) + k(c+1)

Base case(s):

For column = 0 < n, row = 1: f(1, n) = 0
For column = 0, row = 1: f(1, 0) = k(1)

----------------------------------------------------------------------------------------------------------------------------------------------------------------

The following is not necessary because the problem is basically solved, but is there for good practice and to log my thought processes.

State variable(s) : Theoretical maximum points of said sequence of steps.

So there is another state variable with sequence of steps. Then one with theoretical maximum points (of each sequence).

We encode both concepts using a 2D matrix.

Decision variable(s) : Either to stay (go down in the matrix) or go to the next hotel (go right in the matrix).

Some learning insights : If i can figure out a way to visualise the literal actions + visualise the state values (cell values), you can solve the problem in mind. So figuring out roughly what do you want to solve -
the state and decision variables - enables you to start exploring visualisation methods.

The key question that led me to figure out that it requires a 2D matrix was this line above : 
if you have 2 coins ==> you have 2 steps ==> What is the best move? If i can figure this out, i can solve the entire question. So i will focus on this question from now onwards.

I think it was because of "2 steps". I related this 2 steps to another 2 steps i was thinking => Staying or moving. Then i realise that 2D matrices also allow state variables to be "stored". This was needed because
i wanted to know the maximum value at each step.

Proof:

Base case 1 : For column = 0 < n, row = 1: f(1, n) = 0. This is because tourist did not stay in any hotels => No happiness is earned.

Base case 2 : For column = 0, row = 1: f(1, 0) = k(1). This is because tourist stays in hotel 1. This is the first hotel, hence the tourist's points is simply k(1).

Recurrence cases: Using the above two, we fill a 2D-matrix row-wise first, then column-wise. The idea is that we do not know the steps leading up to the cell, but we can know the theoretical maximum of happiness points
the tourist can achieve if he takes the "best" sequence of steps which we do not know and reaches this cell. If you focus on f(1, 1), you can see that it is has considered all cases to reach this step. By repeating this,
we can see that the tourist considers all possible steps' theoretical maximum of happiness points

Time complexity : O(n^2)

Space complexity : O(n^2)

----------------------------------------------------------------------------------------------------------------------------------------------------------------

Update:
I realise that the 2D matrix is a variant of the usual one. You will have a upper right triangle, and your constraint you must set is: row index + column index <= C. This is the searchable area.
'''
from arrayMatrixHelper import *
from togglePrinting import *

printer = TogglePrint()
printer.disable()



def tourist(k, c):
    
    matrix = create2DMatrix(c, c, 0)
    matrix = setEntry(matrix, 1, 0, k[0])
    
    rows = getRows(matrix)
    columns = getColumns(matrix)
    for row in range(1, rows):
        for column in range(row-1, columns):
            if column <= getColumns(k) and (row + column <= c):
                setEntry(matrix, row, column, max(getEntry(matrix,row-1,column),getEntry(matrix,row,column-1))+k[column])

    return getMax(matrix)


n = 6
c = 4

k = createListRandom("int", n, 1, 10)
#* [7, 7, 1, 5, 9, 8]

printer.enable()
print(tourist(k,c))
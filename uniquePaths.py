'''
Problem : Medium

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

https://leetcode.com/problems/unique-paths/description/

Personal Interpretations:

Input : Two integers representing the row and column size of the grid

Output : Total unique paths to get from top left of grid to bottom right of grid

Subproblem : Given current grid, what is the number of ways to get here?

Optimal-substructure? : Yes, because solving a subproblem leads to a solution to the main problem

State variable(s) : The number of unique ways to reach current grid

Decision variable(s) : Travel either right or down

Recurrence Formula : F(row, col) = F(row - 1, col) + F(row, col - 1)

By solving this, we can chain-construct the number of ways to get to any grid we want

It can also be solved via math through permutations and combinations.
'''
def uniquePaths(m: int, n: int) -> int:
    # Rows = m
    # Columns = n
    memo = [[0 for i in range(n)] for j in range(m)]
    for row in range(m):
        memo[row][0] = 1
    for col in range(n):
        memo[0][col] = 1
    for r in range(1,m):
        for c in range(1,n):
            memo[r][c] = memo[r][c-1] + memo[r-1][c]
    return memo[m-1][n-1]

def create2DMatrix(rows, columns, initialisedValue = 0):
    return [[initialisedValue for i in range(columns)] for j in range(rows)]

def printMatrix(matrix):
    print("Display of two-dimensional matrix:")
    print("Number of rows:",len(matrix))
    print("Number of columns:",len(matrix[0]))

    for row in matrix:
        for col in row:
            print(f"{col}  ", end="")
        print()

def getEntry(matrix, rowIndex, columnIndex):
    print("\ngetEntry():")
    try:
        rowIndex = int(rowIndex)
        columnIndex = int(columnIndex)
        if rowIndex >= len(matrix):
            print("Row index is larger than number of rows! Please enter a valid row index!")
        if columnIndex >= len(matrix):
            print("Column index is larger than number of columns! Please enter a valid column index!")
    except ValueError:
        print("Please enter a valid integer >= 0 for row index and column index!")
        return None
    
    print(f"Value of cell: row index {rowIndex} column index {columnIndex} is :", matrix[rowIndex][columnIndex])
    return matrix[rowIndex][columnIndex]

def updateEntry(matrix, rowIndex, columnIndex, newValue):
    print("\nupdateEntry():")
    try:
        rowIndex = int(rowIndex)
        columnIndex = int(columnIndex)
        if rowIndex >= len(matrix):
            print("Row index is larger than number of rows! Please enter a valid row index!")
        if columnIndex >= len(matrix):
            print("Column index is larger than number of columns! Please enter a valid column index!")
    except ValueError:
        print("Please enter a valid integer >= 0 for row index and column index!")
        return None
    
    print(f"Value of cell to be updated: row index {rowIndex} column index {columnIndex}")
    print(f"Current value is: {matrix[rowIndex][columnIndex]}")
    print(f"New value to be update in cell: {newValue}")
    return matrix[rowIndex][columnIndex]

def setLeftColumn(matrix, value):
    print("\nsetLeftColumn():")
    if not isinstance(value, float) and not isinstance(value, int):
        print("Input value is not numeric! Please enter a valid value!")
        return None

    for row in range(len(matrix)):
        matrix[row][0] = value
    
    print(f"Setting left column to value: {value}")
    print("New matrix:")
    printMatrix(matrix)

def setTopRow(matrix, value):
    print("\nsetTopRow():")
    if not isinstance(value, float) and not isinstance(value, int):
        print("Input value is not numeric! Please enter a valid value!")
        return None

    for column in range(len(matrix[0])):
        matrix[0][column] = value
    
    print(f"Setting top row to value: {value}")
    print("New matrix:")
    printMatrix(matrix)

def setDiagonal(matrix, value): # Assumes matrix is square!
    print("\nsetDiagonal():")
    if len(matrix) != len(matrix[0]):
        print("Matrix is not square! setDiagonal(matrix, value) will not work! Exiting...")
        return None

    if not isinstance(value, float) and not isinstance(value, int):
        print("Input value is not numeric! Please enter a valid value!")
        return None

    for index in range(len(matrix)):
        matrix[index][index] = value
    
    print(f"Setting diagonal to value: {value}")
    print("New matrix:")
    printMatrix(matrix)

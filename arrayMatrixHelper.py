def createList(size, initialisedValue = 0):
    return [initialisedValue for _ in range(size)]

def printList(list_):
    try:
        if (isinstance(list_[0],list)):
            print("Error occurred.")
            print("The input for printList() is not a list! Please input the correct data structure!")
            return None
        
        if (isinstance(list_,str)):
            print("Error occurred.")
            print("The input for printList() is not a list! Please input the correct data structure!")
            return None
        
    except TypeError:
            print("Error occurred.")
            print("The input for printList() is not a list! Please input the correct data structure!")
            return None
    
    print("Display of list:")
    print("Number of columns (size):",len(list_))
    print()
    maxLengthForFormatting = 0

    for element in list_:
        if len(str(element)) > maxLengthForFormatting:
                maxLengthForFormatting = len(str(element))

    for element in list_:
        print(f"{element:<{2*maxLengthForFormatting}}  ", end="")
    print("\n")

def create2DMatrix(rows, columns, initialisedValue = 0):
    return [[initialisedValue for _ in range(columns)] for _ in range(rows)]

def print2DMatrix(matrix):
    try:
        if (not isinstance(matrix[0],list)):
            print("Error occurred.")
            print("The input for print2DMatrix() is not a 2D array or matrix! Please input the correct data structure!")
            return None
        
        if (isinstance(matrix, str)):
            print("Error occurred.")
            print("The input for print2DMatrix() is not a list! Please input the correct data structure!")
            return None
        
    except TypeError:
        print("Error occurred.")
        print("The input for print2DMatrix() is not a 2D array or matrix! Please input the correct data structure!")
        return None
    
    print("Display of two-dimensional matrix:")
    print("Number of rows:",len(matrix))
    print("Number of columns:",len(matrix[0]))
    print()

    maxLengthForFormatting = 0

    for row in matrix:
        for col in row:
            if len(str(col)) > maxLengthForFormatting:
                maxLengthForFormatting = len(str(col))
                
    for row in matrix:
        for col in row:
            print(f"{col:<{2*maxLengthForFormatting}}", end="")
        print()
    print()

def getEntry(matrix, rowIndex, columnIndex):
    print("\ngetEntry(): Returns the entry in the matrix at row rowIndex and column columnIndex")
    try:
        rowIndex = int(rowIndex)
        columnIndex = int(columnIndex)

        if rowIndex >= len(matrix):
            print("Error occurred.")
            print("Row index is larger than number of rows! Please enter a valid row index!")

        if columnIndex >= len(matrix):
            print("Error occurred.")
            print("Column index is larger than number of columns! Please enter a valid column index!")

    except ValueError:
        print("Please enter a valid integer >= 0 for row index and column index!")
        return None
    
    print(f"Value of cell: row index {rowIndex} column index {columnIndex} is :", matrix[rowIndex][columnIndex])
    return matrix[rowIndex][columnIndex]

def setEntry(matrix, rowIndex, columnIndex, newValue):
    print("\nsetEntry(): Updates entry of matrix. It is simply matrix[rowIndex][columnIndex] = value")
    try:
        rowIndex = int(rowIndex)
        columnIndex = int(columnIndex)

        if rowIndex >= len(matrix):
            print("Error occurred.")
            print("Row index is larger than number of rows! Please enter a valid row index!")

        if columnIndex >= len(matrix):
            print("Error occurred.")
            print("Column index is larger than number of columns! Please enter a valid column index!")
            
    except ValueError:
        print("Please enter a valid integer >= 0 for row index and column index!")
        return None
    
    print(f"Value of cell to be updated: row index {rowIndex} column index {columnIndex}")
    print(f"Current value is: {matrix[rowIndex][columnIndex]}")
    print(f"New value to be updated in cell [{rowIndex}][{columnIndex}]: {newValue}")
    matrix[rowIndex][columnIndex] = newValue
    return matrix

def setLeftColumn(matrix, value):
    print("\nsetLeftColumn(): Sets all elements in the first column to the same value")

    if isinstance(matrix[0],list): # * Is a matrix
        
        if not isinstance(value, float) and not isinstance(value, int):
            print("Error occurred.")
            print("Input value is not numeric! Please enter a valid value!")
            return None
        
        print(f"Setting left column to value: {value}")
        
        for row in range(len(matrix)):
            matrix[row][0] = value

        print("New matrix:")
        print2DMatrix(matrix)

    elif isinstance(matrix, list): # * Is a list
        if not isinstance(value, float) and not isinstance(value, int):
            print("Error occurred.")
            print("Input value is not numeric! Please enter a valid value!")
            return None
        
        print(f"Setting left column to value: {value}")
        
        matrix[0] = value

        print("New List:")
        printList(matrix)
    else:
        print("Error occurred.")
        print("Data type is not a matrix or list!\n")
        return None

def setTopRow(matrix, value):
    print("\nsetTopRow(): Sets all elements in the first row to the same value")

    if isinstance(matrix[0],list): # * Is a matrix
        
        if not isinstance(value, float) and not isinstance(value, int):
            print("Error occurred.")
            print("Input value is not numeric! Please enter a valid value!")
            return None
        
        print(f"Setting top row to value: {value}")
        
        for column in range(len(matrix[0])):
            matrix[0][column] = value

        print("New matrix:")
        print2DMatrix(matrix)

    elif isinstance(matrix, list): # * Is a list
        if not isinstance(value, float) and not isinstance(value, int):
            print("Error occurred.")
            print("Input value is not numeric! Please enter a valid value!")
            return None
        
        print(f"Setting top row to value: {value}")

        for _ in range(len(matrix)):
            matrix[_] = value

        print("New List:")
        printList(matrix)
    else:
        print("Error occurred.")
        print("Data type is not a matrix or list!\n")
        return None


def setDiagonal(matrix, value): # Assumes matrix is square!
    print("\nsetDiagonal(): Sets all elements along the main diagonal to the same value. Assumes matrix is a square")
    if len(matrix) != len(matrix[0]):
        print("Error occurred.")
        print("Matrix is not square! setDiagonal(matrix, value) will not work! Exiting...")
        return None

    if not isinstance(value, float) and not isinstance(value, int):
        print("Error occurred.")
        print("Input value is not numeric! Please enter a valid value!")
        return None
    
    print(f"Setting diagonal to value: {value}")
    for index in range(len(matrix)):
        matrix[index][index] = value

    print("New matrix:")
    print2DMatrix(matrix)

def getRows(matrix):
    print("\nrowsIn(): Counts the number of rows in list or matrix")
    if isinstance(matrix[0],list):
        print(f"Matrix has {len(matrix[0])} rows.\n")
        return (len(matrix[0]))
    
    elif isinstance(matrix, list):
        print(f"List has 1 row.\n")
        return 1
    
    else:
        print("Error occurred.")
        print("Data type is not a matrix or list!\n")
        return None

def getColumns(matrix):
    print("\ncolumnsIn(): Counts the number of columns in list or matrix")
    if isinstance(matrix[0],list):
        print(f"Matrix has {len(matrix[0])} columns.\n")
        return (len(matrix[0]))
        
    elif isinstance(matrix, list):
        print(f"List has {len(matrix)} columns.\n")
        return (len(matrix))
    
    else:
        print("Error occurred.")
        print("Data type is not a matrix or list!\n")
        return None
    
def getMax(matrix, returnRow = 0, returnColumn = 0):
    print("\ngetMax(): Returns the maximum element in matrix or list. Set returnRow = 1 to return the row index of maximum and or set returnColumn = 1 to return the column index of maximum")
    print("Returns max element, max element's row, max element's column in a tuple format. If only element is required, no tuple is returned. The element itself is returned.")
    requiredResult = str(returnRow) + str(returnColumn)

    if isinstance(matrix[0],list): # * Is a matrix
            
            maxValue = matrix[0][0]
            maxRow = 0
            maxCol = 0
            
            
            for row in range(len(matrix)):
                for col in range(len(matrix[row])):
                    if matrix[row][col] > maxValue:
                        maxValue = matrix[row][col]
                        maxRow = row
                        maxCol = col
            
            print(f"Maximum of matrix is : {maxValue}.\n")

            match requiredResult:
                case "11":
                    return (maxValue, maxRow, maxCol)

                case "10":
                    return (maxValue, maxRow)

                case "01":
                    return (maxValue, maxCol)
                case "00":
                    return maxValue
                case _:
                    print("Error occurred.")
                    print("Please enter integers for parameters returnRowIndex and returnColumnIndex, setting a 1 for either or both or whichever is required.\n")
                    return None
    
    elif isinstance(matrix, list): # * Is a list

        maxValue = 0
        maxCol = 0
        for col in range(matrix):
            if matrix[col] > maxValue:
                maxValue = col
                maxCol = col

        print(f"Maximum of list is : {maxValue}.\n")

        match requiredResult:
            case "11":
                return (maxValue, 1, maxCol)

            case "10":
                return (maxValue, 1)

            case "01":
                return (maxValue, maxCol)
            case "00":
                return maxValue
            case _:
                print("Error occurred.")
                print("Please enter integers for parameters returnRowIndex and returnColumnIndex, setting a 1 for either or both or whichever is required.\n")
                return None
    
    else:
        print("Error occurred.")
        print("Data type is not a matrix or list!\n")
        return None
    
def getMin(matrix, returnRow = 0, returnColumn = 0):
    print("\ngetMin(): Returns the minimum element in matrix or list. Set returnRow = 1 to return the row index of maximum and or set returnColumn = 1 to return the column index of maximum")
    print("Returns min element, min element's row, min element's column in a tuple format. If only element is required, no tuple is returned. The element itself is returned.")
    requiredResult = str(returnRow) + str(returnColumn)

    if isinstance(matrix[0],list): # * Is a matrix
            
            minValue = matrix[0][0]
            minRow = 0
            minCol = 0
            
            
            for row in range(len(matrix)):
                for col in range(len(matrix[row])):
                    if matrix[row][col] < minValue:
                        minValue = matrix[row][col]
                        minRow = row
                        minCol = col
            
            print(f"Maximum of matrix is : {minValue}.\n")

            match requiredResult:
                case "11":
                    return (minValue, minRow, minCol)

                case "10":
                    return (minValue, minRow)

                case "01":
                    return (minValue, minCol)
                
                case "00":
                    return minValue
                
                case _:
                    print("Error occurred.")
                    print("Please enter integers for parameters returnRowIndex and returnColumnIndex, setting a 1 for either or both or whichever is required.\n")
                    return None
    
    elif isinstance(matrix, list): # * Is a list

        minValue = 0
        minCol = 0
        for col in range(matrix):
            if matrix[col] < minValue:
                minValue = col
                minCol = col

        print(f"Maximum of list is : {minValue}.\n")

        match requiredResult:
            case "11":
                return (minValue, 1, minCol)

            case "10":
                return (minValue, 1)

            case "01":
                return (minValue, minCol)
            
            case "00":
                return minValue
            
            case _:
                print("Error occurred.")
                print("Please enter integers for parameters returnRowIndex and returnColumnIndex, setting a 1 for either or both or whichever is required.\n")
                return None
    
    else:
        print("Error occurred.")
        print("Data type is not a matrix or list!\n")
        return None
    

def createListRandom(dataType, size, startingNumberInclusive = 0, endingNumberInclusive = 0, stringLength = 0, seed = 0):
    
    print("\ncreateListRandom(): Creates a random list. Some of the parameters are required; some are not. It will return error(s) if required parameter(s) are absent.")

    try:
        size = int(size)
        if size <= 0:
            print("Error occurred.")
            print("Please enter a positive integer for your size parameter!")
            return None

    except ValueError:
        print("Error occurred.")
        print("Please enter an integer for your size parameter! It should be > 0 as well.")
        return None
    
    import random
    random.seed(seed)

    match dataType:

        case "str":

            import string

            lettersDigits = string.ascii_letters + string.digits

            if stringLength == 0:
                print("Error occurred.")
                print("Please enter a valid string length!")
                return None
            
            return [''.join(random.choice(lettersDigits) for _ in range(stringLength)) for _ in range(size)]
            

        case "int":
            try:
                startingNumberInclusive = int(startingNumberInclusive)

            except ValueError:
                print("Error occurred.")
                print("Please enter an integer for your starting number. Ensure that the ending number (inclusive) should be >= starting number (inclusive)!")
                return None
            
            try:
                endingNumberInclusive = int(endingNumberInclusive)

            except ValueError:
                print("Error occurred.")
                print("Please enter an integer for your ending number. Ensure that the ending number (inclusive) should be >= starting number (inclusive)!")
                return None
    

            if startingNumberInclusive > endingNumberInclusive:
                print("Error occurred.")
                print("Please ensure that the ending number (inclusive) should be >= starting number (inclusive)!")
                return None
            
            return [random.randrange(startingNumberInclusive, endingNumberInclusive) for _ in range(size)]
        
        case "float":
            try:
                startingNumberInclusive = int(startingNumberInclusive)

            except ValueError:
                print("Error occurred.")
                print("Please enter an integer for your starting number. Ensure that the ending number (inclusive) should be >= starting number (inclusive)!")
                return None
            
            try:
                endingNumberInclusive = int(endingNumberInclusive)

            except ValueError:
                print("Error occurred.")
                print("Please enter an integer for your ending number. Ensure that the ending number (inclusive) should be >= starting number (inclusive)!")
                return None
    

            if startingNumberInclusive > endingNumberInclusive:
                print("Error occurred.")
                print("Please ensure that the ending number (inclusive) should be >= starting number (inclusive)!")
                return None
            
            return [random.uniform(startingNumberInclusive, endingNumberInclusive) for _ in range(size)]
        
        case _:
            print("Please enter a valid parameter type for dataType for createListRandom()!. It should either be 'int', 'float' or 'str'!")
            return None

def create2DMatrixRandom(dataType, rows = 1, columns = 1,startingNumberInclusive = 0, endingNumberInclusive = 10, stringLength = 0, seed = 0):

    print("\ncreate2DMatrixRandom(): Creates a random matrix. Some of the parameters are required; some are not. It will return error(s) if required parameter(s) are absent.")

    try:
        rows = int(rows)
        if rows <= 0:
            print("Error occurred.")
            print("Please enter a positive number for the number of rows!")
            return None

    except ValueError:
        print("Error occurred.")
        print("Please enter an integer for the number of rows. Ensure that the ending number (inclusive) should be >= starting number (inclusive)!")
        return None

    try:
        columns = int(columns)
        if columns <= 0:
            print("Error occurred.")
            print("Please enter a positive number for the number of columns!")
            return None

    except ValueError:
        print("Error occurred.")
        print("Please enter a positive integer for the number of columns!")
        return None

    import random
    random.seed(seed)

    if dataType == "str":

        import string

        if stringLength == 0:
                print("Error occurred.")
                print("Please enter a valid string length!")
                return None
        lettersDigits = string.ascii_letters + string.digits

        return [[''.join(random.choice(lettersDigits) for _ in range(stringLength)) for _ in range(columns)] for _ in range(rows)]
            

    if dataType == "int":

        try:
            startingNumberInclusive = int(startingNumberInclusive)

        except ValueError:
            print("Error occurred.")
            print("Please enter an integer for your starting number. Ensure that the ending number (inclusive) should be >= starting number (inclusive)!")
            return None
        
        try:
            endingNumberInclusive = int(endingNumberInclusive)

        except ValueError:
            print("Error occurred.")
            print("Please enter an integer for your ending number. Ensure that the ending number (inclusive) should be >= starting number (inclusive)!")
            return None


        if startingNumberInclusive > endingNumberInclusive:
            print("Error occurred.")
            print("Please ensure that the ending number (inclusive) should be >= starting number (inclusive)!")
            return None
            
 
        return [[random.randrange(startingNumberInclusive, endingNumberInclusive) for _ in range(columns)] for _ in range(rows)]
        
    

    if dataType == "float":
        
        try:
            startingNumberInclusive = int(startingNumberInclusive)

        except ValueError:
            print("Error occurred.")
            print("Please enter an integer for your starting number. Ensure that the ending number (inclusive) should be >= starting number (inclusive)!")
            return None
        
        try:
            endingNumberInclusive = int(endingNumberInclusive)

        except ValueError:
            print("Error occurred.")
            print("Please enter an integer for your ending number. Ensure that the ending number (inclusive) should be >= starting number (inclusive)!")
            return None


        if startingNumberInclusive > endingNumberInclusive:
            print("Error occurred.")
            print("Please ensure that the ending number (inclusive) should be >= starting number (inclusive)!")
            return None
            
        return [[random.uniform(startingNumberInclusive, endingNumberInclusive) for _ in range(columns)] for _ in range(rows)]

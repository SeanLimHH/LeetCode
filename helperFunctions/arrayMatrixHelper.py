def createList(size, initialisedValue = 0, info = 0):
    if info:
        print('\ncreateList()')
        printList([initialisedValue for _ in range(size)])
    return [initialisedValue for _ in range(size)]

def getDimensions(list_, info = 0): #* Returns False if it is not a list or matrix
    #* Assumes that element has at least 1 element for each dimension
    
    a = list_
    count = 0
    while isinstance(a,list):
        a = a[0]
        count += 1
        
    if info:
        print('\ngetDimensions()')
        match count:
            case 0:
                print(f"{list_} is not a list or matrix!")
                print(f"{list_} data type is of {type(list_)}.")
                
            case 1:
                print(f"{list_} is a list!")
                
            case _:
                print(f"{list_} is a {count}-dimensional matrix!")
                
        print(f"Number of dimensions of input is {count}.")
    return count
        


def printList(list_):
    print("\nprintList()")

    if getDimensions(list_) != 1:
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
        try:
            print(f"{element:<{2*maxLengthForFormatting}}", end="")
        except TypeError:
            print('Error occured.')
            print('Data type of list unsuitable to be printed in this function.')
            return None
    print("\n")

def create2DMatrix(rows, columns, initialisedValue = 0, info = 0):
    if info:
        print('\ncreate2DMatrix()')
        print2DMatrix([[initialisedValue for _ in range(columns)] for _ in range(rows)])
    return [[initialisedValue for _ in range(columns)] for _ in range(rows)]

def print2DMatrix(matrix):
    print("\nprint2DMatrix()")

    if getDimensions(matrix) != 2:
        print("Error occurred.")
        print("The input for print2DMatrix() is not a matrix! Please input the correct data structure!")
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

def getEntry(matrix, rowIndex, columnIndex, info = 0):
    if info:
        print("\ngetEntry()")
        print(f"Returns the entry in the matrix at row {rowIndex} and column {columnIndex}.")
    
    if getDimensions(matrix) != 2:
        print("Error occurred.")
        print("The input for getEntry() is not a matrix! Please input the correct data structure!")
        return None
    
    if info:
        print(f"Value of cell: row index {rowIndex} column index {columnIndex} is :", matrix[rowIndex][columnIndex])
    return matrix[rowIndex][columnIndex]

def setEntry(matrix, rowIndex, columnIndex, newValue, info = 0):
    if info:
        print("\nsetEntry()")
        print("Updates entry of matrix. It is simply matrix[rowIndex][columnIndex] = value")
    
    if getDimensions(matrix) != 2:
        print("Error occurred.")
        print("The input for setEntry() is not a matrix! Please input the correct data structure!")
        return None
    
    try:
        rowIndex = int(rowIndex)
        columnIndex = int(columnIndex)

        if rowIndex >= len(matrix):
            print("Error occurred.")
            print("Row index is larger than number of rows! Please enter a valid row index!")
            return None
        
        if columnIndex >= len(matrix):
            print("Error occurred.")
            print("Column index is larger than number of columns! Please enter a valid column index!")
            return None
        
    except ValueError:
        print("Please enter a valid integer >= 0 for row index and column index!")
        return None
    
    if info:
        print(f"Value of cell to be updated: row index {rowIndex} column index {columnIndex}")
        print(f"Current value is: {matrix[rowIndex][columnIndex]}")
        print(f"New value to be updated in cell [{rowIndex}][{columnIndex}]: {newValue}")
    matrix[rowIndex][columnIndex] = newValue
    return matrix

def setLeftColumn(matrix, value, info = 0):
    if info:
        print("\nsetLeftColumn()")
        print("Sets all elements in the first column to the same value")
    
    if getDimensions(matrix) != 1 and getDimensions(matrix) != 2:
        print("Error occurred.")
        print("The input for setLeftColumn() is not a list or matrix! Please input the correct data structure!")
        return None
    
    if getDimensions(matrix) == 2:
        
        if not isinstance(value, float) and not isinstance(value, int):
            print("Error occurred.")
            print("Input value is not numeric! Please enter a valid value!")
            return None
        
        if info:
            print(f"Setting left column to value: {value}")
        
        for row in range(len(matrix)):
            matrix[row][0] = value

        if info:
            print("New matrix:")
            print2DMatrix(matrix)

    
    if getDimensions(matrix) == 1:
    
        if not isinstance(value, float) and not isinstance(value, int):
            print("Error occurred.")
            print("Input value is not numeric! Please enter a valid value!")
            return None
        if info:
            print(f"Setting left column to value: {value}")
        
        matrix[0] = value

        if info:
            print("New List:")
            printList(matrix)

def setTopRow(matrix, value, info = 0):
    if info:
        print("\nsetTopRow()")
        print("Sets all elements in the first row to the same value")
    
    if getDimensions(matrix) != 1 and getDimensions(matrix) != 2:
        print("Error occurred.")
        print("The input for setTopRow() is not a list or matrix! Please input the correct data structure!")
        return None
    
    if getDimensions(matrix) == 2:
        
        if not isinstance(value, float) and not isinstance(value, int):
            print("Error occurred.")
            print("Input value is not numeric! Please enter a valid value!")
            return None
        
        if info:
            print(f"Setting the top row to value: {value}")
        
        for column in range(len(matrix[0])):
            matrix[0][column] = value

        if info:
            print("New matrix:")
            print2DMatrix(matrix)

    
    if getDimensions(matrix) == 1:
    
        if not isinstance(value, float) and not isinstance(value, int):
            print("Error occurred.")
            print("Input value is not numeric! Please enter a valid value!")
            return None
        
        if info:
            print(f"Setting the top row to value: {value}")
        
        matrix[0] = value
        
        if info:
            print("New List:")
            printList(matrix)

def setDiagonal(matrix, value, info = 0): # Assumes matrix is square!
    if info: 
        print("\nsetDiagonal()")
        print("Sets all elements along the main diagonal to the same value. Assumes matrix is a square")
    
    if getDimensions(matrix) != 2:
        print("Error occurred.")
        print("The input for setDiagonal() is not a matrix! Please input the correct data structure!")
        return None
    
    if len(matrix) != len(matrix[0]):
        print("Error occurred.")
        print("Matrix is not square! setDiagonal(matrix, value) will not work! Exiting...")
        return None

    if not isinstance(value, float) and not isinstance(value, int):
        print("Error occurred.")
        print("Input value is not numeric! Please enter a valid value!")
        return None
    
    if info:
        print(f"Setting diagonal to value: {value}")

    for index in range(len(matrix)):
        matrix[index][index] = value

    if info:
        print("New matrix:")
        print2DMatrix(matrix)

def getRows(matrix, info = 0):
    if info:
        print("\ngetRows()")
        print("Counts the number of rows in list or matrix")
            
    if getDimensions(matrix) == 2:
        print(f"Matrix has {len(matrix[0])} rows.\n")
        return (len(matrix[0]))
    
    if getDimensions(matrix) == 1:
        print(f"List has 1 row.\n")
        return 1
    
    print("Error occurred.")
    print("Data type is not a matrix or list!\n")
    return None

def getColumns(matrix, info = 0):
    if info:
        print("\ngetColumns()")
        print("Counts the number of columns in list or matrix")
            
    if getDimensions(matrix) == 2:
        print(f"Matrix has {len(matrix[0])} columns.\n")
        return (len(matrix[0]))
    
    if getDimensions(matrix) == 1:
        print(f"List has {len(matrix)} columns.\n")
        return len(matrix)
    
    print("Error occurred.")
    print("Data type is not a matrix or list!\n")
    return None
    
def getMax(matrix, returnRow = 0, returnColumn = 0, info = 0):
    if info:
        print("\ngetMax()")
        print("Set returnRow = 1 to return the row index of maximum and or set returnColumn = 1 to return the column index of maximum")
        print("Returns max element, max element's row, max element's column in a tuple format. If only element is required, no tuple is returned. The element itself is returned.")
    requiredResult = str(returnRow) + str(returnColumn)

    if getDimensions(matrix) == 2: # * Is a matrix
            
            maxValue = matrix[0][0]
            maxRow = 0
            maxCol = 0
            
            
            for row in range(len(matrix)):
                for col in range(len(matrix[row])):
                    if matrix[row][col] > maxValue:
                        maxValue = matrix[row][col]
                        maxRow = row
                        maxCol = col
            if info:
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
    
    elif getDimensions(matrix) == 1: # * Is a list

        maxValue = 0
        maxCol = 0
        for col in range(matrix):
            if matrix[col] > maxValue:
                maxValue = col
                maxCol = col
        if info:
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
    
def getMin(matrix, returnRow = 0, returnColumn = 0, info = 0):
    if info:
        print("\ngetMin()")
        print("Set returnRow = 1 to return the row index of minimum and or set returnColumn = 1 to return the column index of minimum")
        print("Returns min element, min element's row, min element's column in a tuple format. If only element is required, no tuple is returned. The element itself is returned.")
    requiredResult = str(returnRow) + str(returnColumn)

    if getDimensions(matrix) == 2: #* Is a matrix
            
            minValue = matrix[0][0]
            minRow = 0
            minCol = 0
            
            
            for row in range(len(matrix)):
                for col in range(len(matrix[row])):
                    if matrix[row][col] < minValue:
                        minValue = matrix[row][col]
                        minRow = row
                        minCol = col
            if info:
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
    
    elif getDimensions(matrix) == 1: #* Is a list

        minValue = 0
        minCol = 0
        for col in range(matrix):
            if matrix[col] < minValue:
                minValue = col
                minCol = col
        if info:
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
    

def createListRandom(dataType, size, startingNumberInclusive = 0, endingNumberInclusive = 0, stringLength = 0, seed = 0, info = 0):
    if info:
        print("\ncreateListRandom()")
        print("Creates a random list. Some of the parameters are required; some are not. It will return error(s) if required parameter(s) are absent.")

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
            
            if info:
                print("Created list:")
                _ = [''.join(random.choice(lettersDigits) for _ in range(stringLength)) for _ in range(size)]
                printList(_)
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
            
            if info:
                print("Created list:")
                _ = [random.randrange(startingNumberInclusive, endingNumberInclusive) for _ in range(size)]
                printList(_)
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
            
            if info:
                print("Created list:")
                _ = [random.uniform(startingNumberInclusive, endingNumberInclusive) for _ in range(size)]
                printList(_)
            return [random.uniform(startingNumberInclusive, endingNumberInclusive) for _ in range(size)]
        
        case _:
            print("Please enter a valid parameter type for dataType for createListRandom()!. It should either be 'int', 'float' or 'str'!")
            return None

def create2DMatrixRandom(dataType, rows = 1, columns = 1,startingNumberInclusive = 0, endingNumberInclusive = 10, stringLength = 0, seed = 0, info = 0):
    if info:
        print("\ncreate2DMatrixRandom()")
        print("Creates a random matrix. Some of the parameters are required; some are not. It will return error(s) if required parameter(s) are absent.")

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

        if info:
            _ = [[''.join(random.choice(lettersDigits) for _ in range(stringLength)) for _ in range(columns)] for _ in range(rows)]
            print2DMatrix(_)
            
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

        if info:
            _ = [[random.randrange(startingNumberInclusive, endingNumberInclusive) for _ in range(columns)] for _ in range(rows)]
            print2DMatrix(_)
 
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
        
        if info:
            _ = [[random.uniform(startingNumberInclusive, endingNumberInclusive) for _ in range(columns)] for _ in range(rows)]
            print2DMatrix(_)

        return [[random.uniform(startingNumberInclusive, endingNumberInclusive) for _ in range(columns)] for _ in range(rows)]

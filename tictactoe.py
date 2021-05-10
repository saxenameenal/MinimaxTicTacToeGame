import sys

boards = sys.argv[1]
file = sys.argv[2]

linear_matrix = []
for i in range(len(boards)):
    linear_matrix.append(boards[i])

# print(linear_matrix)
matrix = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"],
]

# storing input as 2D array 
count = 0
for i in range(0,3):
    for j in range(0,3):
        matrix[i][j] = linear_matrix[count]
        count +=1

#function to check if board has any empty state 
def EmptyBoard(matrix):
    for i in range(0,3):
        for j in range(0,3):
            if (matrix[i][j] == "-"):
                return True
    return False

#function to check vertical, horizontal, and diagonal states (check if game is terminal or not)
def util(matrix):
    
    #checking vertically
    for c in range(0,3):
        if(matrix[0][c] ==  matrix[1][c] == matrix[2][c]):
            if(matrix[2][c] == "o"):
                return -1
            if(matrix[2][c] == "x"):
                return 1

    #checking horizontally
    for r in range(0,3):
        if(matrix[r][0] == matrix[r][1] == matrix[r][2]):
            if(matrix[r][2] == "o"):
                return -1
            if(matrix[r][2] == "x"):
                return 1

    #checking diagonally
    if(matrix[0][0] == matrix[1][1] == matrix[2][2]):
        if(matrix[2][2] == "o"):
            return -1
        if(matrix[2][2] == "x"):
            return 1 

    if(matrix[0][2] == matrix[1][1] == matrix[2][0]):
        if(matrix[2][0] == "o"):
            return -1
        if(matrix[2][0] == "x"):
            return 1  

    else:
        return 0

#who's turn it is (x/o)
def turn(matrix):
    countX = 0
    countO = 0 
    noValue = 0
    empty = EmptyBoard(matrix)

    #if all states are empty (empty board)
    for i in range(0,3):
        for j in range(0,3):
            if (matrix[i][j] == '-'):
                noValue += 1

    #iterating through matrix to count number of turns 
    for i in range(0,3):
        for j in range(0,3):
            if(matrix[i][j] == "x"):
                countX +=1
            if(matrix[i][j] == "o"):
                countO +=1
    
    if(countX > countO):
        return "o"
    if(countX == countO):
        return "x"
    else:
        return "x"

name = " "

def PrintToFile(matrix, value):
    f = open(name,"a")
    string = ""
    for i in range(0,3):
        for j in range(0,3):
            string = string + matrix[i][j]
    
    #so concatentate the matrix and the value
    #Then print it out as following
    f.write(string+ " " + str(value) + "\n")
    f.close()

name = file

def minimaxFin(matrix):
    
    utility = util(matrix)
    empty = EmptyBoard(matrix)
    move = turn(matrix)

    xValue = -100
    oValue = 100

    #checking if x or o has already won the game
    if(utility == -1 or utility == 1):    
        return utility
    
    # checking if board is already filled up (no empty states left)
    if(empty == False):   
        return 0   

    if(move == "x"):
        num = xValue
        for i in range(0,3):
            for j in range(0,3): 
                if(matrix[i][j] == "-"):  

                    move = turn(matrix) 

                    matrix[i][j] = "x"

                    state = minimaxFin(matrix)
                    PrintToFile(matrix, state)

                    #selecting max value out of all possible values that function will recursively iterate through   
                    num = max(num, state) 
                    #num = minimax value
                    
                    
                    matrix[i][j] = "-"
        return num

    elif (move == "o"): 
        num = oValue 
        for i in range(0,3):
            for j in range(0,3): 
                if(matrix[i][j] == "-"):  

                    move = turn(matrix) 
                                     
                    matrix[i][j] = "o"

                    state = minimaxFin(matrix)
                    PrintToFile(matrix, state)
                  
                    #selecting max value out of all possible values that function will recursively iterate through   
                    minValue = min(num, state) 
                    num = minValue
                    
                    matrix[i][j] = "-"
        return num

def printTerminal(matrix):
    string = ""
    for i in range(0,3):
        for j in range(0,3):
            string = string + matrix[i][j]
    return (string)

def optimalState(matrix):

    neg = -100  
    pos = 100

    for i in range(0,3):
        for j in range(0,3):
            if(matrix[i][j] == "-"): 
                
                move = turn(matrix)

                if(move == "x"):

                    matrix[i][j] == "x"                  

                    state = minimaxFin(matrix) 
                    PrintToFile(matrix, state)
                   
                    matrix[i][j] = "-"

                    if(neg < state):      
                        iVal = (i)  
                        jVal = (j)
                        neg = state
                        
                elif(move == "o"):
                    
                    matrix[i][j] = "o"
                    
                    state = minimaxFin(matrix) 
                    PrintToFile(matrix, state)

                    matrix[i][j] = "-"

                    if(pos > state):    
                        iVal = (i)  
                        jVal = (j)
                        pos = state

    move = turn(matrix)

    if(move == "o"):
        matrix[iVal][jVal] = "o"
        print(printTerminal(matrix))

    elif(move == "x"):
        matrix[iVal][jVal] = "x"
        print(printTerminal(matrix))

#calling normal minimax function 
if((len(sys.argv)) == 3 ):
    optimalState(matrix)

def minimax_AlphBet(matrix, a, b, xo):
    
    utility = util(matrix)
    empty = EmptyBoard(matrix)

    xValue = -100
    oValue = 100  

    # checking if x or o has already won the game
    if((utility == -1) or (utility == 1)):    
        return utility
    
    # checking if board is already filled up (no empty states left)
    if(empty == False):   
        return 0   

    if(xo):
        num = xValue 
        for i in range(0,3):
            for j in range(0,3): 
                if(matrix[i][j] == "-"):  
                    matrix[i][j] = "x"
                    state = minimax_AlphBet(matrix, a, b, False)
                    #selecting max value out of all possible values that function will recursively iterate through   
                    num = max(num, state) 
                    a = max(state,a) 

                    if(b <= a):
                        PrintToFile(matrix, state)
                        matrix[i][j] = "-"
                        return num 

                    PrintToFile(matrix, state)
                    matrix[i][j] = "-"        
        return num

    elif(not xo):
        num = oValue 
        for i in range(0,3):
            for j in range(0,3): 
                if(matrix[i][j] == "-"):  
                                       
                    matrix[i][j] = "o"
                    state = minimax_AlphBet(matrix, a , b, True)
                    #selecting max value out of all possible values that function will recursively iterate through   
                    num = min(num, state) 
                    b = min(state,b)

                    if(b <= a):
                        PrintToFile(matrix, state)
                        matrix[i][j] = "-"
                        return num

                    PrintToFile(matrix, state)
                    matrix[i][j] = "-"
        return num

def optimalState_AlphBet(matrix, xTurn):
    neg, a, pos, b, jVal, iVal = -100, -100, 100, 100, 0, 0 

    for i in range(0,3):
        for j in range(0,3):
            if(matrix[i][j] == "-"): 
                if(xTurn):
                    matrix[i][j] == "x"      
                    state = minimax_AlphBet(matrix, a, b, False)
                    PrintToFile(matrix, state)
                    matrix[i][j] = "-"
                    a = max(a, state)
                    
                    if(neg < state):      
                        iVal = (i)  
                        jVal = (j)
                        neg = state

                else:
                    matrix[i][j] = "o"
                    state = minimax_AlphBet(matrix, a, b, True)
                    PrintToFile(matrix, state)
                    matrix[i][j] = "-"
                    b = min(b, state)
                    
                    if(pos > state):   
                        iVal = (i)  
                        jVal = (j)
                        pos = state

    move = turn(matrix)
    if(move == "o"):
        matrix[iVal][jVal] = "o"
        print(printTerminal(matrix))

    elif(move == "x"):
        matrix[iVal][jVal] = "x"
        print(printTerminal(matrix))

#calling pruning minimax function, implemented with alpha and beta 
if((len(sys.argv)) == 4 ):
    move = turn(matrix)
    if(move == "x"):
        optimalState_AlphBet(matrix, True)
    elif(move =="o"):
        optimalState_AlphBet(matrix, False)

def Es(matrix):

    winsX = 0 

    x = [
        ["-","-","-"],
        ["-","-","-"],
        ["-","-","-"],
    ]

    for i in range(0,3):
        for j in range(0,3):
            x[i][j] = matrix[i][j]

    for i in range(0,3):
        for j in range(0,3):
            if(x[i][j] == "-"):
                x[i][j] = "x"

    for c in range(0,3):
        if(x[0][c] ==  x[1][c] == x[2][c]):
            if(x[2][c] == "x"):
                winsX += 1

    #checking horizontally
    for r in range(0,3):
        if(x[r][0] == x[r][1] == x[r][2]):
            if(x[r][2] == "x"):
                winsX += 1

    #checking diagonally
    if(x[0][0] == x[1][1] == x[2][2]):
        if(x[2][2] == "x"):
            winsX += 1

    if(x[0][2] == x[1][1] == x[2][0]):
        if(x[2][0] == "x"):
            winsX += 1
    
    winsY = 0 

    y = [
        ["-","-","-"],
        ["-","-","-"],
        ["-","-","-"],
    ]

    for i in range(0,3):
        for j in range(0,3):
            y[i][j] = matrix[i][j]

    for i in range(0,3):
        for j in range(0,3):
            if(y[i][j] == "-"):
                y[i][j] = "o"

    for c in range(0,3):
        if(y[0][c] ==  y[1][c] == y[2][c]):
            if(y[2][c] == "o"):
                winsY += 1

    #checking horizontally
    for r in range(0,3):
        if(y[r][0] == y[r][1] == y[r][2]):
            if(y[r][2] == "o"):
                winsY += 1

    #checking diagonally
    if(y[0][0] == y[1][1] == y[2][2]):
        if(y[2][2] == "o"):
            winsY += 1

    if(y[0][2] == y[1][1] == y[2][0]):
        if(y[2][0] == "o"):
            winsY += 1

    final = winsX - winsY
    return final 

def minimax_ply(matrix, a, b, d):
    
    utility = util(matrix)
    empty = EmptyBoard(matrix)
    move = turn(matrix)

    xValue, oValue = -100, 100  

    #checking if x or o has already won the game
    if(utility == -1 or utility == 1):    
        return Es(matrix)
    
    # checking if board is already filled up (no empty states left)
    if(empty == False):   
        return Es(matrix)   

    d = int(d)
    d = d - 1

    if(d == 0 ):
        return Es(matrix)

    if(move == "x"):
        num = xValue
        # a = 10
        for i in range(0,3):
            for j in range(0,3): 
                if(matrix[i][j] == "-"):  

                    move = turn(matrix) 
                    matrix[i][j] = "x"

                    state = minimax_ply(matrix, a, b, d)

                    #selecting max value out of all possible values that function will recursively iterate through   
                    maxValue = max(num, state) 
                    num = maxValue  

                    # aValue = max(num, a)
                    aValue = max(state,a)
                    a = aValue

                    if (a >= b):
                        PrintToFile(matrix, state)
                        matrix[i][j] = "-"
                        return num
                                    
                    PrintToFile(matrix, state)
                    matrix[i][j] = "-"
        return num

    elif (move == "o"): 
        num = oValue 
        for i in range(0,3):
            for j in range(0,3): 
                if(matrix[i][j] == "-"):  

                    move = turn(matrix) 
                    matrix[i][j] = "o"

                    state = minimax_ply(matrix, a, b, d)
                  
                    #selecting max value out of all possible values that function will recursively iterate through   
                    minValue = min(num, state) 
                    num = minValue

                    # bValue = min(num, b)
                    bValue = min(state,b)
                    b = bValue

                    if(a >= b):
                        PrintToFile(matrix, state)
                        matrix[i][j] = "-"
                        return num 
                    
                    PrintToFile(matrix, state)
                    matrix[i][j] = "-"
        return num

def optimalState_ply(matrix, d):
    neg, a, pos, b, jVal, iVal = -100, -100, 100, 100, 0, 0 

    for i in range(0,3):
        for j in range(0,3):
            if(matrix[i][j] == "-"): 

                move = turn(matrix)

                if(move == "x"):
                    
                    matrix[i][j] == "x"      

                    state = minimax_ply(matrix, a, b, d)

                    if(neg < state):      
                        iVal = (i)  
                        jVal = (j)
                        neg = state
                    
                    aValue= max(a, state)
                    a = aValue

                    PrintToFile(matrix, state)
                    matrix[i][j] = "-"

                elif(move == "o"):
    
                    matrix[i][j] = "o"
                    state = minimax_ply(matrix, a, b, d)

                    if(pos > state):   
                        iVal = (i)  
                        jVal = (j)
                        pos = state

                    bValue = min(b, state)
                    b = bValue

                    PrintToFile(matrix, state)
                    matrix[i][j] = "-"

    move = turn(matrix)

    if(move == "o"):
        matrix[iVal][jVal] = "o"
        print(printTerminal(matrix))

    elif(move == "x"):
        matrix[iVal][jVal] = "x"
        print(printTerminal(matrix))

#calling pruning minimax function with Early Termination 
if((len(sys.argv)) == 5 ):
    d = sys.argv[4]
    optimalState_ply(matrix, d)
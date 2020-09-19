def display():
    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            print(arr[i][j], end=" ")
        print()
def position_input():
    flag = False
    while flag == False:
        s = input("Enter X or O: ").upper()
        if (s == "X") or (s == "O"):
            flag = True
        else:
            print("Enter either X or O")
    flag = False
    while flag == False:
        x, y = map(int, input("Enter row and column number: ").split())
        if (x in range(1, 4)) and (y in range(1, 4)):
            flag = True
            x -= 1
            y -= 1
        else:
            print("Enter a valid position between 1 and 3")
    return s, x, y

def replace(arr, return_list):
    arr[return_list[1]][return_list[2]] = return_list[0]
    return arr
    
def game_on():
    choice = ""
    while True:
        choice = input("Do you want to continue? [Y or N]: ")
        if (choice == "Y") or (choice == "y"):
            return True
        elif (choice == "N") or (choice == "n"):
            return False
        else:
            print("Enter a valid choice")
            
def logic(arr):
    diag_1 = []
    diag_2 = []
    for i in range(0, 3, 1):
        temp_row = []
        for j in range(0, 3, 1):
            temp_row.append(arr[i][j])
            #print(arr[i][j], end = " ")
            if i == j:
                diag_1.append(arr[i][j])
        #print(temp_row)
        temp_row = list(set(temp_row))
        if ("_" not in temp_row) and (len(temp_row) == 1):
            print("WINNER")
            return True
            
    for i in range(0, 3, 1):
        temp_col = []
        for j in range(0, 3, 1):
            temp_col.append(arr[j][i])
            #print(arr[j][i], end = " ")
            if ((i + j) == (len(arr) - 1)):
                diag_2.append(arr[i][j])
        #print(temp_col)
        temp_col = list(set(temp_col))
        if ("_" not in temp_col) and (len(temp_col) == 1):
            print("WINNER")
            return True
                    
    diag_1 = list(set(diag_1))
    if ("_" not in diag_1) and (len(diag_1) == 1):
        print("WINNER")
        return True
        
    diag_2 = list(set(diag_2))
    if ("_" not in diag_2) and (len(diag_2) == 1):
        print("WINNER")
        return True
    return False
        
    
            
            

#driver code
flag = True
res = False

while (flag == True):
    arr = [["_" for i in range(0, 3, 1)] for k in range(0, 3, 1)]

    while logic(arr) == False:
        display()
        return_list = list(map(str, position_input()))
        return_list[1] = int(return_list[1])
        return_list[2] = int(return_list[2])
        #print(return_list)    
        arr = replace(arr, return_list)
        display()
    flag = game_on()



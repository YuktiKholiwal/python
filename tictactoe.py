tictactoe=["_","_","_","_","_","_","_","_","_"]

game_still_going=True

winner=None
current_player ="X"

def display():
    print(tictactoe[0]+" | "+tictactoe[1]+" | "+tictactoe[2])
    print(tictactoe[3]+" | "+tictactoe[4]+" | "+tictactoe[5])
    print(tictactoe[6]+" | "+tictactoe[7]+" | "+tictactoe[8])

#tictactoe[0]->1
#tictactoe[1]->2
#tictactoe[2]->3
#tictactoe[3]->4
#tictactoe[4]->5
#tictactoe[5]->6
#tictactoe[6]->7
#tictactoe[7]->8
#tictactoe[8]->9

def play():

    #display initial board first
    display()
    while game_still_going:
        turn(current_player)

        check_if_game_over()

        flip_player()

    if winner == "X" or winner == "0":
        print(winner + " won")
    elif winner == None:
        print("tie")


def turn(player):
    print(player +"'s turn")
    loc=input("Choose the location(1-9) ")

    valid = False
    while not valid:
        while loc not in ["1","2","3","4","5","6","7","8","9"]:
            loc = input("Invalid Input. Please enter a number between 1 and 9 ")

        loc=int(loc)-1

        if tictactoe[loc] == "_":
            valid = True
        else:
            print("The position is already occupied. Try again.")

    tictactoe[loc] = player
    display()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    global winner
    row_winner=check_rows()
    column_winner = check_columns()
    diagnol_winner = check_diagnols()

    if row_winner:
        winner= row_winner
    elif column_winner:
        winner=column_winner
    elif diagnol_winner:
        winner=diagnol_winner
    else:
        winner=None
    return

def check_rows():
    global game_still_going
    row1= tictactoe[0]==tictactoe[1]==tictactoe[2] != "_"
    row2= tictactoe[3]==tictactoe[4]==tictactoe[5] != "_"
    row3= tictactoe[6]==tictactoe[7]==tictactoe[8] != "_"

    if row1 or row2 or row3:
        game_still_going=False
    if row1:
        return tictactoe[0]
    elif row2:
        return tictactoe[3]
    elif row3:
        return tictactoe[6]
    return

def check_columns():
    global game_still_going
    col1= tictactoe[0]==tictactoe[3]==tictactoe[6] != "_"
    col2= tictactoe[1]==tictactoe[4]==tictactoe[7] != "_"
    col3= tictactoe[2]==tictactoe[5]==tictactoe[8] != "_"
    if col1 or col2 or col3:
        game_still_going=False
    if col1:
        return tictactoe[0]
    elif col2:
        return tictactoe[1]
    elif col3:
        return tictactoe[2]
    return

def check_diagnols():
    global game_still_going
    diag1= tictactoe[0]==tictactoe[4]==tictactoe[8] != "_"
    diag2= tictactoe[2]==tictactoe[4]==tictactoe[6] != "_"
    
    if diag1 or diag2:
        game_still_going=False
    if diag1:
        return tictactoe[0]
    elif diag2:
        return tictactoe[6]
    return

def check_if_tie():
    global game_still_going
    if "_" not in tictactoe:
        game_still_going=False
    return

def flip_player():
    global current_player

    if current_player=="X":
        current_player="0"
    
    elif current_player=="0":
        current_player="X"
    return

play()
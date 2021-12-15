table = [[' ',' ',' ',' ',' ',' ',' ',' ',],
         [' ',' ',' ',' ',' ',' ',' ',' ',],
         [' ',' ',' ',' ',' ',' ',' ',' ',],
         [' ',' ',' ',' ',' ',' ',' ',' ',],
         [' ',' ',' ',' ',' ',' ',' ',' ',],
         [' ',' ',' ',' ',' ',' ',' ',' ',],
         [' ',' ',' ',' ',' ',' ',' ',' ',],
         [' ',' ',' ',' ',' ',' ',' ',' ',]]

def add_coin(coin,location):
    i = location
    for j in range(1,8):
        if table[-j][i] == ' ':
            table[-j][i] = coin
            break


def winning(coin,player):
    #checking horizontal
    for row in range(0,8):
        for col in range(0,5):
            if table[row][col] == coin and table[row][col+1] == coin and table[row][col+2] == coin and table[row][col+3] == coin:
                return True

    #checking vertical
    for row in range(0,5):
        for col in range(0,8):
            if table[row][col] == coin and table[row+1][col] == coin and table[row+2][col] == coin and table[row+3][col] == coin:
                return True


    #checking right side diagonal
    for row in range(3,8):
        for col in range(0,5):
            if table[row][col] == coin and table[row-1][col+1] == coin and table[row-2][col+2] == coin and table[row-3][col+3] == coin:
                return True

    #checking left side diagonal
    for row in range(3,8):
        for col in range(3,8):
            if table[row][col] == coin and table[row-1][col-1] == coin and table[row-2][col-2] == coin and table[row-3][col-3] == coin:
                return True


def print_table():
    for i in range(0, 8):
        print("   " + str(i) + "  ", end='')
    print()
    for i in range(0, 8):
        print("+-----" * 8)
        for j in range(0, 8):
            print("|", end='  ')
            print(table[i][j], end='  ')
        print("|")
    print("+-----" * 8, end='')
    print('+')

print("player 1 will be coin 'x' and player 2 will be coin 'o' ")
print()
print()
turn = 1
print_table()
print()
print()
while True:
    if turn%2 == 0:
        coin = 'o'
        player = "player 2"
    else:
        coin = 'x'
        player = "player 1"

    print("it is " + player + "'s turn!")
    print()
    location = int(input("Choose the coloumn in which you would like to add your coin -> "))
    add_coin(coin, location)
    print()
    print("coin has been added")
    print()
    print()
    turn += 1
    print_table()
    print()
    print()
    print()
    print()
    print()
    if winning(coin,player) == True:
        print(player + " who has " + coin + " coin has won!")
        break


















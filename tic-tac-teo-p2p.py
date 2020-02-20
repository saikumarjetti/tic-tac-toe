def print_mat(p1, p2, v=" "):
    if p1 != -1:
        matrix[p1][p2] = v
    print("**********")
    print(f" {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]}")
    print(f"_ _|_ _|_ _")
    print(f" {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]}")
    print(f"_ _|_ _|_ _")
    print(f" {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]}")
    print(f"   |   |  ")
    print("**********")


# Checking all possible wining rows
def check_winner():
    if matrix[0][0] == matrix[0][1] == matrix[0][2] != " ":
        return matrix[0][0]
    elif matrix[1][0] == matrix[1][1] == matrix[1][2] != " ":
        return matrix[1][0]
    elif matrix[2][0] == matrix[2][1] == matrix[2][2] != " ":
        return matrix[2][0]
    elif matrix[0][0] == matrix[1][0] == matrix[2][0] != " ":
        return matrix[0][0]
    elif matrix[0][1] == matrix[1][1] == matrix[2][1] != " ":
        return matrix[0][1]
    elif matrix[0][2] == matrix[1][2] == matrix[2][2] != " ":
        return matrix[0][2]
    elif matrix[0][0] == matrix[1][1] == matrix[2][2] != " ":
        return matrix[0][0]
    elif matrix[2][0] == matrix[1][1] == matrix[0][2] != " ":
        return matrix[2][0]
    else:
        return -1


# Printing winner
def p_winner(s):
    if s == u1:
        print(f"The Winner is {user1}")
    else:
        print(f"The Winner is {user2}")
    exit(0)


# To stop replacing data in matrix
def check_error(k1, k2):
    if matrix[k1][k2] == " ":
        return 1
    else:
        return -1


#  Number of filled block's
filledBlocks = 0
print("Welcome to the tic tac toe game!\n")

user1 = input("User1 name : ")
user2 = input("User1 name : ")

matrix = [[" " for i in range(3)] for j in range(3)]
print_mat(-1, -1)
print(f"{user1} select your symbol ")
u1 = input('\nselect your symbol (X | O) : ')
u2 = "x" if u1 == "o" else "o"

print(f'{user1} symbol is "{u1}"')
print(f'{user2} symbol is "{u2}"')

# filling the data

while filledBlocks < 10:
    # user input
    while True:
        pos = input(f"{user1} enter the  position (x y): ")
        if check_error(int(pos[0]), int(pos[1])) == 1:
            break
        else:
            print("This position is already filled, try another.")

    print(f"{user1} input ")
    print_mat(int(pos[0]), int(pos[1]), u1)
    filledBlocks += 1
    # Checking for winner
    if filledBlocks > 3:
        winD = check_winner()
        if winD != -1:
            p_winner(winD)

    if filledBlocks >= 9:
        print("\n******Draw********")
        exit(0)

    # User2 input
    while True:
        cPos = input(f"{user2} enter the  position (x y): ")
        if check_error(int(cPos[0]), int(cPos[1])) == 1:
            break
        else:
            print("This position is already filled, try another.")

    # printing grid for User2
    print(f"{user2} input ")
    filledBlocks += 1
    print_mat(int(cPos[0]), int(cPos[1]), u2)

    if filledBlocks > 2:
        winD = check_winner()
        if winD != -1:
            p_winner(winD)

import random as rd


def print_mat(p1, p2, v=" "):
    if p1 != -1:
        a[p1][p2] = v
    print("************")
    print(f" {a[0][0]} | {a[0][1]} | {a[0][2]}")
    print(f"_ _|_ _|_ _")
    print(f" {a[1][0]} | {a[1][1]} | {a[1][2]}")
    print(f"_ _|_ _|_ _")
    print(f" {a[2][0]} | {a[2][1]} | {a[2][2]}")
    print(f"   |   |  ")
    print("************")


# Checking all possible wining rows
def check_winner():
    if a[0][0] == a[0][1] == a[0][2] != " ":
        return a[0][0]
    elif a[1][0] == a[1][1] == a[1][2] != " ":
        return a[1][0]
    elif a[2][0] == a[2][1] == a[2][2] != " ":
        return a[2][0]
    elif a[0][0] == a[1][0] == a[2][0] != " ":
        return a[0][0]
    elif a[0][1] == a[1][1] == a[2][1] != " ":
        return a[0][1]
    elif a[0][2] == a[1][2] == a[2][2] != " ":
        return a[0][2]
    elif a[0][0] == a[1][1] == a[2][2] != " ":
        return a[0][0]
    elif a[2][0] == a[1][1] == a[0][2] != " ":
        return a[2][0]
    else:
        return -1


# Printing winner
def p_winner(s):
    if s == u_s:
        print("The Winner is Human")
    else:
        print("The Winner is computer")
    exit(0)


# To stop replacing data in matrix
def check_error(k1, k2):
    if a[k1][k2] == " ":
        return 1
    else:
        return -1


#  Number of filled block's
filledBlocks = 0
print("Welcome to the tic tac toe game!\n")

a = [[" " for i in range(3)] for j in range(3)]
print_mat(-1, -1)

u_s = input('\nselect your symbol (X | O) : ')
c_s = "x" if u_s == "o" else "o"

print(f'user symbol is "{u_s}"')
print(f'computer symbol is "{c_s}"')

# filling the data

while filledBlocks < 10:
    # user input
    while True:
        pos = input("Enter the position (x y): ")
        if check_error(int(pos[0]), int(pos[1])) == 1:
            break
        else:
            print("This position is already filled try another.")

    print("User input ")
    print_mat(int(pos[0]), int(pos[1]), u_s)
    filledBlocks += 1
    # Checking for winner
    if filledBlocks > 3:
        winD = check_winner()
        if winD != -1:
            p_winner(winD)
    if filledBlocks >= 9:
        print("\n******Draw********")
        exit(0)

    # computer input
    while True:
        cPos = [rd.randint(0, 2) for i in range(2)]
        if check_error(int(cPos[0]), int(cPos[1])) == 1:
            break

    # printing grid for computer
    print("Computer input ")
    filledBlocks += 1
    print_mat(int(cPos[0]), int(cPos[1]), c_s)

    if filledBlocks > 2:
        winD = check_winner()
        if winD != -1:
            p_winner(winD)

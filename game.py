matrix = [["*", 1, 2, 3],
          [1, " ", " ", " "],
          [2, " ", " ", " "],
          [3, " ", " ", " "]
          ]


def take_a_move(simbol):
    i, j = int(input("Введите номер строки")), int(input("Введите номер столбца"))
    if matrix[i][j] == " ":
        matrix[i][j] = simbol
    else:
        print("Ячейка занята, выберите другую!")
        i, j = int(input("Введите номер строки")), int(input("Введите номер столбца"))
        if matrix[i][j] == " ":
            matrix[i][j] = simbol
        else:
            print("Ваш ход аннулирован!")
    return


def proof_of_win(test):
    for i in range(1, 4):
        winner = True
        for j in range(1, 4):
            if matrix[i][j] != test:
                winner = False
        if winner:
            return True
    for j in range(1, 4):
        winner = True
        for i in range(1, 4):
            if matrix[i][j] != test:
                winner = False
        if winner:
            return True
    winner = True
    if matrix[1][1] != test or matrix[2][2] != test or matrix[3][3] != test:
        winner = False
    if winner:
        return True
    winner = True
    if matrix[1][3] != test or matrix[2][2] != test or matrix[3][1] != test:
        winner = False
    if winner:
        return True


counter = 1
while counter < 10:
    for i in range(0, 4):
        print()
        for j in range(0, 4):
            print(matrix[i][j], end=" ")
    print()

    if counter % 2 != 0:
        take = "x"
    else:
        take = "o"

    print(f"ход {counter}, ходит '{take}':")

    if take == "x":
        take_a_move(take)
        counter += 1
        if proof_of_win(take):
            for i in range(0, 4):
                print()
                for j in range(0, 4):
                    print(matrix[i][j], end=" ")
            print()
            print(f"'{take}' победил! Игра окончена.")
            counter = 11

    if take == "o":
        take_a_move(take)
        counter += 1
        if proof_of_win(take):
            for i in range(0, 4):
                print()
                for j in range(0, 4):
                    print(matrix[i][j], end=" ")
            print()
            print(f"'{take}' победил! Игра окончена.")
            counter = 11

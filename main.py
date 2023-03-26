matrix_ = [['-'] * 4 for i in range(4)]  # создаем матрицу 4х4
matrix_[0] = list(range(4))  # присваиваем значения оси Х


def chek_the_matrix(x_y):  # функция проверки условий на выйгрыш

    count_diagonal = 0  # счетчик диогонали если будет 3 то выйгрыш
    count_reverse_diagonal = 0  # счетчик обратной диогонали если будет 3 то выйгрыш
    for i in range(1, 4):
        count_x = 0  # счетчик для оси х если будет 3 то выйгрыш
        count_y = 0  # счетчик для оси y если будет 3 то выйгрыш
        if matrix_[i][i] == x_y:
            count_diagonal += 1
        if matrix_[4 - i][i] == x_y:
            count_reverse_diagonal += 1
        for j in range(1, 4):
            if matrix_[i][j] == x_y:
                count_x += 1
            if matrix_[j][i] == x_y:
                count_y += 1

        if count_x == 3 or count_y == 3:
            return True
    if count_diagonal == 3 or count_reverse_diagonal == 3:
        return True


def paint_matrix():  # функция прорисовки матрицы
    for i in range(4):
        for j in range(4):
            if not j:  # присваиваем значения оси Y
                matrix_[i][j] = i
            print(matrix_[i][j], end='  ')
        print()


print('Игра начинается')
paint_matrix()

count = 0  # счетчик ходов если 9 то ничья
while True:  # блок кода игры
    # запрашиваем координаты 'Х'
    player_x = list(map(int, input('Игрок 1 введите две координаты "X" через пробел: ').split()))
    count += 1

    if matrix_[player_x[1]][player_x[0]] != '-':  # проверяем не занята ли ячейка
        print('Эта клетка уже занята. Попробуйте заного')
        break

    matrix_[player_x[1]][player_x[0]] = 'x'  # присваиваем 'х' в матрицу
    paint_matrix()
    if chek_the_matrix('x'):  # проверяем на выйгрыш
        print('Выйграл игрок 1 КРЕСТИКИ')
        break

    if count == 9:
        print('Ничья')
        break
    # заправшиваем координаты '0'
    player_y = list(map(int, input('Игрок 2 введите две координаты "0" через пробел: ').split()))

    if matrix_[player_y[1]][player_y[0]] != '-':  # проверяем не занята ли ячейка
        print('Эта клетка уже занята. Попробуйте заного')  # не понял как вернуть цикл к запросу координат  Y
        break                                              # в случае ошибочно введенных координат
                                                           # пришлось сделать через break
    matrix_[player_y[1]][player_y[0]] = '0'  # присваиваем '0' в матрицу
    paint_matrix()
    if chek_the_matrix('0'):  # проверяем на выйгрыш
        print('Выйграл игрок 2 НОЛИКИ')
        break


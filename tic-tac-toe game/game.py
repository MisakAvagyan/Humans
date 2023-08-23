lst1 = ['-', '-', '-']
lst2 = ['-', '-', '-']
lst3 = ['-', '-', '-']

print('Lines are numbered like:\n'
      '1-2-3\n'
      '4-5-6\n'
      '7-8-9')

print(''.join(lst1))
symbol = input('Choose (x) or (o) - ')

if symbol == 'x':
    symbol2 = 'o'
elif symbol == 'o':
    symbol2 = 'x'


def print_board():
    print(''.join(lst1))
    print(''.join(lst2))
    print(''.join(lst3))


def check_winner(symbol):
    for row in [lst1, lst2, lst3]:
        if all(cell == symbol for cell in row):
            return True

    for vert in range(3):
        if all(row[vert] == symbol for row in [lst1, lst2, lst3]):
            return True

    if all(lst1[i] == symbol for i in range(3)) or all(lst2[i] == symbol for i in range(3)) or all(lst3[i] == symbol for i in range(3)):
        return True

    if lst1[0] == lst2[1] == lst3[2] == symbol or lst1[2] == lst2[1] == lst3[0] == symbol:
        return True

    return False


used_cells = set()

while True:
    num = int(input('Write the numbered line - '))
    if num not in used_cells:
        used_cells.add(num)
        if num == 1:
            lst1[0] = symbol
        elif num == 2:
            lst1[1] = symbol
        elif num == 3:
            lst1[2] = symbol
        elif num == 4:
            lst2[0] = symbol
        elif num == 5:
            lst2[1] = symbol
        elif num == 6:
            lst2[2] = symbol
        elif num == 7:
            lst3[0] = symbol
        elif num == 8:
            lst3[1] = symbol
        elif num == 9:
            lst3[2] = symbol
        print_board()

        if check_winner(symbol):
            print(symbol, 'wins!')
            break

        if len(used_cells) == 9:
            print("It's a draw!")
            break

        num2 = int(input('Write the second numbered line - '))
        if num2 not in used_cells:
            used_cells.add(num2)
            if num2 == 1:
                lst1[0] = symbol2
            elif num2 == 2:
                lst1[1] = symbol2
            elif num2 == 3:
                lst1[2] = symbol2
            elif num2 == 4:
                lst2[0] = symbol2
            elif num2 == 5:
                lst2[1] = symbol2
            elif num2 == 6:
                lst2[2] = symbol2
            elif num2 == 7:
                lst3[0] = symbol2
            elif num2 == 8:
                lst3[1] = symbol2
            elif num2 == 9:
                lst3[2] = symbol2
            print_board()

            if check_winner(symbol2):
                print(symbol2, 'wins!')
                break
    else:
        print("Cell already taken. Try again.")

# some comment
def numbers(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    elif num == 3:
        return 1
    else:
        return numbers(num - 1) + numbers(num - 2)


def main():
    num = int(input('enter a number - '))
    print('Fibonacci number is - ', numbers(num))


if __name__ == '__main__':
    main()

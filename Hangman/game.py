import random


def game_mode():
    while True:
        st = input("Choose the words (food or vehicle) - ").lower()
        if st in ['food', 'vehicle']:
            return st
        else:
            print("No such option, please try again")


def hangman(attempts):
    lst1 = ['', '', '', '']
    lst2 = ['', '', '', '']
    lst3 = ['', '', '', '']
    lst4 = ['', '', '', '']
    lst5 = ['', '', '', '']
    lst6 = ['', '', '', '']
    if attempts <= 5:
        lst6[0] = '_'
        lst6[1] = '|'
        lst6[2] = '_'
    if attempts <= 4:
        lst5[1] = ' |'
        lst4[1] = ' |'
        lst3[1] = ' |'
        lst2[1] = ' |'
    if attempts <= 3:
        lst1[1] = '  _'
        lst1[2] = ' _'
        lst1[3] = ' _'
    if attempts <= 2:
        lst2[3] = '   |'
        lst3[3] = '   o'
    if attempts <= 1:
        lst4[3] = '  /|\\'
    if attempts <= 0:
        lst5[3] = '   |'
        lst6[3] = ' / \\'
    print(''.join(lst1), '\n', ''.join(lst2), '\n', ''.join(lst3), '\n', ''.join(lst4), '\n', ''.join(
        lst5), '\n', ''.join(lst6))


def game(st):
    food = ["banana", "cherry", "grape", "apple", "cheese", "watermelon", "cucumber", "potato", "tomato"]
    vehicle = ["car", "bus", "bike", "train", "truck", "motorcycle", "scooter", "jet-ski", "plane"]

    if st == 'food':
        word = random.choice(food)
    elif st == 'vehicle':
        word = random.choice(vehicle)
    else:
        return 'No such option, please try again'

    letters = set()
    attempts = 6

    print('--Guess the word--')
    while attempts > 0:
        result = ''.join([letter if letter in letters else '-' for letter in word])
        print(result)

        if result == word:
            return 'Congrats! You guessed the word -', word

        letter = input("Write the letter - ").lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Please, write one letter")
            continue

        if letter in letters:
            print("You have already guessed this letter")
            continue

        letters.add(letter)

        if letter not in word:
            attempts -= 1
            print('No such letter in the word, attempts left -', attempts)
            hangman(attempts)

    return 'You lost, the word was -', word


def main():
    mode = game_mode()
    result = game(mode)
    print(result)


if __name__ == '__main__':
    main()

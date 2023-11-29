# Jogo da Adivinhação

from random import randint
from os import system, name

stop = False

def ClearConsole():
    return system('cls' if name == 'nt' else 'clear')

def SecretNumber():
    max_range = randint(1, 60)
    min_range = randint(1, 60)

    if max_range < min_range:
        while max_range < min_range:
            max_range = randint(1, 60)
    elif min_range > max_range:
        while min_range > max_range:
            min_range = randint(1, 60)
    elif min_range == max_range:
        while min_range == max_range:
            min_range = randint(1, 60)
            max_range = randint(1, 60)

    secret_number = randint(min_range, max_range)
    return min_range, max_range, secret_number

def Play():
    trys = 3
    min_range, max_range, secret_number = SecretNumber()
    
    while trys > 0:
        ClearConsole()
        # print(f'*** {secret_number} ***') # Secret Number
        print(f"Trys: {trys}\n")
        print(f'The secret number is between {min_range} and {max_range}')
        number = int(input("Guess the number: "))
        if number != secret_number:
            trys -= 1
            ClearConsole()
            print(f"Trys: {trys}\n")
            print("Wrong number!")
            
        elif number == secret_number:
            ClearConsole()
            print("Congratulations!\nYou win!\n")
            option = int(input('Do you want to play again?\n1 - Yes\n2 - No\n => '))
            if option == 1:
                Play()
            elif option == 2:
                MainMenu()
            else:
                print("Invalid option!")
        else:
            print("Invalid number!")

    if trys == 0:
        ClearConsole()
        print("Game Over!")
        print(f'The secret number is: {secret_number}')
        option = int(input('Do you want to play again?\n1 - Yes\n2 - No\n => '))
        if option == 1:
            Play()
        elif option == 2:
            MainMenu()
        else:
            print("Invalid option!")

def Rules():
    print("Not Available...")
    MainMenu()

def MainMenu():
    print("_________________________________\n")
    print("    Secret Number - The Game\n   ")
    print("    GitHub: spy-exe")
    print("_________________________________\n")
    print("Select a option:")
    print("1 - Play")
    print("1 - Rules")
    print("2 - Exit\n")
    option = int(input(" =>  "))

    if option == 1:
        Play()
    elif option == 2:
        Rules()
    elif option == 3:
        print("Closing...")
    else:
        print("Invalid Option!")
        MainMenu()

MainMenu()
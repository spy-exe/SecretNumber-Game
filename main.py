# Jogo da Adivinhação
from random import randint
from os import system, name

# Default Values
default_min_range = 1
default_max_range = 60
default_trys = 10

def ClearConsole():
    return system('cls' if name == 'nt' else 'clear')

def SecretNumber(trys, min_range, max_range):

    while max_range < min_range:
        max_range = randint(min_range, max_range)
        if (max_range - min_range) != 15:
            max_range = randint(min_range, max_range)
    while min_range > max_range:
        min_range = randint(min_range, max_range)
        if (max_range - min_range) != 15:
            min_range = randint(min_range, max_range)
    while min_range == max_range:
        min_range = randint(min_range, max_range)
        max_range = randint(min_range, max_range)
        if (max_range - min_range) != 15:
            min_range = randint(min_range, max_range)
            max_range = randint(min_range, max_range)

    """
    if max_range < min_range: 
        while max_range < min_range:
            max_range = randint(min_range, max_range)
            if (max_range - min_range) < trys:
                min_range = randint(min_range, max_range)

    elif min_range > max_range:
        while min_range > max_range:
            min_range = randint(min_range, max_range)
            if (max_range - min_range) < trys:
                min_range = randint(min_range, max_range)

    elif min_range == max_range:
        while min_range == max_range:
            min_range = randint(min_range, max_range)
            max_range = randint(min_range, max_range)
            if (max_range - min_range) < trys:
                min_range = randint(min_range, max_range)
    """
    secret_number = randint(min_range, max_range)
    return min_range, max_range, secret_number

def Play(trys):
    min_range, max_range, secret_number = SecretNumber(trys, default_min_range, default_max_range)
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
                Play(default_trys)
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
            Play(default_trys)
        elif option == 2:
            MainMenu()
        else:
            print("Invalid option!")

def Rules():
    print("Not Available...")
    MainMenu()

def Settings():
    
    print("Select an option:")
    print("1 - Change the number of trys")
    print("2 - Change the range of numbers\n")
    print("3 - Back\n")
    option = int(input("Select an option\n =>   "))

    if option == 1:
        ClearConsole()
        SettingsTrysMenu(default_trys)
    elif option == 2:
        ClearConsole()
        SettingsRangeMenu(default_min_range, default_max_range)
    elif option == 3:
        ClearConsole()
        MainMenu()
    else:
        ClearConsole()
        print("Invalid option!")
        Settings()

def SettingsTrysMenu(default_trys):
        print(f'Default: 10 trys')
        print(f"Actual: {trys} trys")
        print("Max allowed: 100 trys")
        print("Min allowed: 1 trys")
        trys = int(input("Select the number of trys\n =>   "))
        if trys > 100:
            ClearConsole()
            print("This number is bigger than 100!")
            trys = default_trys
            SettingsTrysMenu(default_trys)
        elif trys < 1:
            ClearConsole()
            trys = default_trys
            print("This number is smaller than 1!")
            SettingsTrysMenu(default_trys)
        else:
            ClearConsole()
            print(f'You changed to {trys} trys!')
            Settings()

        

def SettingsRangeMenu(default_min_range, default_max_range):
    print(f'Default: 1 - 60')
    print(f"Actual: {default_min_range} - {default_max_range}")
    print("Max allowed: 1 - 10.000")
    print("Min allowed: 1 - 10.000")
    min_range = int(input("Select the min number\n =>   "))
    max_range = int(input("Select the max number\n =>   "))

    if min_range > 10000 or max_range > 10000:
        ClearConsole()
        print("This number is bigger than 10.000! Try Again!")
        SettingsRangeMenu(min_range, max_range)
        min_range = default_min_range
        min_range = default_min_range

    elif min_range < 1 or max_range < 1:
        ClearConsole()
        min_range = default_min_range
        min_range = default_min_range
        print("This number is smaller than 1! Try Again!")
        SettingsRangeMenu(min_range, max_range)

    elif min_range == max_range:
        ClearConsole()
        min_range = default_min_range
        min_range = default_min_range
        print("Equals numbers not allowed! Try Again!")
        SettingsRangeMenu(min_range, max_range)
    else:
        ClearConsole()
        print(f'You changed to {min_range} - {max_range} range!')
    Settings()

    
    return min_range, max_range
    

def MainMenu():
    print("_________________________________\n")
    print("    Secret Number - The Game\n   ")
    print("    GitHub: spy-exe")
    print("_________________________________\n")
    print("Select a option:")
    print("1 - Play")
    print("2 - Rules")
    print("3 - Settings\n")
    print("4 - Exit\n")
    option = int(input(" =>  "))

    if option == 1:
        Play(default_trys)
    elif option == 2:
        Rules()
    elif option == 3:
        Settings()
    elif option == 4:
        print("Closing...")
    else:
        print("Invalid Option!")
        MainMenu()

MainMenu()

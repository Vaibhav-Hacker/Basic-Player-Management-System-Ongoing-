# A VERY BASIC PLAYER DATA SYSTEM --------------------------------------------------------------------------------------
# SUPPORTS THE C.R.U.D SYSTEM ---------------------------------------------------------------------------------------
# AUTHOR: VAIBHAV TANWAR

import random


def player_entry():
    file = open("Players.txt", "w")
    try:
        num = int(input("Enter how many player you want to add: "))

        for i in range(1, num + 1):
            players = str(input("Enter all the players one by one: "))
            file.write("Player " + str(i) + ": " + players + "\n")

    except ValueError:
        print("Please Enter a numeric value!")
        exit(0)

    print("\nData has been entered...")
    file.close()


def select_player():
    f = open("Players.txt", "r")
    print("\nPlayer would be selected randomly")
    lines = f.readlines()
    selected = random.randrange(0, len(lines))
    player_selected = lines[selected]
    f.close()

    return player_selected


def add_players():
    f = open("Players.txt", "r")
    lines = f.readlines()
    f.close()
    f = open("Players.txt", "a")
    try:
        more = int(input("Enter the number of players you wish to add: "))

        for i in range(len(lines) + 1, len(lines) + more + 1):
            players = str(input("Enter all the players one by one: "))
            f.write("Player " + str(i) + ": " + players + "\n")

    except ValueError:
        print("Please Enter a numeric value!")
        exit(0)

    f.close()


def show_players():
    f = open("Players.txt", "r")
    print("\n")
    players = f.read()
    f.close()

    return players


def remove():  # NEW FEATURE
    file = open("Players.txt", "r")
    f = file.readlines()
    if len(f) == 0:
        print("Nothing to remove!\n")
        return None
    
    rem = int(input("Please enter the Player to remove: "))
    for i in range(len(f)):
        if i == rem - 1:
            f[rem - 1] = ""

    file.close()
    file = open("Players.txt", "w")
    file.writelines(f)
    file.close()


if __name__ == "__main__":
    while True:
        options = [
            "\t1: Enter players. (Will overwrite existing players)",
            "\t2: Select player.",
            "\t3: Add more players.",
            "\t4: Show players.",
            "\t5: Remove Player.",
            "\t6: Exit."
        ]

        print("\nHere are some operations to perform on the Data file...\n")

        for a in options:
            print(a)

        try:
            choice = int(input("\nPlease Select an Operation -> "))
        
            if choice == 1:
                player_entry()
            elif choice == 2:
                player = select_player()
                print(player)
            elif choice == 3:
                add_players()
            elif choice == 4:
                x = show_players()
                print(x)
            elif choice == 5:
                remove()
            elif choice == 6:
                print("Bye Bye! \N{smiling face with sunglasses}")
                exit(0)
            else:
                print("Invalid Option Selected!")
                break
        except ValueError:
            print("Please Enter a Proper Value!")

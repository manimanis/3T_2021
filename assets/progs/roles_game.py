def choose_option(question, choice1, choice2):
    while True:
        print(question)
        print("0: Return back")
        print(f"1: {choice1}")
        print(f"2: {choice2}")

        choice = input("Your choice ? ")

        if choice in ['0', '1', '2']:
            return choice

        print('Wrong choice!')


def game_over(msg):
    print()
    print('=-=-' * 13)
    print('|                G A M E   O V E R                 |')
    print('|' + msg.center(50) + '|')
    print('=-=-' * 13)
    quit()


def winner():
    show_title("Congratulations, you won the game!")

def show_title(room):
    print()
    print('-' * 46)
    print('---      D I A M O N D   H U N T E R       ---')
    print('---' + room.center(40) + '---')
    print('-' * 46)
    print()

def lobby_room():
    show_title('Lobby Room')

    print("You entered the castle, you're in the lobby.")
    print("You see two doors in front of you.")

    choice = choose_option("Which door do you want to select?",
                           "Right door", 
                           "Left door")

    if choice == '0':
        game_over('You choose to escape you are a coward.')
    elif choice == '1':
        bear_room()
    else:
        monster_room()


def bear_room():
    show_title('Bear Room')

    print("You're in the Bear room.")
    print("You see a huge bear in front of you.")

    choice = choose_option("What you want to do?",
                           "Fight the bear", 
                           "Open the left door")

    if choice == '0':
        lobby_room()
    elif choice == '1':
        game_over("You fight the bear and you died!")
    else:
        lobby_room()


def monster_room():
    show_title('Monster Room')

    print("You're in the Monster room.")
    print("You see a tiny monster in front of you.")

    choice = choose_option("What you want to do?",
                           "Beat the monster to access the right door",
                           "Escape from the left door")

    if choice == '0':
        lobby_room()
    elif choice == '1':
        diamond_room()
    else:
        game_over("You died of terror in the next room!")


def diamond_room():
    show_title('Diamond Room')

    print("You're in the Diamond room.")
    print("You see a diamond in your left.")
    print("And a closed chest in your right.")

    choice = choose_option("What you want to do?",
                           "Take the diamond and leave the castle!",
                           "Force the chest to win more diamonds.")

    if choice == '0':
        monster_room()
    elif choice == '1':
        winner()
    else:
        game_over("The chest is full of vipers and scorpions!")

## Programme Principal ##
lobby_room()

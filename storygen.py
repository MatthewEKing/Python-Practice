from Companion import Companion

name = ""

# COMPANIONS
Lydia = Companion("Lydia", "Mace", "Sweet Roll")
Einar = Companion("Einar", "Gauntlets", "Bread")
Alesandel = Companion("Alesandel", "penis", "ass")

companions = [Lydia, Einar, Alesandel]


starting_dialogue = (
    "Welcome To The Inn",
    "I hope you had a safe journey",
    "Settle in and we'll talk business",
    "All settled?",
    "Good.",
    "We called you here because of the recent attacks from the goblins in the east",
    "We need your help to eliminate them"
)

choose_companion_dialogue = (
    "It'll be difficult if you go alone so...",
    "We have a couple of companions to accompany you"
)

no_companion_dialogue = (
    "Its dangerous to go alone y'know",
    "I hope you know what youre doing"
)

def setup_game():
    press_enter = True
    for lines in starting_dialogue:
        print(lines)
        if press_enter:
            player_input = input("Press Enter to Continue\n")
            press_enter = False
        else:
            input()



def init_playername():
    name_input = input("Whats your name traveler?\n")
    player_input = input("So your name is " + name_input + "? (Y/N)\n")
    if player_input == "Y":
        print("Its nice to meet you " + name_input)
        input()
        return name_input
    elif player_input == "N":
        init_playername()
    else:
        init_playername()


def choose_companion():
    for lines in choose_companion_dialogue:
        print(lines)
        input()
    print("Which one of these great warriors would you like to accompany you?")
    input()
    for companion in companions:
        print(companion.name)
    companion_choice_input = input()
    if companion_choice_input == Lydia.name:
        print("You chose " + Lydia.name + "! She uses a " + Lydia.weapon + " to fight")
    elif companion_choice_input == Einar.name:
        print("You chose " + Einar.name + "! He uses a " + Einar.weapon + " to fight")
    elif companion_choice_input == Alesandel.name:
        print("You chose " + Alesandel.name + "! He uses a " + Alesandel.weapon + " to fight")
    elif companion_choice_input == "None":
        no_companion_check = input("Are you sure you dont want company? (Y/N)\n")
        if no_companion_check == "Y":
            for lines in no_companion_dialogue:
                print(lines)
                input()
        elif no_companion_check == "N":
            choose_companion()
    else:
        choose_companion()

#setup_game()
#name = init_playername()
choose_companion()
# print(name)

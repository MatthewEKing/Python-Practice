from Companion import Companion

name = ""

starting_dialogue = (
    "Welcome To The Inn",
    "Hope you're doing well",
    "Test Dialogue"
)

def setup_game():
    for lines in starting_dialogue:
        print(lines)
        player_input = input()
        if player_input != "":



setup_game()

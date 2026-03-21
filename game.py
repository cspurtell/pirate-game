from player import Player

def create_player():
    print("Welcome to Pirate Game!")
    name = input("What shall your captain's name be? ").strip()

    if not name:
        name = "Unnamed Captain"

    print("Choose your speciality:")
    print("1. I want to be strong")
    print("2. I want to be charming")
    print("3. I want to be lucky")

    choice = input("> ").strip()

    strength = 5
    charisma = 5
    luck = 5

    if choice == "1":
        strength += 2
    elif choice == "2":
        charisma += 2
    elif choice == "3":
        luck += 2
    else:
        print("No specialty chosen. You are average in all things.")